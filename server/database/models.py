from sqlalchemy.orm import Mapped, mapped_column
from database import ModelBase

class QuestionsTxtOrm(ModelBase):
    __tablename__ = 'questionsTxt'

    id: Mapped[int] = mapped_column(primary_key=True)
    qestion: Mapped[str]



