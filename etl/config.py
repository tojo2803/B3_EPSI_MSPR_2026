import os

DATABASE_URL = os.getenv("DATABASE_URL")
LOG_LEVEL = os.getenv("ETL_LOG_LEVEL", "INFO")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")