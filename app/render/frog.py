import logging
from typing import Tuple

import pygame  # type: ignore

from app.game.state.controller import GameStateController
from app.game.state.player import Player


class FrogRender:
    radius = 64.0

    def __init__(self, parent_surface, data: GameStateController):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Init FrogRender")

        self.color = pygame.Color(0, 200, 200)
        self.data = data
        self.parent_surface = parent_surface

        self.surface = pygame.Surface(self.pos).convert()
        self.__draw()

    @property
    def pos(self) -> Tuple[float, float]:
        return (
            self.data.player.vector[0] - self.radius,
            self.data.player.vector[1] - self.radius
        )

    def __draw(self):
        ...

    def update(self):
        self.__draw()
        # self.parent_surface.blit(self.surface, self.pos)
