import logging
import pygame

from abstarct.app.mainprocess import ABCApp
from app.render import Render
from app.state import AppState
from app.events import EventManager
from app.game import Game
from app.constants import FPS
from config import GAME_SETTINGS


class App(ABCApp):
    _run_timer = 0.0

    dimensions = GAME_SETTINGS["resolution"]

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Init App...")

        pygame.init()
        self._clock = pygame.time.Clock()

        self.state = AppState()
        self.events = EventManager()
        self.game = Game()
        self.render = Render(self.game.state, *self.dimensions)

        self.__configure_global_app_events()

    def run(self):
        self.state.run()
        self.__mainloop()
        self.exit()

    def exit(self):
        pygame.quit()

    def __mainloop(self):
        while self.state.is_run:
            self.events.check_events()

            if not self.state.is_pause:
                pygame.display.set_caption(self.state.title)
                self.__fps_update()
                self.game.update()
                self.render.update()

    def __configure_global_app_events(self):
        """
        TODO should load from ini-config r sort of...
        """
        self.events.subscribe(
            event_type=pygame.QUIT,
            callback=self.state.stop
        )
        self.events.subscribe(
            event_type=pygame.KEYDOWN,
            callback=self.state.stop,
            conditions={"key": pygame.K_q}
        )
        self.events.subscribe(
            event_type=pygame.KEYDOWN,
            callback=self.state.stop,
            conditions={"key": pygame.K_ESCAPE}
        )
        self.events.subscribe(
            event_type=pygame.KEYDOWN,
            callback=self.state.pause,
            conditions={"key": pygame.K_p}
        )

    def __fps_update(self):
        self._run_timer += (self._clock.tick(FPS) / 1000.0)
        # fps = f"FPS: {self._clock.get_fps():.2f} Playtime: {self._run_timer:.2f}"
        # self.state.title = fps
        ...
