from __future__ import annotations

import pygame

from abstarct.game.state.player import ABCPlayer
from app.game.state.mouse import MouseDescriptor
from app.game.state.gun import Gun
from config import GAME_SETTINGS


class Player(ABCPlayer):
    mouse: pygame.Vector2 = MouseDescriptor()

    def __init__(self, x=None, y=None):
        x = x if x is not None else GAME_SETTINGS["resolution"][0] / 2
        y = y if y is not None else GAME_SETTINGS["resolution"][1] / 2

        self.__vector = pygame.Vector2(x, y)
        self.gun = Gun(self)  # A GunKlass may be?

    @property
    def vector(self) -> pygame.Vector2:
        return pygame.Vector2(self.__vector)

    def update(self):
        self.gun.update()
