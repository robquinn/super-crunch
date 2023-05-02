from dotenv import load_dotenv

from .log import setup_custom_logger

load_dotenv()

logger = setup_custom_logger("root")
