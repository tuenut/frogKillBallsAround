from abc import ABC, abstractmethod
from logging import Logger

from abstarct.app.game import ABCGame
from abstarct.app.render import ABCRender
from abstarct.app.state import ABCAppState


class ABCApp(ABC):
    """
    Attributes
    ----------
    logger : Logger
        logger object for class
    title : str
        Text for window title
    state : ABCAppState
        Application state
    game : ABCGame
        Game class
    _run_timer : float
        timer starts from start app
    """

    logger: Logger = None
    state: ABCAppState = None
    game: ABCGame = None
    render: ABCRender = None

    @abstractmethod
    def __init__(self):
        ...

    @property
    @abstractmethod
    def _run_timer(self) -> float:
        """Timer since app started"""
        ...

    @abstractmethod
    def run(self):
        """Mainloop"""
        ...

    @abstractmethod
    def exit(self):
        """Method executes for close app"""
        ...
