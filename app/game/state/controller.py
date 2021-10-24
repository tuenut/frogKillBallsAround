import logging
import pygame

from abstarct.game.state.controller import ABCGameStateController
from app.game.state.gun_controller import GunController
from app.game.state.mouse import Mouse, MouseDescriptor
from app.game.state.player import Player
from app.state import AppState


class GameStateController(ABCGameStateController):
    mouse: pygame.Vector2 = MouseDescriptor()

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.__mouse = Mouse()
        self.__player = Player()
        self._gun = GunController(self.__player)

        self.__app_state = AppState()  # todo: ????

    @property
    def player(self) -> pygame.Vector2:
        return self.__player.vector

    @property
    def bullets(self) -> list:
        return self._gun.fired_bullets

    def update(self):
        self.__mouse.update()
        self.__player.update()
        self._gun.update()
