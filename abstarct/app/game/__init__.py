from abc import ABC, abstractmethod
from logging import Logger

from abstarct.app.render import ABCRender


class ABCGame(ABC):
    logger: Logger = None

    state = None

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def update(self):
        ...
