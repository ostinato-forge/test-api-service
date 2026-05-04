"""Tests for authentication module."""

from src.api.auth.token import create_access_token, validate_access_token


def test_create_access_token_returns_string() -> None:
    """Token creation should return a non-empty string."""
    token = create_access_token(subject="user-123")
    assert isinstance(token, str)
    assert len(token) > 0


def test_validate_access_token_returns_payload() -> None:
    """Token validation should return a dict with sub claim."""
    payload = validate_access_token("stub-jwt-token")
    assert "sub" in payload


def test_validate_empty_token_raises() -> None:
    """Validating an empty token should raise ValueError."""
    try:
        validate_access_token("")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass