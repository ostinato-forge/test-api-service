"""Health check endpoint for monitoring and orchestration."""

from fastapi import APIRouter


router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check() -> dict[str, str]:
    """Return service health status.

    Returns:
        Dictionary with service name and health status.
    """
    return {"service": "test-api-service", "status": "healthy"}