from uuid import uuid4

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from .model import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._db = session

    async def create(self, user_name: str) -> User:
        uuid = str(uuid4())
        user = User(uuid=uuid, user_name=user_name)

        async with self._db as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)

        return user

    async def get(self, uuid: str) -> User | None:
        try:
            async with self._db as session:
                return await session.get(User, uuid)
        except NoResultFound:
            return None

    async def get_all(self) -> list[User]:
        async with self._db as session:
            users = await session.execute(select(User))
            return list(users.scalars().all())


def get_user_repository(session: AsyncSession) -> UserRepository:
    return UserRepository(session)
