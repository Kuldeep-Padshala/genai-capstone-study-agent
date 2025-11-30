from dataclasses import dataclass

@dataclass
class Resource:
    title: str
    url: str
    summary: str
    relevance: float
