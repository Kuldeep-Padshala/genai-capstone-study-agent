from typing import Any, Dict, List

class MockLLMAgent:
    """A mocked LLM agent that 'generates' summaries, explanations, quiz questions and answers queries."""

    def summarize(self, text: str, max_length: int = 60) -> str:
        return (text[:max_length] + "...") if len(text) > max_length else text

    def explain(self, topic: str, level: str = "intro") -> str:
        return (
            f"Explanation ({level}) for {topic}: "
            f"This is a concise, learner-friendly explanation covering the main ideas and intuition."
        )

    def generate_quiz(self, topic: str, n_questions: int = 3) -> List[Dict[str, Any]]:
        return [
            {
                "q": f"Sample question {i+1} about {topic}",
                "a": f"Short model answer for question {i+1} on {topic}."
            }
            for i in range(n_questions)
        ]

    def answer_query(self, topic: str, query_type: str) -> str:
        if query_type == "prerequisites":
            return f"Prerequisites for {topic}: basic Python, linear algebra, probability."
        if query_type == "key_concepts":
            return f"Key concepts of {topic}: core algorithms, structure, examples."
        if query_type == "practice_problems":
            return f"Practice ideas for {topic}: implement concepts and solve exercises."
        return f"General advice for {topic}: explore examples."
