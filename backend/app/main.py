from fastapi import FastAPI
from .db.session import init_db

app = FastAPI(title="Jezweb AI App")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/api/health")
def health_check():
    return {"status": "ok"}
