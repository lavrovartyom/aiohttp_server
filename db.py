from sqlalchemy import create_engine
import psycopg2
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from environs import Env

env = Env()
env.read_env()


SQLALCHEMY_DATABASE_URL = env.str('SQLALCHEMY_DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
connection = psycopg2.connect(user=env.str('USER'), password=env.str('PASSWORD'))
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base(bind=engine)
