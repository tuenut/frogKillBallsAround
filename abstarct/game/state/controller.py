from abc import ABC, abstractmethod

import pygame

from abstarct.game.state.player import ABCPlayer


class ABCGameStateController(ABC):
    @property
    @abstractmethod
    def mouse(self) -> pygame.Vector2:
        ...

    @property
    @abstractmethod
    def player(self) -> ABCPlayer:
        ...

    @property
    @abstractmethod
    def bullets(self):
        ...

    @abstractmethod
    def update(self):
        ...