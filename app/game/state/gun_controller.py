import logging
import math
import random

import pygame

from abstarct.game.state.gun_controller import ABCBullet, ABCMagazine, ABCGunController
from abstarct.game.state.player import ABCPlayer
from config import GAME_SETTINGS


class Bullet(ABCBullet):
    SPEED = 15  # px per frame

    def __init__(self, start_pos: pygame.Vector2, color: pygame.Color):
        self.__start_pos = self.vector = pygame.Vector2(start_pos)

        self.x_factor = 0
        self.y_factor = 0

        self.color = color

    def fire(self, aiming_vector: pygame.Vector2):
        aim_radius_vector = pygame.Vector2(
            aiming_vector.x - self.__start_pos.x,
            aiming_vector.y - self.__start_pos.y
        )
        angle_to_ox = aim_radius_vector.angle_to(pygame.Vector2(1, 0))
        angle_to_oy = aim_radius_vector.angle_to(pygame.Vector2(0, 1))

        self.x_factor = math.cos(math.radians(angle_to_ox))
        self.y_factor = math.cos(math.radians(angle_to_oy))

    def update(self):
        y_increment = self.SPEED * self.y_factor
        x_increment = self.SPEED * self.x_factor

        self.vector = pygame.Vector2(
            self.vector.x + x_increment,
            self.vector.y + y_increment
        )


class Magazine(ABCMagazine):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    COLORS: list = (RED, GREEN, BLUE)

    PALETTE: dict = {
        RED: pygame.Color(200, 0, 0),
        GREEN: pygame.Color(0, 200, 0),
        BLUE: pygame.Color(0, 0, 200),
    }
    __default_weight: int = 15
    __color_weights: dict = {
        RED: __default_weight,
        GREEN: __default_weight,
        BLUE: __default_weight,
    }
    __last_color = None

    def __init__(self, player: ABCPlayer):
        self.__player = player
        self.__magazine = []
        self._add_bullet(2)

    def get_bullet(self) -> Bullet:
        self._add_bullet()

        return self.__magazine.pop(0)

    def _add_bullet(self, count=1):
        for i in range(count):
            bullet = Bullet(start_pos=self.__player.vector, color=self.__color)
            self.__magazine.append(bullet)

    @property
    def __color(self) -> pygame.Color:
        color = random.choices(
            self.COLORS,
            weights=list(self.__color_weights.values())
        )[0]

        if self.__last_color == color:
            self.__color_weights[color] -= random.randint(1, 5)
        else:
            self.__color_weights = {
                color_name: self.__default_weight
                for color_name in self.COLORS
            }

        return self.PALETTE[color]


class GunController(ABCGunController):
    def __init__(self, player: ABCPlayer):
        self.logger = logging.getLogger(__name__)

        self.__player: ABCPlayer = player
        self.fired_bullets = []
        self.magazine = Magazine(self.__player)

    def fire(self, fire_vector):
        bullet = self.magazine.get_bullet()
        bullet.fire(self.__player.mouse)

        self.fired_bullets.append(bullet)

    def update(self):
        for idx, bullet in enumerate(self.fired_bullets):
            bullet.update()

            if (bullet.vector.__x > GAME_SETTINGS["resolution"][0] + 30) \
                    or (bullet.vector.__y > GAME_SETTINGS["resolution"][1] + 30):
                self.fired_bullets.pop(idx)
                del bullet
