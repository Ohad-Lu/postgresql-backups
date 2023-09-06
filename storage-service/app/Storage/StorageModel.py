from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class Storage(Base):
    __tablename__ = "storages"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    type: Mapped[str] = mapped_column(String(30))

    aws_bucket_name: Mapped[str] = mapped_column(String(30))
    aws_secret_access_id: Mapped[str] = mapped_column(String(50))
    aws_access_key_id: Mapped[str] = mapped_column(String(50))
