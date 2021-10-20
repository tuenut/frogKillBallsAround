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

        self.__subscribe_onevents()

    def __subscribe_onevents(self):
        self.events.subscribe(
            event_type=pygame.MOUSEBUTTONDOWN,
            callback=self.state.bullets.fire,
            kwargs=["pos"],
            as_args=True
        )

    def update(self):
        self.state.update()
