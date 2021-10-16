import logging
import pygame
import math

from app.state import AppState
from config import GAME_SETTINGS


class Frog:
    def __init__(self):
        self.pos = (
            math.ceil(GAME_SETTINGS["resolution"][0] / 2),
            math.ceil(GAME_SETTINGS["resolution"][1] / 2)
        )

    @property
    def vector(self) -> pygame.Vector2:
        return pygame.Vector2(self.pos)


class GameStateController:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.mouse_pos = pygame.mouse.get_pos()
        self.player = Frog()

        self.__app_state = AppState()

    @property
    def vector(self):
        return pygame.Vector2(self.player.pos), pygame.Vector2(self.mouse_pos)

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.__app_state.title = self.mouse_pos
