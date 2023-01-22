from aiohttp.web import run_app, Application
from app.handlers import routes


app = Application()
app.add_routes(routes)


if __name__ == '__main__':
    run_app(app)
