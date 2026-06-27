from fastapi import APIRouter

from app.shared.response import success_response

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
async def health_check():
    return success_response(
        message="Health check successful",
        data={
            "status": "healthy",
            "service": "TenderIQ AI",
            "version": "1.0.0",
        },
    )