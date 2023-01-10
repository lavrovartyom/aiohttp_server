from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
import psycopg2
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('postgresql+psycopg2://postgres:4322@localhost/postgres')
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
	password = Column(String(500), nullable=True)
	date_of_birth = Column(DateTime)
	permission_id = Column(Integer, ForeignKey('permission.id'))
	user_permission = relationship('Permission')

	def __repr__(self):
		return f'{self.id}, {self.first_name}, {self.last_name}'


class Permission(Base):
	""" Модель права """
	__tablename__ = 'permission'

	id = Column(Integer, primary_key=True)
	permission = Column(String(25))

	def __repr__(self):
		return f'{self.permission}'


Base.metadata.create_all()
