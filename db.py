import os
import pandas as pd
from sqlalchemy import create_engine

class DatabaseManager:
    def __init__(self):
        # Fetch database credentials from environment variables
        dbname = os.getenv("POSTGRES_DB", "dexscreener")
        user = os.getenv("POSTGRES_USER", "postgres")
        password = os.getenv("POSTGRES_PASSWORD", "")
        host = os.getenv("POSTGRES_HOST", "localhost")
        port = os.getenv("POSTGRES_PORT", "5432")

        # Create the SQLAlchemy database engine
        self.engine = create_engine(
            f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
        )

    def save_token_data(self, token_data: dict):
        """Save token data to the database."""
        df = pd.DataFrame([token_data])
        df.to_sql("tokens", self.engine, if_exists="append", index=False)
