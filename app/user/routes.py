from litestar import Router, get, post
from litestar.di import Provide

from app.db.session import get_session

from .repository import get_user_repository
from .schemas import AllUsersOut, UserOut
from .service import UserService, get_user_service


@post('/create-user')
async def create_user(
    user_name: str,
    service: UserService,
) -> UserOut:
    return await service.create_user(user_name)


@get('/get-user')
async def get_user(
    uuid: str,
    service: UserService,
) -> UserOut:
    return await service.get_user(uuid)


@get('/get-users')
async def get_users(
    service: UserService,
) -> AllUsersOut:
    return await service.get_all_users()


user_router = Router(
    path='/user',
    route_handlers=[get_user, get_users, create_user],
    dependencies={
        'session': Provide(get_session),
        'service': Provide(get_user_service, sync_to_thread=False),
        'repository': Provide(get_user_repository, sync_to_thread=False),
    },
)
