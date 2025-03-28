from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationsMixins


class Profile(UserRelationsMixins, Base):
    _user_id_unique: bool = True
    _user_back_population: str = "profile"

    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    bio: Mapped[str | None]
