from utils.logger import configure_logger

from app import main_mode
from utils.start_arguments import parse_arguments

from config import BASE_DIR

if __name__ == "__main__":
    logger = configure_logger()
    logger.debug("Logger initialized.")

    start_opts = parse_arguments()

    logger.debug(f"Start with args <{start_opts}>.")
    logger.debug(f"Base dir: <{BASE_DIR}>.")

    main_mode()