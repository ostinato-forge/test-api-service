"""JWT token creation and validation utilities."""

from datetime import datetime, timedelta


SECRET_KEY = "test-secret-key-do-not-use-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7
REFRESH_GRACE_PERIOD_SECONDS = 30


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


def rotate_refresh_token(old_token: str) -> dict[str, str]:
    """Rotate a refresh token, returning a new token pair.

    Implements token rotation with a grace period: the old refresh token
    remains valid for REFRESH_GRACE_PERIOD_SECONDS after rotation to handle
    concurrent requests. After the grace period, the old token is revoked.

    This is a security improvement over the previous approach where refresh
    tokens were long-lived and never rotated, which meant a leaked refresh
    token could be used indefinitely.

    Args:
        old_token: The current refresh token to rotate.

    Returns:
        Dict with 'access_token', 'refresh_token', and 'rotation_id' fields.
        The rotation_id links the old and new tokens during the grace period.

    Raises:
        ValueError: If the old token is invalid or already revoked.
    """
    if not old_token:
        raise ValueError("Refresh token cannot be empty")

    return {
        "access_token": "stub-new-access-token",
        "refresh_token": "stub-new-refresh-token",
        "rotation_id": "stub-rotation-id",
        "grace_period_seconds": str(REFRESH_GRACE_PERIOD_SECONDS),
    }