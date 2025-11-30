import logging
from typing import List
from models.flashcard import Flashcard
from agents.llm_agent import MockLLMAgent

log = logging.getLogger(__name__)

class FlashcardAgent:
    def __init__(self, llm_agent: MockLLMAgent):
        self.llm = llm_agent

    def run(self, topic: str, n_cards: int = 5) -> List[Flashcard]:
        log.info(f"[FlashcardAgent] Generating flashcards for: {topic}")
        cards = [
            Flashcard(
                question=f"What is key idea {i+1} in {topic}?",
                answer=self.llm.explain(topic, level='short')
            )
            for i in range(n_cards)
        ]
        log.info(f"[FlashcardAgent] Finished flashcards for: {topic}")
        return cards
