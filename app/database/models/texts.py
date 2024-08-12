from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


class TextModel(BaseModel):
    __tablename__ = "texts"

    id_: Mapped[int] = mapped_column(BigInteger, default=1, primary_key=True)

    not_sub_text: Mapped[str]
    manual_text: Mapped[str]
    main_text: Mapped[str]
