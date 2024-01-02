from sqlalchemy import Column, String

from app.db.session import Base


class User(Base):
    __tablename__ = 'users'
    uuid = Column(String, primary_key=True)
    user_name = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f'<User(name={self.user_name})>'
