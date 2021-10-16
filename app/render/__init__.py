import logging
import math

import pygame  # type: ignore

from abstarct.app.render import ABCRender
from app.render.playground import PlayGround
from app.constants import COLOR_RENDER_BG

from app.game.state.controller import GameStateController

FROG_RADIUS = 64.0


class Render(ABCRender):
    def __init__(self, data: GameStateController, width=640, height=640):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Init Render...")

        self.__text_prolonged = ""
        self.__text_ZX = ""
        self.__text_ZM = ""
        self.__text_cos_MCQ = ""
        self.__text_sin_MCQ = ""
        self.__text_MC = ""
        self.__text_MQ = ""
        self.__text_cursor = ""
        self.__text_in_top = ""

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

    def get_prolonged_to_X_vector(self, origin: pygame.Vector2) -> pygame.Vector2:
        in_top_part = origin.x >= 0 and origin.y <= self.height / 2
        self._in_top = in_top_part
        self.__text_in_top = f"{in_top_part}"

        MC = origin.distance_to(self.game_data.player.pos)
        self.__text_MC = f"MC={MC:.2f}"

        MQ = abs(self.width / 2 - origin.x)
        self.__text_MQ = f"MQ={MQ:.2f}"

        sin_MCQ = MQ / MC
        cos_MCQ = math.sqrt(1 - sin_MCQ ** 2)

        self.__text_sin_MCQ = f"sin_MCQ={sin_MCQ:.2f}"
        self.__text_cos_MCQ = f"cos_MCQ={cos_MCQ:.2f}"

        try:
            if in_top_part:
                ZM = origin.y / cos_MCQ
            else:
                ZM = (self.height - origin.y) / cos_MCQ
        except ZeroDivisionError:
            if origin.x <= self.width / 2:
                return pygame.Vector2(0, self.height / 2)
            else:
                return pygame.Vector2(self.width, self.height / 2)
        else:
            self.__text_ZM = f"ZM={ZM:.2f}"

        ZX = ZM * sin_MCQ
        self.__text_ZX = f"ZX={ZX:.2f}"

        if origin.x <= self.width / 2:
            if in_top_part:
                x = origin.x - ZX
                y = 0
            else:
                x = origin.x - ZX
                y = self.height
        else:
            if in_top_part:
                x = origin.x + ZX
                y = 0
            else:
                x = origin.x + ZX
                y = self.height

        return pygame.Vector2(x, y)

    def __draw(self):
        self.__draw_frog()
        self.__draw_aim_line()
        self.__draw_cursor()

        self.screen.blit(self.surface, (0, 0))

        self.screen.blit(self.font.render(self.__text_MC, True, (255, 255, 255)), pygame.Vector2(5, 5))
        self.screen.blit(self.font.render(self.__text_MQ, True, (255, 255, 255)), pygame.Vector2(5, 15))
        self.screen.blit(self.font.render(self.__text_sin_MCQ, True, (255, 255, 255)), pygame.Vector2(5, 25))
        self.screen.blit(self.font.render(self.__text_cos_MCQ, True, (255, 255, 255)), pygame.Vector2(5, 35))
        self.screen.blit(self.font.render(self.__text_ZM, True, (255, 255, 255)), pygame.Vector2(5, 45))
        self.screen.blit(self.font.render(self.__text_ZX, True, (255, 255, 255)), pygame.Vector2(5, 55))
        self.screen.blit(self.font.render(self.__text_in_top, True, (255, 255, 255)), pygame.Vector2(5, 65))

        self.screen.blit(
            self.font.render(self.__text_cursor, True, (255, 255, 255)),
            pygame.Vector2(self.width - 160, self.height - 40)
        )
        self.screen.blit(
            self.font.render(self.__text_prolonged, True, (255, 255, 255)),
            pygame.Vector2(self.width - 160, self.height - 20)
        )

    def __draw_frog(self):
        pygame.draw.circle(
            surface=self.surface,
            color=pygame.Color(0, 100, 100),
            center=self.game_data.player.pos,
            radius=FROG_RADIUS
        )

    def __draw_aim_line(self, verbose=True):
        try:
            prolonged = self.get_prolonged_to_X_vector(self.game_data.mouse)
        except ZeroDivisionError:
            prolonged = self.last_prolonged
        else:
            self.last_prolonged = prolonged
        self.__text_prolonged = f"{prolonged} {prolonged.length():.2f}"

        pygame.draw.line(
            surface=self.surface,
            color=pygame.Color(200, 100, 0),
            start_pos=self.game_data.player.pos,
            end_pos=prolonged
        )

        if verbose:
            # vector Oz
            pygame.draw.line(
                surface=self.surface,
                color=pygame.Color(0, 200, 200),
                start_pos=(0, 0),
                end_pos=prolonged
            )

            # vector OC
            pygame.draw.line(
                surface=self.surface,
                color=pygame.Color(0, 200, 0),
                start_pos=(0, 0),
                end_pos=self.game_data.player.pos
            )
            # vector OM
            pygame.draw.line(
                surface=self.surface,
                color=pygame.Color(0, 200, 0),
                start_pos=(0, 0),
                end_pos=self.game_data.mouse
            )

            # aim line
            pygame.draw.line(
                surface=self.surface,
                color=pygame.Color(200, 0, 0),
                start_pos=self.game_data.player.pos,
                end_pos=self.game_data.mouse
            )

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

        self.__text_cursor = f"{self.game_data.mouse} ({self.game_data.mouse.length():.2f})"

    def update(self):
        pygame.display.flip()
        self.surface.fill(COLOR_RENDER_BG)

        self.__draw()
