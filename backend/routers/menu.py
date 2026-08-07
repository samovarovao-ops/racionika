from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.storage import save_menu, get_versions, rollback_to, list_all_menus
import os

router = APIRouter()

MAX_SIZE_MB = 5


@router.get("/latest-menu")
def latest_menu():
    versions = get_versions()
    if not versions:
        raise HTTPException(status_code=404, detail="Нет загруженных меню")
    latest = versions[-1]
    return {"menu_id": latest["menu_id"], "version": latest["version"]}


@router.post("/upload-menu")
async def upload_menu(file: UploadFile = File(...)):
    if not file.filename.endswith(".xlsx"):
        raise HTTPException(status_code=400, detail="Файл должен быть формата .xlsx")

    content = await file.read()
    size_mb = len(content) / (1024 * 1024)
    if size_mb > MAX_SIZE_MB:
        raise HTTPException(status_code=400, detail=f"Размер файла превышает {MAX_SIZE_MB} МБ")

    result = save_menu(content, file.filename)

    if result["errors"]:
        return {
            "status": "warnings",
            "menu_id": result["menu_id"],
            "version": result["version"],
            "row_count": result["row_count"],
            "errors": result["errors"],
            "warnings": result["warnings"],
        }

    return {
        "status": "ok",
        "menu_id": result["menu_id"],
        "version": result["version"],
        "row_count": result["row_count"],
        "errors": [],
        "warnings": result["warnings"],
    }


@router.get("/menu/{menu_id}/meta")
def menu_meta(menu_id: str):
    versions = get_versions()
    for v in reversed(versions):
        if v["menu_id"] == menu_id:
            return v
    raise HTTPException(status_code=404, detail="Меню не найдено")


@router.get("/menus")
def list_menus():
    return list_all_menus()


@router.post("/menu/{menu_id}/rollback")
def rollback(menu_id: str):
    if rollback_to(menu_id):
        return {"status": "ok", "menu_id": menu_id}
    raise HTTPException(status_code=404, detail="Меню не найдено")
