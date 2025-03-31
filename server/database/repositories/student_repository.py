from server.schemas.user_schemas import Sign_in
from server.database.models.student_models import StudentOrm
from server.database.database import new_session
from server.schemas.user_schemas import Student
from client.constants import ADMIN_GROUP
from sqlalchemy import select

class StudentRepository():
    @classmethod
    async def sign_in(self, data: Sign_in):
        if data.group != ADMIN_GROUP:
            async with new_session() as session:
                student_dict = data.model_dump()
                student = StudentOrm(**student_dict)
                session.add(student)
                await session.flush()
                await session.commit()
                return student.id
    
    @classmethod
    async def get_students(self) -> list[Student]:
        async with new_session() as session:
            query = select(StudentOrm)
            result = await session.execute(query)
            result = result.scalars().all()
            result = [Student.model_validate(student) for student in result]
            return result



