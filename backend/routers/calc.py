from fastapi import APIRouter, HTTPException, Query
from backend.storage import get_menu_data
from backend.calculator import calculate
from backend.models.schemas import CalcRequest
import uuid
import json
from pathlib import Path

router = APIRouter()

RESULTS_FILE = Path(__file__).parent.parent.parent / "storage" / "results.json"


def _load_results() -> dict:
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if RESULTS_FILE.exists():
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_results(data: dict):
    RESULTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


results_store: dict[str, dict] = _load_results()


@router.post("/calc")
def calc_from_body(body: CalcRequest):
    menu_data = get_menu_data(body.menu_id)
    if menu_data is None:
        raise HTTPException(status_code=404, detail="Меню не найдено")

    try:
        result = calculate(menu_data, body.groups, body.days, body.start_day)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    token = uuid.uuid4().hex[:12]
    result.token = token
    result.menu_id = body.menu_id

    results_store[token] = result.model_dump()
    _save_results(results_store)

    return result.model_dump()


@router.get("/calc")
def calc_legacy(
    menu_id: str = Query(...),
    program: str = Query(...),
    adults: int = Query(1, ge=1),
    children: int = Query(0, ge=0),
    days: int = Query(7, ge=1, le=7),
    start_day: int = Query(1, ge=1, le=7),
):
    menu_data = get_menu_data(menu_id)
    if menu_data is None:
        raise HTTPException(status_code=404, detail="Меню не найдено")

    try:
        from backend.models.schemas import PersonGroup
        groups = [PersonGroup(program=program, adults=adults, children=children)]
        result = calculate(menu_data, groups, days, start_day)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    token = uuid.uuid4().hex[:12]
    result.token = token
    result.menu_id = menu_id

    results_store[token] = result.model_dump()
    _save_results(results_store)

    return result.model_dump()
