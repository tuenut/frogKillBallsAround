from abc import ABC, abstractmethod
from logging import Logger

from abstarct.app.render import ABCRender
from abstarct.game.state.controller import ABCGameStateController


class ABCGame(ABC):
    logger: Logger = None

    state: ABCGameStateController = None
    events = None

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def update(self):
        ...
