from fastapi import APIRouter, Depends

from app.auth.dependencies import get_current_admin

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.get("/dashboard")
def admin_dashboard(
    current_user=Depends(get_current_admin),
):
    return {
        "message": f"Welcome {current_user.first_name}",
        "role": current_user.role,
    }