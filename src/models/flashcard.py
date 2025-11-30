from dataclasses import dataclass

@dataclass
class Flashcard:
    question: str
    answer: str
    ease: float = 2.5
