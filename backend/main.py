from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

app = FastAPI(title="Калькулятор рационов API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from backend.routers import menu, calc, admin, pdf_gen, share, orders

app.include_router(menu.router, prefix="/api", tags=["menu"])
app.include_router(calc.router, prefix="/api", tags=["calc"])
app.include_router(admin.router, prefix="/api", tags=["admin"])
app.include_router(pdf_gen.router, prefix="/api", tags=["pdf"])
app.include_router(share.router, prefix="/api", tags=["share"])
app.include_router(orders.router, prefix="/api", tags=["orders"])


@app.get("/api/health")
def health():
    return {"status": "ok"}
