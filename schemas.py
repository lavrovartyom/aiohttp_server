from pydantic import BaseModel


class BaseUser(BaseModel):
	first_name: str
	last_name: str
	login: str
	permission: int


class UserIn(BaseUser):
	password: str


class UserOut(BaseUser):
	id: int

	class Config:
		orm_mode = True
