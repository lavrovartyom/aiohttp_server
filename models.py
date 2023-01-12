from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
import psycopg2
from sqlalchemy.orm import sessionmaker, relationship
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


class User(Base):
	""" Модель пользователя  """
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	first_name = Column(String(50))
	last_name = Column(String(50))
	login = Column(String(50), unique=True)
	password = Column(String(500), nullable=False)
	date_of_birth = Column(Date)
	permission = Column(Integer, ForeignKey('permission.id'), nullable=False)
	relation_permission = relationship('Permission')

	def __repr__(self):
		return f'{self.id}, {self.first_name}, {self.last_name}'


class Permission(Base):
	""" Модель права """
	__tablename__ = 'permission'

	id = Column(Integer, primary_key=True)
	permission = Column(String(25), unique=True)

	def __repr__(self):
		return f'{self.permission}'
