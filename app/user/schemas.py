from attrs import define


@define
class UserIn:
    user_name: str


@define
class UserOut(UserIn):
    uuid: str


@define
class AllUsersOut:
    users: list[UserOut]
