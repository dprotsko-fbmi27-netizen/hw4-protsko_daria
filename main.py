import time

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

DB_USER = "my_user"
DB_PASSWORD = "my_password"
DB_HOST = "127.0.0.1"
DB_PORT = "3306"
DB_NAME = "my_database"

DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

MAX_RETRIES = 10
RETRY_DELAY_SECONDS = 10


def get_dataframe() -> pd.DataFrame:
    engine = create_engine(DATABASE_URL)

    last_error: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with engine.connect() as connection:
                # Перевірка, що БД відповідає, перед читанням таблиці.
                connection.execute(text("SELECT 1"))
                return pd.read_sql("SELECT * FROM titanic", connection)
        except SQLAlchemyError as error:
            last_error = error
            print(
                f"Database is not ready yet "
                f"({attempt}/{MAX_RETRIES}). Retrying in {RETRY_DELAY_SECONDS} seconds..."
            )
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY_SECONDS)

    raise RuntimeError("Could not connect to MySQL after all retry attempts.") from last_error


if __name__ == "__main__":
    df = get_dataframe()
    print(df)
    print(f"\nShape: {df.shape[0]} rows x {df.shape[1]} columns")

