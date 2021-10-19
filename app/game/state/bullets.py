import logging

import pygame


class Bullet:
    def __init__(self, start_pos, vector):
        self.start_pos = self.pos = pygame.Vector2(start_pos)
        self.target_vector = vector

    def update(self):
        # TODO calculate next position from current and target vector
        ...


class BulletController:
    def __init__(self, player_position: pygame.Vector2):
        self.logger = logging.getLogger(__name__)

        self.player_position = player_position
        self.fired_bullets = []

    def fire(self, fire_vector: pygame.Vector2):
        self.logger.debug("FIRE!!!")

        bullet = Bullet(self.player_position, fire_vector)
        self.fired_bullets.append(bullet)

    def update(self):
        for bullet in self.fired_bullets:
            bullet.update()
