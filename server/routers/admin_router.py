from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from server.database.repositories.admin_repository import AdminRepository 

router = APIRouter(tags=["admin"])


@router.get('/admin/stats')
async def get_students():
    try:
        count = await AdminRepository.get_online()
        return {"ok": count}
    except HTTPException as e:
        raise HTTPException(status_code=409, detail={"message":str(e)}) from e



