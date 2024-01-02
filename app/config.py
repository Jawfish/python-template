import os

from attrs import define, field


@define
class Config:
    DB_USER: str = field(factory=lambda: os.environ.get('DB_USER', 'postgres'))
    DB_PASS: str = field(factory=lambda: os.environ.get('DB_PASS', 'postgres'))
    DB_HOST: str = field(factory=lambda: os.environ.get('DB_HOST', 'localhost'))
    DB_PORT: int = field(factory=lambda: int(os.environ.get('DB_PORT', '5432')))
    DB_NAME: str = field(factory=lambda: os.environ.get('DB_NAME', 'postgres'))

    @property
    def db_url(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
