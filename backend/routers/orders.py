from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from backend.storage import create_order, get_orders, get_order, update_order_status

router = APIRouter()


class OrderCreate(BaseModel):
    menu_id: str
    groups: list[dict]
    days: int = 7
    start_day: int = 1
    user_id: int = 0
    user_name: str = ""
    source: str = "web"


class OrderStatusUpdate(BaseModel):
    status: str


@router.post("/orders")
def api_create_order(body: OrderCreate):
    order = create_order(
        menu_id=body.menu_id,
        groups=body.groups,
        days=body.days,
        start_day=body.start_day,
        user_id=body.user_id,
        user_name=body.user_name,
        source=body.source,
    )
    return order


@router.get("/orders")
def api_get_orders():
    return get_orders()


@router.get("/orders/{order_id}")
def api_get_order(order_id: str):
    order = get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order


@router.patch("/orders/{order_id}")
def api_update_order(order_id: str, body: OrderStatusUpdate):
    order = update_order_status(order_id, body.status)
    if not order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return order
