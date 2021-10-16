from abc import ABC, abstractmethod


class ABCRender(ABC):
    @abstractmethod
    def update(self):
        ...
