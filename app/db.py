from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from environs import Env

env = Env()
env.read_env()


SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg2://{env.str("DB_USER")}:{env.str("DB_PASSWORD")}@{env.str("PGHOST")}:{env.str("PGPORT")}/{env.str("DB_NAME")}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base(bind=engine)
