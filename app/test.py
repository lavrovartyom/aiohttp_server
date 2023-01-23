# @routes.get('/users')
# async def get(request) -> r200[List[schemas.UserOut]]:
#     """
#     Обработчик для получения всеx пользователей
#     :return: json response
#     """
#     users = session.query(User).all()
#     result = [schemas.UserOut.from_orm(user).dict() for user in users]
#     return web.json_response(result, content_type='application/json', status=200)
#
#
# @routes.get('/user/{user_id}')
# async def get_user(request) -> r200[List[schemas.UserOut]]:
#     """ Обработчик для получения пользователя по идентификатору """
#     user = session.query(User).where(User.id == request.match_info['user_id']).one_or_none()
#     if user:
#         result = schemas.UserOut.from_orm(user).dict()
#         return web.json_response(result, content_type='application/json', status=200)
#
#     return web.json_response(text='Пользователь не найден', content_type='application/json', status=200)
#
#
# @routes.post('/create_user')
# async def post(request) -> r201[schemas.UserOut]:
#     """
#     Метод для создания нового пользователя
#     :param user: данные о пользователе
#     :return: json response
#     """
#     print(request.match_info.)
#     # new_user = User(**user.dict())
#     # try:
#     #     with session.begin():
#     #         session.add(new_user)
#     # except IntegrityError:
#     #     return web.json_response('Ошибка! Такой пользователь уже есть!')
#     return web.json_response(text='ok', content_type='application/json', status=201)