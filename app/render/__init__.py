import logging
import pygame  # type: ignore

from abstarct.app.render import ABCRender
from app.constants import COLOR_RENDER_BG
from app.game.state.bullets import BulletController

from app.game.state.controller import GameStateController
from app.render.player import PlayerRender
from config import RENDER_DEBUG


class BulletsRender:
    def __init__(self, parent_surface: pygame.Surface, data: BulletController):
        self.surface = parent_surface
        self.data = data

    def update(self):
        for bullet in self.data:
            pygame.draw.circle(
                surface=self.surface,
                color=bullet.color,
                center=bullet.position,
                radius=30
            )


class Render(ABCRender):
    def __init__(self, data: GameStateController, width=640, height=640):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Init Render...")

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
        self.bullets = BulletsRender(self.surface, data.bullets)

    def update(self):
        pygame.display.flip()
        self.surface.fill(COLOR_RENDER_BG)

        self.player.update()
        self.bullets.update()
        self.screen.blit(self.surface, (0, 0))

        if RENDER_DEBUG:
            self.draw_debug()

    text_prolonged = ""
    text_cursor = ""

    def draw_cursor(self):
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
        self.screen.blit(self.surface, (0, 0))

    def draw_cursor_text(self):
        self.text_cursor = \
            f"{self.game_data.mouse} " \
            f"({self.game_data.mouse.length():.2f})"
        self.text_prolonged = \
            f"{self.game_data.player.gun.vector} " \
            f"({self.game_data.player.gun.vector.length():.2f})"

        self.screen.blit(
            self.font.render(self.text_cursor, True, (255, 255, 255)),
            pygame.Vector2(self.width - 160, self.height - 40)
        )
        self.screen.blit(
            self.font.render(self.text_prolonged, True, (255, 255, 255)),
            pygame.Vector2(self.width - 160, self.height - 20)
        )

    def draw_debug(self):
        self.draw_cursor()
        self.draw_cursor_text()
