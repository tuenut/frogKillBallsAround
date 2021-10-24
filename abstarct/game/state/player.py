import pygame
from abc import ABC, abstractmethod


class ABCPlayer(ABC):
    @property
    @abstractmethod
    def vector(self) -> pygame.Vector2:
        ...

    @property
    @abstractmethod
    def mouse(self) -> pygame.Vector2:
        ...

    @abstractmethod
    def update(self):
        ...