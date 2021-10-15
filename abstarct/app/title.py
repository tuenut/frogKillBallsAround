from abc import ABC, abstractmethod


class AbcTitle(ABC):
    @property
    @abstractmethod
    def text(self) -> str:
        ...

    @text.setter
    @abstractmethod
    def text(self, value: str):
        ...

    @abstractmethod
    def enable_hint(self):
        ...

    @abstractmethod
    def disable_hint(self):
        ...


class ABCAppTitle(ABC):
    @abstractmethod
    def __get__(self, obj, object_type=None) -> str:
        ...

    @abstractmethod
    def __set__(self, obj, value: str):
        ...
