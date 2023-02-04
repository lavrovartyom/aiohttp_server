# aiohttp server
* http://localhost:8080/login - авторизация по логину и паролю
* http://localhost:8080/logout - выход из учетной записи
* http://localhost:8080/ - получить всех пользователей
* http://localhost:8080/get/{id} - получить информацию о пользователе по id
* http://localhost:8080/create - добавить пользователя
* http://localhost:8080/delete/{id} - удалить пользователя
* http://localhost:8080/update/ - обновить данные о пользователе

Сервер общается только по средствам REST API.  
У пользователя может быть одно из 3-х прав "admin", "reading", "blocking"  
"admin" имеет право на полный CRUD    
"reading" имеет право только читать    
"blocking" заблокирован

# stack
* aiohttp
* asyncio
* PostgreSQL
* SQlAlchemy
* alembic
* pydantic
* Docker, docker-compose

# starting

В файле .env вписать имя и пароль базы данных или оставить их тестовыми

собрать проект:
> docker-compose build

накатить миграции в базу данных и создать дефолтного пользователя: 

> docker-compose run aiohttp-server alembic upgrade head

запуск

> docker-compose up
