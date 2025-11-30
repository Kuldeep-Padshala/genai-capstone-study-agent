import logging
import concurrent.futures
from typing import List, Dict, Any
from agents.llm_agent import MockLLMAgent
from agents.search_agent import ContentSearchAgent
from agents.flashcard_agent import FlashcardAgent
from memory.session_service import InMemorySessionService

log = logging.getLogger(__name__)

class StudyCoordinator:
    def __init__(self, session_service: InMemorySessionService):
        self.llm = MockLLMAgent()
        self.search_agent = ContentSearchAgent()
        self.flashcard_agent = FlashcardAgent(self.llm)
        self.sessions = session_service

    def create_or_get_session(self, user_id: str, metadata=None) -> str:
        return self.sessions.create_session(user_id, metadata)

    def plan_for(self, session_id: str, topics: List[str], weekly_hours: int = 5) -> Dict[str, Any]:
        log.info("Coordinator: Starting study plan generation...")
        self.sessions.set_state(session_id, "topics", topics)
        self.sessions.set_state(session_id, "weekly_hours", weekly_hours)

        results = {"resources": {}, "flashcards": {}, "quizzes": {}, "informative_queries": {}}

        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            future_search = {executor.submit(self.search_agent.run, t): t for t in topics}
            future_flash = {executor.submit(self.flashcard_agent.run, t, 4): t for t in topics}

            for future in concurrent.futures.as_completed(future_search):
                topic = future_search[future]
                results["resources"][topic] = future.result()

            for future in concurrent.futures.as_completed(future_flash):
                topic = future_flash[future]
                results["flashcards"][topic] = future.result()

        for topic in topics:
            results["quizzes"][topic] = self.llm.generate_quiz(topic, 3)

            results["informative_queries"][topic] = {
                qtype: self.llm.answer_query(topic, qtype)
                for qtype in ["prerequisites", "key_concepts", "practice_problems"]
            }

        self.sessions.set_state(session_id, "last_plan", results)
        return results
