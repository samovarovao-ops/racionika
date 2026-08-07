from fastapi import APIRouter, HTTPException
from backend.routers.calc import results_store

router = APIRouter()


@router.get("/share/{token}")
def get_share(token: str):
    if token in results_store:
        return results_store[token]
    raise HTTPException(status_code=404, detail="Результат не найден")
