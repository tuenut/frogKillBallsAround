import logging
import pygame  # type: ignore

from abstarct.app.render import ABCRender
from app.render.playground import PlayGround
from app.constants import COLOR_RENDER_BG

from app.game.state.controller import GameStateController

FROG_RADIUS = 64.0


class Render(ABCRender):
    def __init__(self, data, width=640, height=640):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Init Render...")

        self.__data = data

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(
            (self.width, self.height),
            pygame.DOUBLEBUF
        )

        self.surface = pygame.Surface(self.screen.get_size()).convert()
        self.surface.fill(COLOR_RENDER_BG)

    def __draw(self):
        pygame.draw.circle(
            surface=self.surface,
            color=pygame.Color(0, 200, 200),
            center=(self.width/2, self.height/2),
            radius=FROG_RADIUS
        )
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 0, 0),
            start_pos=self.__data.vector[0],
            end_pos=self.__data.vector[1]
        )

    def update(self):
        pygame.display.flip()
        self.surface.fill(COLOR_RENDER_BG)

        self.__draw()

        self.screen.blit(self.surface, (0, 0))
