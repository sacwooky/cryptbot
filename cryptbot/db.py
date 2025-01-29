from sqlalchemy import create_engine
import pandas as pd

class DatabaseManager:
    def __init__(self, config: dict):
        self.engine = create_engine(
            f"postgresql+psycopg2://{config['DB']['user']}:{config['DB']['password']}@"
            f"{config['DB']['host']}:{config['DB']['port']}/{config['DB']['dbname']}"
        )

    def save_token_data(self, token_data: dict):
        """Save token data to the database."""
        df = pd.DataFrame([token_data])
        df.to_sql("tokens", self.engine, if_exists="append", index=False)