from sqlalchemy.orm import Mapped

from core.models.base import Base


class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str]  # mapped is a type hint for the ORM and it used for type checking
    price: Mapped[float]
    description: Mapped[str]
