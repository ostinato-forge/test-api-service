"""Test API Service - FastAPI application entry point."""

from fastapi import FastAPI

app = FastAPI(
    title="Test API Service",
    description="Minimal API backend for Jurati integration testing",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint returning service info."""
    return {"service": "test-api-service", "status": "ok"}