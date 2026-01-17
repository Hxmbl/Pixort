from enum import Enum

class Decision(Enum):
    UNDECIDED = 0
    KEEP = 1
    DELETE = 2


class ReviewState:
    def __init__(self, image_paths: list[str]):
        self.images = image_paths
        self.decisions = {p: Decision.UNDECIDED for p in image_paths}
        self.index = 0

    def current(self):
        if self.index >= len(self.images):
            return None
        return self.images[self.index]

    def keep(self):
        self.decisions[self.current()] = Decision.KEEP
        self.index += 1

    def delete(self):
        self.decisions[self.current()] = Decision.DELETE
        self.index += 1

    def finished(self):
        return self.index >= len(self.images)
