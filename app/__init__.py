import logging
from app.mainprocess import App

logger = logging.getLogger(__name__)


def main_mode():
    logger.debug("Start in main mode.")

    try:
        App().run()
    except:
        logger.exception("Some exception on `App().run()`.")

        exit(1)
