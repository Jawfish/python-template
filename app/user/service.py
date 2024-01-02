from cattrs import unstructure
from litestar.exceptions.http_exceptions import NotFoundException
from sqlalchemy.ext.asyncio.session import AsyncSession

from .repository import UserRepository
from .schemas import AllUsersOut, UserOut


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def create_user(self, user_name: str) -> UserOut:
        user = await self.repository.create(user_name)
        return unstructure(user, UserOut)

    async def get_user(self, uuid: str) -> UserOut:
        user = await self.repository.get(uuid)
        if not user:
            raise NotFoundException(detail='User not found')
        return unstructure(user, UserOut)

    async def get_all_users(self) -> AllUsersOut:
        response = await self.repository.get_all()
        users = [unstructure(user, UserOut) for user in response]
        return AllUsersOut(users)


def get_user_service(session: AsyncSession) -> UserService:
    return UserService(UserRepository(session))
