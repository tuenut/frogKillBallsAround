import pygame

FROG_RADIUS = 64.0


class PlayerRender:
    def __init__(self, parent_surface: pygame.Surface, player_vector: pygame.Vector2):
        self.surface = parent_surface
        self.vector = player_vector

    def update(self):
        self.__draw_player()

    def __draw_player(self):
        pygame.draw.circle(
            surface=self.surface,
            color=pygame.Color(0, 100, 100),
            center=self.vector,
            radius=FROG_RADIUS
        )
