FROM python:3.11

RUN mkdir /aiohttp_server

COPY app /aiohttp_server/app/
COPY migrations /aiohttp_server/migrations/
COPY requirements.txt /aiohttp_server/
COPY alembic.ini /aiohttp_server/
COPY .env /aiohttp_server/

RUN pip install -r /aiohttp_server/requirements.txt

EXPOSE 80:80

ENTRYPOINT ["python", "aiohttp_server/app/main.py"]


