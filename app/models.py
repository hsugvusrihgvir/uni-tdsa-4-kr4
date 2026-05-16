from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import String

# ДЛЯ ЗАДАНИЯ 9
class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(default=0.0, nullable=False)
    count: Mapped[int] = mapped_column(default=0, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)


