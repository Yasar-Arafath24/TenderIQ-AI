from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{message}</cyan>",
)

logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="7 days",
)