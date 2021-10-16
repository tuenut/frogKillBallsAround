import logging

from app.render.frog import FrogRender


class PlayGround:
    def __init__(self, parent_surface, data):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Init PlayGround")

        self.surface = parent_surface
        self.player = FrogRender(self.surface, data)

    def update(self):
        self.player.update()
