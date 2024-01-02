from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from litestar import Litestar

from app.db.session import sessionmanager
from app.user.routes import user_router

from .config import Config


# # https://docs.litestar.dev/2/usage/applications.html#lifespan-context-managers
@asynccontextmanager
async def db_session(
    app: Litestar,
) -> AsyncGenerator[None, None]:
    load_dotenv()
    config = Config()
    sessionmanager.init(config)

    async with sessionmanager.connect() as connection:
        await sessionmanager.create_all(connection)

    try:
        yield
    finally:
        await sessionmanager.close()


app = Litestar(
    lifespan=[db_session],
    route_handlers=[user_router],
)
