from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User


class UserRelationsMixins:
    _user_id_unique: bool = True
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("user.id"), unique=cls._user_id_unique)

    @declared_attr
    def user(cls) -> Mapped[int]:
        return relationship(
            "user",
            back_populates=cls._user_back_populates)
