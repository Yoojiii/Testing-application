from database.schemas.user_schemas import Sign_in
class UserRepository():

    async def sign_in(self, data: Sign_in):
        async with new_session() as session:
