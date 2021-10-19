import pygame

from utils.decorators import as_singleton


class MouseDescriptor:
    def __get__(self, instance, owner):
        try:
            return Mouse().pos
        except pygame.error as e:
            # seems to be a problem with initialization order with ABC
            if "video system not initialized" in e.args:
                return None
            else:
                raise e


@as_singleton
class Mouse:
    def __init__(self):
        self.pos = pygame.Vector2(pygame.mouse.get_pos())

    def update(self):
        self.pos = pygame.Vector2(pygame.mouse.get_pos())
