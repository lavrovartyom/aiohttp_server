from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


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
		return f'{self.id}, {self.first_name}, {self.last_name}, {self.login}, {self.date_of_birth}, {self.permission}'

	def to_json(self):
		return {user.name: getattr(self, user.name) for user in self.__table__.columns}


class Permission(Base):
	""" Модель права """
	__tablename__ = 'permission'

	id = Column(Integer, primary_key=True)
	permission = Column(String(25), unique=True)

	def __repr__(self):
		return f'{self.permission}'
