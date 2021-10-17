import pygame

from utils.decorators import as_singleton


class MouseDescriptor:
    def __get__(self, instance, owner):
        return Mouse().pos


@as_singleton
class Mouse:
    def __init__(self):
        self.pos = pygame.Vector2(pygame.mouse.get_pos())

    def update(self):
        self.pos = pygame.Vector2(pygame.mouse.get_pos())
