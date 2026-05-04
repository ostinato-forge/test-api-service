"""Authentication middleware for request validation."""

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from src.api.auth.token import validate_access_token


class AuthMiddleware(BaseHTTPMiddleware):
    """Middleware that validates JWT tokens on protected routes."""

    EXCLUDED_PATHS: set[str] = {"/", "/health", "/docs", "/openapi.json"}

    async def dispatch(self, request: Request, call_next):
        """Process request through auth validation.

        Args:
            request: The incoming HTTP request.
            call_next: The next middleware or route handler.

        Returns:
            Response from the downstream handler.

        Raises:
            HTTPException: If authentication fails on a protected route.
        """
        if request.url.path in self.EXCLUDED_PATHS:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Missing or invalid token")

        token = auth_header.removeprefix("Bearer ")
        try:
            payload = validate_access_token(token)
            request.state.user = payload
        except ValueError as exc:
            raise HTTPException(status_code=401, detail=str(exc)) from exc

        return await call_next(request)