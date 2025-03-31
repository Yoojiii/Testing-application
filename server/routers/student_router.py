from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from server.schemas.user_schemas import Sign_in
from server.database.repositories.student_repository import StudentRepository 

router = APIRouter(tags=["student"])

@router.post('/sign_in')
async def sign_in(data: Sign_in):
    try:
        student_id = await StudentRepository.sign_in(data)
        return {"ok": student_id}
    except HTTPException as e:
        raise HTTPException(status_code=409, detail={"message":str(e)}) from e

@router.get('/students')
async def get_students():
    try:
        students = await StudentRepository.get_students()
        return {"ok": students}
    except HTTPException as e:
        raise HTTPException(status_code=409, detail={"message":str(e)}) from e



