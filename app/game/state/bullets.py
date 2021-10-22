import logging
import random
import math

from typing import Tuple, Union

import pygame

from abstarct.game.state.player import ABCPlayer
from app.constants import FPS
from config import GAME_SETTINGS


class Bullet:
    SPEED = 10  # px per update tick

    def __init__(
            self,
            start_pos: Union[Tuple[int, int], pygame.Vector2],
            sin_to_OX: float,
            cos_to_OY: float
    ):
        self.start_pos = self.position = pygame.Vector2(start_pos)
        self.sin_to_OX = sin_to_OX
        self.sin_to_OY = cos_to_OY
        self.color = pygame.Color(*tuple(random.randint(100, 255) for i in range(3)))

    def update(self):
        # TODO calculate next position from current and target vector
        y_increment = self.SPEED * self.sin_to_OY
        x_increment = self.SPEED * self.sin_to_OX

        self.position = pygame.Vector2(self.position.x + x_increment, self.position.y + y_increment)


class BulletController:
    def __init__(self, player: ABCPlayer):
        self.logger = logging.getLogger(__name__)

        self.player = player
        self.fired_bullets = []

    def fire(self, fire_vector: Tuple[int, int]):
        self.logger.debug(f"FIRE!!! <{fire_vector}>, {type(fire_vector)}")

        bullet = Bullet(
            self.player.vector,
            self.player.gun.shooting_vector.sin_to_OX,
            self.player.gun.shooting_vector.sin_to_OY
        )

        self.fired_bullets.append(bullet)

    def update(self):
        for idx, bullet in enumerate(self.fired_bullets):
            bullet.update()

            if (bullet.position.x > GAME_SETTINGS["resolution"][0] + 30) \
                    or (bullet.position.y > GAME_SETTINGS["resolution"][1] + 30):
                self.fired_bullets.pop(idx)
                del bullet

    def __iter__(self):
        return iter(self.fired_bullets)
