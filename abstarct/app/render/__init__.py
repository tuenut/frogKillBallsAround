from abc import ABC, abstractmethod


class ABCRender(ABC):
    @abstractmethod
    def __init__(self, game_state, width: int = None, height: int = None):
        ...

    @abstractmethod
    def update(self):
        ...