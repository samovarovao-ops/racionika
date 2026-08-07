import os
import uuid
import shutil
import json
import time
from pathlib import Path
from backend.menu_parser import parse_menu, MenuData

STORAGE_DIR = Path(__file__).parent.parent / "storage"
MENU_DIR = STORAGE_DIR / "menus"
VERSIONS_FILE = STORAGE_DIR / "versions.json"
ORDERS_FILE = STORAGE_DIR / "orders.json"

MAX_VERSIONS = 3


def _ensure_dirs():
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    MENU_DIR.mkdir(parents=True, exist_ok=True)


def _load_versions() -> dict:
    _ensure_dirs()
    if VERSIONS_FILE.exists():
        with open(VERSIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def _save_versions(data: dict):
    _ensure_dirs()
    with open(VERSIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_menu(file_content: bytes, filename: str) -> dict:
    _ensure_dirs()
    menu_id = uuid.uuid4().hex[:12]
    versions = _load_versions()

    versions_list = versions.get("versions", [])
    version_num = len(versions_list) + 1

    dest = MENU_DIR / f"{menu_id}_v{version_num}.xlsx"
    with open(dest, "wb") as f:
        f.write(file_content)

    result = parse_menu(str(dest))
    errors = [e.to_dict() for e in result.errors]
    warnings = result.warnings

    version_info = {
        "menu_id": menu_id,
        "version": version_num,
        "filename": filename,
        "file_path": str(dest),
        "row_count": len(result.menu_items),
        "errors": errors,
        "warnings": warnings,
        "timestamp": time.time(),
    }

    versions_list.append(version_info)

    if len(versions_list) > MAX_VERSIONS:
        removed = versions_list[:len(versions_list) - MAX_VERSIONS]
        versions_list = versions_list[len(versions_list) - MAX_VERSIONS:]
        for v in removed:
            p = Path(v["file_path"])
            if p.exists():
                p.unlink()

    versions["versions"] = versions_list
    versions["latest_id"] = menu_id
    _save_versions(versions)

    return {
        "menu_id": menu_id,
        "version": version_num,
        "row_count": len(result.menu_items),
        "errors": errors,
        "warnings": warnings,
    }


def get_menu_data(menu_id: str) -> MenuData | None:
    versions = _load_versions()
    for v in reversed(versions.get("versions", [])):
        if v["menu_id"] == menu_id:
            file_path = v["file_path"]
            if os.path.exists(file_path):
                return parse_menu(file_path)
    return None


def get_menu_file_path(menu_id: str) -> str | None:
    versions = _load_versions()
    for v in reversed(versions.get("versions", [])):
        if v["menu_id"] == menu_id:
            if os.path.exists(v["file_path"]):
                return v["file_path"]
    return None


def get_versions() -> list[dict]:
    versions = _load_versions()
    result = []
    for v in versions.get("versions", []):
        result.append({
            "menu_id": v["menu_id"],
            "version": v["version"],
            "filename": v["filename"],
            "row_count": v["row_count"],
            "errors": v["errors"],
            "timestamp": v["timestamp"],
        })
    return result


def rollback_to(menu_id: str) -> bool:
    versions = _load_versions()
    versions_list = versions.get("versions", [])
    for i, v in enumerate(versions_list):
        if v["menu_id"] == menu_id:
            versions["versions"] = versions_list[i:]
            versions["latest_id"] = menu_id
            _save_versions(versions)
            return True
    return False


def list_all_menus() -> list[dict]:
    versions = _load_versions()
    result = []
    for v in versions.get("versions", []):
        md = parse_menu(v["file_path"]) if os.path.exists(v["file_path"]) else None
        result.append({
            "menu_id": v["menu_id"],
            "version": v["version"],
            "filename": v["filename"],
            "row_count": v["row_count"],
            "items": len(md.menu_items) if md else 0,
            "tariffs": len(md.tariffs) if md else 0,
            "settings": md.settings if md else {},
            "errors": v["errors"],
            "timestamp": v["timestamp"],
        })
    return result


ORDERS_FILE = STORAGE_DIR / "orders.json"


def _load_orders() -> list[dict]:
    _ensure_dirs()
    if ORDERS_FILE.exists():
        with open(ORDERS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_orders(data: list[dict]):
    _ensure_dirs()
    with open(ORDERS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def create_order(menu_id: str, groups: list[dict], days: int, start_day: int,
                 user_id: int = 0, user_name: str = "", source: str = "web") -> dict:
    orders = _load_orders()
    order_id = uuid.uuid4().hex[:10]
    order = {
        "order_id": order_id,
        "menu_id": menu_id,
        "groups": groups,
        "days": days,
        "start_day": start_day,
        "user_id": user_id,
        "user_name": user_name,
        "source": source,
        "status": "pending",
        "created_at": time.time(),
    }
    orders.append(order)
    _save_orders(orders)
    return order


def get_orders() -> list[dict]:
    return _load_orders()


def get_order(order_id: str) -> dict | None:
    for o in _load_orders():
        if o["order_id"] == order_id:
            return o
    return None


def update_order_status(order_id: str, status: str) -> dict | None:
    orders = _load_orders()
    for o in orders:
        if o["order_id"] == order_id:
            o["status"] = status
            _save_orders(orders)
            return o
    return None


def get_user_orders(user_id: int) -> list[dict]:
    return [o for o in _load_orders() if o.get("user_id") == user_id]
