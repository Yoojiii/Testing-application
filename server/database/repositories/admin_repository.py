from server.schemas.user_schemas import Sign_in
from server.database.models.student_models import StudentOrm
from server.database.database import new_session
from server.database.repositories.student_repository import StudentRepository
from sqlalchemy import select

class AdminRepository():
    @classmethod
    async def get_online(self) -> int:
        count = len(await StudentRepository.get_students())
        return count
