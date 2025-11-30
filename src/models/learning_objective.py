from dataclasses import dataclass
from typing import List

@dataclass
class LearningObjective:
    topic: str
    difficulty: float
    prerequisites: List[str]
