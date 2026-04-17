from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# for db always create engine first to connect
SQLALCHEMY_DATABASE_URL = "sqlite:///./mon100.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# second create db session
SessionLocal = sessionmaker(bind= engine, autoflush=False,  autocommit=False)

# third base class
Base = declarative_base()