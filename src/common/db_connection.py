
import os
from sqlalchemy import create_engine
from sqlalchemy import text
from dotenv import load_dotenv


class DatabaseConnector:
    def __init__(self):
        dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__),  '..', '..', '.env'))
        load_dotenv(dotenv_path=dotenv_path)
        server = os.getenv("DB_SERVER")
        database = os.getenv("DB_NAME")
        username = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        connection_string = (
            f"postgresql+psycopg2://{username}:{password}@{server}/{database}"
        )
        self.engine = create_engine(connection_string)

    def get_engine(self):
        return self.engine

    def test_connection(self):
        try:
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False
