__all__ = ['Config']

import os


class Config:
    PORT = 8000
    HOST = '0.0.0.0'
    USER_BD = os.getenv('POSTGRES_USER')
    PASS_BD = os.getenv('POSTGRES_PASSWORD')
    HOST_BD = os.getenv('POSTGRES_HOST')
    PORT_BD = os.getenv('POSTGRES_PORT')
    NAME_BD = os.getenv('POSTGRES_DB')
    DB_CONTAINER_NAME = os.getenv('DB_CONTAINER_NAME')
app_settings = Config()