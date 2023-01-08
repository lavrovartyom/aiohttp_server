from sqlalchemy import create_engine, Column, Integer, String, UnicodeText, DateTime
import psycopg2
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('postgresql+psycopg2://root:4322@localhost/db', echo=True, pool_size=6, max_overflow=10, encoding='latin1')
connection = psycopg2.connect(user="postgres", password="4322")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base(bind=engine)


class User(Base):
	""" Модель пользователя  """
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	first_name = Column(String(50))
	last_name = Column(String(50))
	login = Column(String(50))
	password = Column(UnicodeText(50))
	date_of_birth = Column(DateTime)


Base.metadata.create_all()
