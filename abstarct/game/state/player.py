import pygame
from abc import ABC, abstractmethod


class ABCShotVector:
    mouse: pygame = None

    @abstractmethod
    def update(self):
        ...

    @property
    @abstractmethod
    def vector(self) -> pygame.Vector2:
        ...


class ABCGun(ABC):
    @property
    @abstractmethod
    def vector(self) -> pygame.Vector2:
        ...

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def fire(self):
        ...


class ABCPlayer(ABC):
    @property
    @abstractmethod
    def vector(self) -> pygame.Vector2:
        ...

    @abstractmethod
    def update(self):
        ...
