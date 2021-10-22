from __future__ import annotations

import logging
import math
from typing import Type

import pygame

from abstarct.game.state.player import ABCShotVector
from app.game.state.mouse import MouseDescriptor
from config import GAME_SETTINGS


class ShootingVector(ABCShotVector):
    mouse: pygame.Vector2 = MouseDescriptor()

    def __init__(self, player_position: pygame.Vector2):
        self.x_limit = GAME_SETTINGS["resolution"][0]
        self.y_limit = GAME_SETTINGS["resolution"][1]
        self.player_position = player_position

        self.update()

    def update(self):
        self.__update_shot_vector()

    def __update_shot_vector(self):
        """
        Let assume mouse on point M(x, y), there is vector OM and
         right triangle OXM. Also we assume that player stays on center of field,
         there is triangle CMQ, where point Q is a normal on line CX',
         where (X' == x_limit / 2). We need to know point Z that belongs to
         one of axis or edge(limit) lines of field and belongs to line CM.
         I.e. we need to find vector CZ where is vector CM belongs  to CZ.

         We should find ∠ZMX == ∠MCQ, because this triangles is similar.
         Next with Pythagorean theorem we can find XZ and fin x coordinate of Z.

        TODO: For now Z lies on X axis or X limit line, and Y coordinate has
        TODO:  no restrictions, but should be limited with field edges.
        """

        aim_radius_vector = pygame.Vector2(
            self.mouse.x - self.player_position.x,
            self.mouse.y - self.player_position.y
        )
        angle_to_ox = aim_radius_vector.angle_to(pygame.Vector2(1, 0))
        angle_to_oy = aim_radius_vector.angle_to(pygame.Vector2(0, 1))
        self.sin_to_OX = math.sin(math.radians(angle_to_ox + 90))
        self.sin_to_OY = math.sin(math.radians(angle_to_oy + 90))

        self.__vector = pygame.Vector2((
            self.player_position.x + (640 - self.player_position.x) * self.sin_to_OX,
            self.player_position.y + (640 - self.player_position.y) * self.sin_to_OY,
        ))

    @property
    def vector(self):
        return self.__vector


class GunShootingVectorDEscriptor:
    def __get__(self, instance: Type[Gun], owner=None):
        return instance.shooting_vector.vector


class Gun:
    vector: pygame.Vector2 = GunShootingVectorDEscriptor()

    def __init__(self, player_position: pygame.Vector2):
        self.logger = logging.getLogger(__name__)

        self.shooting_vector = ShootingVector(player_position)

    def update(self):
        self.shooting_vector.update()
