from abc import ABC, abstractmethod

from abstarct.app.title import ABCAppTitle


class ABCAppState(ABC):
    title: ABCAppTitle = None

    @property
    @abstractmethod
    def is_run(self) -> bool:
        """If False, then app in exiting phase."""
        ...

    @property
    @abstractmethod
    def is_pause(self) -> bool:
        """If True, then app paused."""
        ...

    @abstractmethod
    def pause(self):
        ...

    @abstractmethod
    def run(self):
        ...

    @abstractmethod
    def stop(self):
        ...
