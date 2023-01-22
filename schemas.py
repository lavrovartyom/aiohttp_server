from pydantic import BaseModel, validator
from datetime import date


class BaseUser(BaseModel):
	first_name: str
	last_name: str
	login: str
	date_of_birth: date
	permission: int

	@validator('date_of_birth', each_item=True)
	def return_date(cls, date_of_birth):
		return str(date_of_birth)

	class Config:
		orm_mode = True


class UserIn(BaseUser):
	password: str


class UserOut(BaseUser):
	id: int
