from sqlalchemy.orm import Mapped

from core.models.base import Base


class Product(Base):
    __tablename__ = 'products'

    name: Mapped[str]
    price: Mapped[float]
    description: Mapped[str]
