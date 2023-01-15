from pydantic import BaseModel
from datetime import date


class BaseUser(BaseModel):
	first_name: str
	last_name: str
	login: str
	date_of_birth: date
	permission: int


class UserIn(BaseUser):
	password: str


class UserOut(BaseUser):
	id: int

	class Config:
		orm_mode = True
