import pygame

from app.game.state.player import Player
from app.render.gun import GunRender
from config import RENDER_DEBUG

FROG_RADIUS = 64.0


class PlayerRender:
    def __init__(self, parent_surface: pygame.Surface, player_data: Player):
        self.surface = parent_surface
        self.data = player_data

        self.gun = GunRender(self.surface, self.data.gun)

    def update(self):
        self.__draw_player()
        self.gun.update()

    def __draw_player(self):
        pygame.draw.circle(
            surface=self.surface,
            color=pygame.Color(0, 100, 100),
            center=self.data.vector,
            radius=FROG_RADIUS
        )

