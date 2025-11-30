import time
from models.resource import Resource
from typing import List
import logging

log = logging.getLogger(__name__)

class ContentSearchAgent:
    def run(self, topic: str) -> List[Resource]:
        log.info(f"[SearchAgent] Starting search for: {topic}")
        time.sleep(0.4)
        log.info(f"[SearchAgent] Finished search for: {topic}")

        playlist = "https://www.youtube.com/playlist?list=PLzJwCIvZuAFY-jBJS0-LlFB0dP469vsMG"
        return [
            Resource(
                title=f"{topic} — Dr Abhishek Playlist",
                url=playlist,
                summary=f"A curated playlist covering {topic}.",
                relevance=0.95
            ),
            Resource(
                title=f"{topic} — Deep dive article",
                url="https://example.com/deep",
                summary=f"In-depth notes for {topic}.",
                relevance=0.75
            )
        ]
