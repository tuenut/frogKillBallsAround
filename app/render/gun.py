import pygame

from config import RENDER_DEBUG


class GunRender:
    def __init__(self, parent_surface, data):
        self.surface = parent_surface
        self.data = data

    def update(self):
        if RENDER_DEBUG:
            self.__draw_aim_line()

    def __draw_aim_line(self):
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 100, 0),
            start_pos=self.data.vector,
            end_pos=self.data.vector
        )

        # vector Oz
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(0, 200, 200),
            start_pos=(0, 0),
            end_pos=self.data.vector
        )

        # vector OC
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(0, 200, 0),
            start_pos=(0, 0),
            end_pos=self.data.vector
        )
        # vector OM
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(0, 200, 0),
            start_pos=(0, 0),
            end_pos=self.data.mouse
        )

        # aim line
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 0, 0),
            start_pos=self.data.vector,
            end_pos=self.data.mouse
        )
