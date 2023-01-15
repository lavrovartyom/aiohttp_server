from aiohttp.web import run_app, Application
from app.handlers import routes


app = Application()


if __name__ == '__main__':
    app.add_routes(routes)
    run_app(app)