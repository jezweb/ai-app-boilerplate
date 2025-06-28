import os
from sqlmodel import create_engine, SQLModel

# Use an environment variable for the database URL, with a default
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/database.db")

# The connect_args are specific to SQLite.
# They are not needed for other databases like PostgreSQL.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db():
    # This will create the database file and tables if they don't exist
    SQLModel.metadata.create_all(engine)
