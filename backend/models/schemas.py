from pydantic import BaseModel
from typing import Optional


class MenuItem(BaseModel):
    Программа: str
    День: int
    Приём: str
    Блюдо_ID: Optional[str] = None
    Название_блюда: str
    Описание: str
    Порции_на_человека: float
    Цена_за_порцию: float
    Вес_грамм: Optional[float] = None
    Теги: Optional[str] = None


class Tariff(BaseModel):
    Программа: str
    Люди: int
    Цена_за_неделю: float


class Setting(BaseModel):
    Ключ: str
    Значение: str


class MenuVersion(BaseModel):
    menu_id: str
    filename: str
    version: int
    row_count: int
    errors: list[str] = []
    warnings: list[str] = []


class PersonGroup(BaseModel):
    program: str
    adults: int = 0
    children: int = 0


class CalcRequest(BaseModel):
    menu_id: str
    groups: list[PersonGroup]
    days: int = 7
    start_day: int = 1


class DayMeal(BaseModel):
    Приём: str
    блюда: list[dict]


class DayPlan(BaseModel):
    День: int
    приёмы: list[DayMeal]
    дневная_стоимость: float


class GroupResult(BaseModel):
    program: str
    adults: int
    children: int
    people_equiv: float
    computed_price: float
    kit_price: float
    plan: list[DayPlan]


class CalcResult(BaseModel):
    menu_id: str
    groups: list[GroupResult]
    days: int
    start_day: int
    total_computed_price: float
    total_kit_price: float
    total_people: int
    per_person_per_day: float
    per_day_cost: float
    discount_percent: float
    discount_amount: float
    final_price: float
    currency: str
    token: Optional[str] = None
