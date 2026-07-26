from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.admin import router as admin_router


__all__ = [
    "auth_router",
    "users_router",
    "admin_router"
]