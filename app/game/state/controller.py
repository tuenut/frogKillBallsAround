import logging
import pygame

from abstarct.game.state.controller import ABCGameStateController
from app.game.state.mouse import Mouse, MouseDescriptor
from app.game.state.player import Player
from app.state import AppState


class GameStateController(ABCGameStateController):
    mouse: pygame.Vector2 = MouseDescriptor()

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.__mouse = Mouse()
        self.player = Player()

        self.__app_state = AppState()

    def update(self):
        self.__mouse.update()
        self.player.update()
