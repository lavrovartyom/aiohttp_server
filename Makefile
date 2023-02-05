run:
	docker-compose run aiohttp-server alembic upgrade head
	docker-compose up
stop:
	docker-compose stop
