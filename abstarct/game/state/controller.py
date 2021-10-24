from abc import ABC, abstractmethod
from typing import List

import pygame

from abstarct.game.state.gun_controller import ABCBullet


class ABCGameStateController(ABC):
    @property
    @abstractmethod
    def mouse(self) -> pygame.Vector2:
        ...

    @property
    @abstractmethod
    def player(self) -> pygame.Vector2:
        ...

    @property
    @abstractmethod
    def bullets(self) -> List[ABCBullet]:
        ...

    @abstractmethod
    def update(self):
        ...