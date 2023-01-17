from typing import List

from fastapi import FastAPI
from sqlalchemy.future import select

from db import session
from models import User
import schemas

app = FastAPI()


@app.get('/', response_model=List[schemas.UserOut])
async def get_all_user() -> List[User]:
	""" Получение всех пользователей """
	res = session.execute(select(User))
	return res.scalars().all()


@app.post('/', response_model=schemas.UserOut)
async def create_user(user: schemas.UserIn):
	""" Добавление нового пользователя """
	new_user = User(**user.dict())
	with session.begin():
		session.add(new_user)
	return new_user



