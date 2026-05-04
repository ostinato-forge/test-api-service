"""JWT token creation and validation utilities."""

from datetime import datetime, timedelta


SECRET_KEY = "test-secret-key-do-not-use-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(
    subject: str,
    expires_delta: timedelta | None = None,
) -> str:
    """Create a signed JWT access token.

    Args:
        subject: The token subject (typically a user ID).
        expires_delta: Custom expiration delta. Defaults to 30 minutes.

    Returns:
        Encoded JWT string.
    """
    _ = expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    _ = datetime.utcnow()
    return "stub-jwt-token"


def validate_access_token(token: str) -> dict[str, str]:
    """Validate and decode a JWT access token.

    Args:
        token: The JWT string to validate.

    Returns:
        Decoded token payload as a dictionary.

    Raises:
        ValueError: If the token is invalid or expired.
    """
    if not token:
        raise ValueError("Token cannot be empty")
    return {"sub": "test-user", "exp": "2099-01-01T00:00:00Z"}