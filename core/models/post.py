from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationsMixins


class Post(UserRelationsMixins, Base):
    _user_id_unique = False
    _user_back_population = "posts"

    title: Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default=""
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.title!r}, user_id={self.user_id})"

    def __repr__(self):
        return str(self)
