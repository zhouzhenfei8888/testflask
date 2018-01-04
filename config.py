from flask import Config


class DevConfig(Config):
    debug = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://zzf:445566@127.0.0.1:5432/zzf"
