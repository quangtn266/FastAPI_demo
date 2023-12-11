import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from sqlalchemy.sql import text
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_retries = 60 * 5
wait_seconds = 1

@retry(
    stop=stop_after_attempt(max_retries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute(text('SELECT 1'))
    except Exception as e:
        logger.error(e)
        raise e

def main() -> None:
    logger.info("Inintializing service")
    init()
    logger.info("Service finished initializing")

if __name__ == "__main__":
    main()