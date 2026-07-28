from fastapi import FastAPI
from sqlalchemy import text
from app.api import auth_router,users_router,admin_router
from app.core.config import settings
from app.database.database import engine
from app.core.handlers import register_exception_handlers
from app.middleware.logging import LoggingMiddleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
## API Database Automation Project

A  FastAPI backend featuring:

- JWT Authentication
- Role-Based Access Control
- PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations
- User Management
- RESTful API
""",
    contact={
        "name": "Christina Manga",
        "email": "christinamanga28@gmail.com",
        "url": "https://github.com/tinamanga",
    },
    license_info={
        "name": "MIT License",
    },
)

app.add_middleware(LoggingMiddleware)
register_exception_handlers(app)


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
app.include_router(users_router)
app.include_router(admin_router)