import time
import logging

log = logging.getLogger(__name__)

class LongRunningAgent:
    def __init__(self):
        self.progress = 0
        self.paused = False

    def step(self):
        if self.paused:
            log.info("LongRunningAgent is paused.")
            return

        self.progress += 10
        log.info(f"[LongRunningAgent] Progress: {self.progress}%")
        time.sleep(0.3)

        if self.progress >= 100:
            log.info("[LongRunningAgent] Task complete!")

    def pause(self):
        self.paused = True
        log.info("LongRunningAgent paused.")

    def resume(self):
        self.paused = False
        log.info("LongRunningAgent resumed.")
