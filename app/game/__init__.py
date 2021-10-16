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

        self.__init_game_events()

    def update(self):
        self.state.update()

    def __init_game_events(self):
        self.events.subscribe(
            event_type=pygame.MOUSEBUTTONDOWN,
            callback=self._handle_mouse,
            kwargs=["pos", "button"]
        )

    def _handle_mouse(self, *args, pos, button, **kwargs):
        if button == pygame.BUTTON_LEFT:
            self.logger.debug(f"Click LMB on {pos}")

        elif button == pygame.BUTTON_RIGHT:
            self.logger.debug(f"Click RMB on {pos}")

        else:
            self.logger.debug(f"Mouse click on {pos}")
