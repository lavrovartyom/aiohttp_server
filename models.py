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

	@property
	def serialize(self):
		return {
			'id': self.id,
			'first_name': self.first_name,
			'last_name': self.last_name,
			'login': self.login,
			'date_of_birth': str(self.date_of_birth),
			'permission': self.permission,
		}


class Permission(Base):
	""" Модель права """
	__tablename__ = 'permission'

	id = Column(Integer, primary_key=True)
	permission = Column(String(25), unique=True)

	def __repr__(self):
		return f'{self.permission}'
