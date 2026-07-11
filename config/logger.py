from loguru import logger

logger.add(
    "logs/investment_agent.log",
    rotation="10 MB",
    retention="10 days",
    level="INFO"
)

logger.info("Logger Initialized")