from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
	""" Модель пользователя  """
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True, autoincrement=True)
	first_name = Column(String(50))
	last_name = Column(String(50))
	login = Column(String(50), unique=True)
	password = Column(String(500), nullable=False)
	date_of_birth = Column(Date)
	permission = Column(String, ForeignKey('permission.permission'), nullable=False)
	permission_table = relationship('Permission', back_populates='user_table')

	def __repr__(self):
		return f'{self.id}, {self.first_name}, {self.last_name}, {self.login}, {self.date_of_birth}, {self.permission}'


class Permission(Base):
	""" Модель права """
	__tablename__ = 'permission'

	id = Column(Integer, primary_key=True)
	permission = Column(String(25), unique=True, nullable=False)
	user_table = relationship("User", back_populates="permission_table", cascade="all, delete-orphan")

	def __repr__(self):
		return f'{self.permission}'
