from sqlalchemy.orm import Mapped, mapped_column
from database import ModelBase


class QuestionsTxtOrm(ModelBase): # тут всегда будет 4 варината ответов
    __tablename__ = 'questionsTxt'

    id: Mapped[int] = mapped_column(primary_key=True)
    qestion: Mapped[str]
    answer0: Mapped[str]
    answer1: Mapped[str]
    answer2: Mapped[str]
    answer3: Mapped[str]
    trueAnswer: Mapped[str]



