import os

from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel, Session
from config import Config

DATABASE_URL = (
    f"postgresql://{Config.USER_BD}:{Config.PASS_BD}@{Config.DB_CONTAINER_NAME}:{Config.PORT_BD}/{Config.NAME_BD}"
    # f"postgresql://{Config.USER_BD}:{Config.PASS_BD}@{Config.HOST_BD}:{Config.PORT_BD}/{Config.NAME_BD}"
)

engine = create_engine(DATABASE_URL, echo=True)

session = sessionmaker(engine, expire_on_commit=False, class_=Session)


def get_db() -> sessionmaker:
    return session()