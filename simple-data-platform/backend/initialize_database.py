import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from .schema import Base

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables.")


engine = create_engine(
    DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)


def initialize_database():
    Base.metadata.create_all(engine)
    print("Tables created successfully!")


# Create tables
if __name__ == "__main__":
    initialize_database()
