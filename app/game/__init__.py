import logging
import pygame

from abstarct.app.game import ABCGame
from app.events import EventManager
from app.game.state.controller import GameStateController


class Game(ABCGame):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Init Game...")

        self.state = GameStateController()
        self.events = EventManager()

    def update(self):
        self.state.update()
