from sqlalchemy.orm import Mapped, mapped_column
from database import ModelBase

class ExamStatus(ModelBase):
    __tablename__ = 'exam_status'
    id: Mapped[int] = mapped_column(primary_key=True) 
    is_started: Mapped[bool] = mapped_column(default=False)
