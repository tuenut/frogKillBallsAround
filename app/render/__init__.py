import logging

import pygame  # type: ignore

from abstarct.app.render import ABCRender
from app.game.state.player import Player
from app.render.playground import PlayGround
from app.constants import COLOR_RENDER_BG

from app.game.state.controller import GameStateController

FROG_RADIUS = 64.0


class PlayerRender:
    def __init__(self, parent_surface: pygame.Surface, player_data: Player):
        self.surface = parent_surface
        self.data = player_data

    def update(self):
        self.__draw_player()
        self.__draw_aim_line()

    def __draw_player(self):
        pygame.draw.circle(
            surface=self.surface,
            color=pygame.Color(0, 100, 100),
            center=self.data.vector,
            radius=FROG_RADIUS
        )

    def __draw_aim_line(self, verbose=True):
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 100, 0),
            start_pos=self.data.vector,
            end_pos=self.data.gun.vector
        )

        if verbose:
            # vector Oz
            pygame.draw.line(
                surface=self.surface,
                color=pygame.Color(0, 200, 200),
                start_pos=(0, 0),
                end_pos=self.data.gun.vector
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


class Render(ABCRender):
    def __init__(self, data: GameStateController, width=640, height=640):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Init Render...")

        self.__text_prolonged = ""
        self.__text_cursor = ""

        self.game_data = data

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode(
            (self.width, self.height),
            pygame.DOUBLEBUF
        )

        self.surface = pygame.Surface(self.screen.get_size()).convert()
        self.surface.fill(COLOR_RENDER_BG)
        self.font = pygame.font.SysFont('mono', 12, bold=True)

        self.player = PlayerRender(self.surface, self.game_data.player)

    def __draw(self):
        self.__draw_cursor()

        self.screen.blit(self.surface, (0, 0))

        self.__draw_cursor_text()

    def __draw_cursor(self):
        # y pos
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 200, 200),
            start_pos=(self.game_data.mouse.x, 640),
            end_pos=(self.game_data.mouse.x, 0)
        )
        # x pos
        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 200, 200),
            start_pos=(640, self.game_data.mouse.y),
            end_pos=(0, self.game_data.mouse.y)
        )

    def __draw_cursor_text(self):
        self.__text_cursor = \
            f"{self.game_data.mouse} " \
            f"({self.game_data.mouse.length():.2f})"
        self.__text_prolonged = \
            f"{self.game_data.player.gun.vector} " \
            f"({self.game_data.player.gun.vector.length():.2f})"

        self.screen.blit(
            self.font.render(self.__text_cursor, True, (255, 255, 255)),
            pygame.Vector2(self.width - 160, self.height - 40)
        )
        self.screen.blit(
            self.font.render(self.__text_prolonged, True, (255, 255, 255)),
            pygame.Vector2(self.width - 160, self.height - 20)
        )

    def update(self):
        pygame.display.flip()
        self.surface.fill(COLOR_RENDER_BG)

        self.player.update()
        self.__draw()
