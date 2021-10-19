import pygame

from app.game.state.mouse import MouseDescriptor
from config import RENDER_DEBUG


class GunRender:
    mouse: pygame.Vector2 = MouseDescriptor()

    def __init__(self, parent_surface, gun_data, player_position):
        self.surface = parent_surface
        self.data = gun_data
        self.player_position = player_position

    def update(self):
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 100, 0),
            start_pos=self.player_position,
            end_pos=self.data.vector
        )

        if RENDER_DEBUG:
            self.draw_debug()

    def draw_debug(self):
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
            end_pos=self.player_position
        )
        # vector OM
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 0, 200),
            start_pos=(0, 0),
            end_pos=self.mouse
        )

        # aim line
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 0, 0),
            start_pos=self.player_position,
            end_pos=self.mouse
        )
