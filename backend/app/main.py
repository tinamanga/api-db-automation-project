from fastapi import FastAPI
from sqlalchemy import text
from app.api import auth_router
from app.core.config import settings
from app.database.database import engine

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


@app.get("/db-health")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "database": "connected",
            "status": "healthy",
        }

    except Exception as error:
        return {
            "database": "disconnected",
            "error": str(error),
        }
        
app.include_router(auth_router)