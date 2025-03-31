from sqlalchemy.orm import Mapped, mapped_column
from server.database.database import ModelBase


class StudentOrm(ModelBase): 
    __tablename__ = 'student'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    group: Mapped[str]
    score: Mapped[int] = 0