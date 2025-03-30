from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine('sqlite+aiosqlite:///questions.db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

class ModelBase(DeclarativeBase):
    pass

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.create_all)

async def delete_table():
    async with engine.begin() as conn:
        await conn.run_sync(ModelBase.metadata.drop_all)
