from __future__ import annotations

import logging
import math
from typing import Type

import pygame

from app.events import EventManager
from abstarct.game.state.player import ABCShotVector
from app.game.state.mouse import MouseDescriptor
from config import GAME_SETTINGS


class Bullet:
    def __init__(self, start_pos, vector):
        self.start_pos = self.pos = pygame.Vector2(start_pos)
        self.target_vector = vector

    def update(self):
        # TODO calculate next position from current and target vector
        ...


class ShootingVector(ABCShotVector):
    mouse: pygame.Vector2 = MouseDescriptor()

    def __init__(self, player):
        self.x_limit = GAME_SETTINGS["resolution"][0]
        self.y_limit = GAME_SETTINGS["resolution"][1]
        self.__player = player

        self.fired_bullets = []

        self.update()

    def update(self):
        self.mouse = pygame.Vector2(pygame.mouse.get_pos())
        self.__update_shot_vector()
        for bullet in self.fired_bullets:
            bullet.update()

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

        in_top_part = self.mouse.x >= 0 and self.mouse.y <= self.y_limit / 2

        MC = self.mouse.distance_to(self.__player.vector)
        MQ = abs(self.x_limit / 2 - self.mouse.x)
        sin_MCQ = MQ / MC
        cos_MCQ = math.sqrt(1 - sin_MCQ ** 2)

        try:
            if in_top_part:
                ZM = self.mouse.y / cos_MCQ
            else:
                ZM = (self.y_limit - self.mouse.y) / cos_MCQ
        except ZeroDivisionError:
            if self.mouse.x <= self.x_limit / 2:
                return pygame.Vector2(0, self.y_limit / 2)
            else:
                return pygame.Vector2(self.x_limit, self.y_limit / 2)

        ZX = ZM * sin_MCQ

        if self.mouse.x <= self.x_limit / 2:
            if in_top_part:
                x = self.mouse.x - ZX
                y = 0
            else:
                x = self.mouse.x - ZX
                y = self.y_limit
        else:
            if in_top_part:
                x = self.mouse.x + ZX
                y = 0
            else:
                x = self.mouse.x + ZX
                y = self.y_limit

        self.__vector = pygame.Vector2(x, y)

    @property
    def vector(self):
        return self.__vector

    def add_bullet_to_vector(self):
        bullet = Bullet((self.x_limit / 2, self.y_limit / 2), self.vector)
        self.fired_bullets.append(bullet)


class GunShootingVectorDEscriptor:
    def __get__(self, instance: Type[Gun], owner=None):
        return instance._Gun__shooting_vector.vector


class Gun:
    vector: pygame.Vector2 = GunShootingVectorDEscriptor()

    def __init__(self, player):
        self.logger = logging.getLogger(__name__)

        self.__player = player
        self.__shooting_vector = ShootingVector(self.__player)

        self.events = EventManager()

        self.events.subscribe(
            event_type=pygame.MOUSEBUTTONDOWN,
            callback=self.fire,
            kwargs=["pos"]
        )

    def update(self):
        self.__shooting_vector.update()

    def fire(self, pos):
        self.logger.debug("FIRE!!!!!")
