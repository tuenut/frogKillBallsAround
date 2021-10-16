import logging
import pygame
import math

from app.state import AppState
from config import GAME_SETTINGS


class Player:
    def __init__(self):
        self.x = GAME_SETTINGS["resolution"][0]
        self.y = GAME_SETTINGS["resolution"][1]

    @property
    def pos(self):
        return pygame.Vector2(self.x, self.y) / 2


class GameStateController:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.mouse = pygame.Vector2(pygame.mouse.get_pos())
        self.player = Player()

        self.__app_state = AppState()

    def update(self):
        self.mouse = pygame.Vector2(pygame.mouse.get_pos())
        self.__app_state.title = self.mouse
