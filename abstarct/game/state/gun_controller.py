from abc import ABC, abstractmethod
from typing import List, Tuple, Union

import pygame


class ABCBullet(ABC):
    x_factor: float = None
    y_factor: float = None
    color: pygame.Color = None
    vector = pygame.Vector2

    @abstractmethod
    def fire(self, aiming_vector: pygame.Vector2):
        ...

    @abstractmethod
    def update(self):
        ...


class ABCMagazine(ABC):
    @abstractmethod
    def get_bullet(self) -> ABCBullet:
        ...


class ABCGunController(ABC):
    magazine: ABCMagazine = None
    fired_bullets: List[ABCBullet] = None

    @abstractmethod
    def fire(sel, fire_vector: Union[Tuple[int, int], pygame.Vector2]):
        ...

    @abstractmethod
    def update(self):
        ...
