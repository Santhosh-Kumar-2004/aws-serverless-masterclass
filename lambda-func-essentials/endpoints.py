from fastapi import APIRouter

router = APIRouter(prefix="/data")

@router.get("")
def get_data():
    return {"data": "Data retrieved successfully!"}