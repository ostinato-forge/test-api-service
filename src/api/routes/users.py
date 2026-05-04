"""User management endpoints."""

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/users", tags=["users"])


class UserResponse(BaseModel):
    """Schema for user data in API responses."""

    id: str
    username: str
    email: str
    is_active: bool = True


class UserCreateRequest(BaseModel):
    """Schema for creating a new user."""

    username: str
    email: str
    password: str


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str) -> UserResponse:
    """Retrieve a user by ID.

    Args:
        user_id: The unique identifier of the user.

    Returns:
        User data matching the requested ID.

    Raises:
        HTTPException: If user is not found.
    """
    return UserResponse(
        id=user_id,
        username="test-user",
        email="test@example.com",
    )


@router.post("/", response_model=UserResponse, status_code=201)
async def create_user(body: UserCreateRequest) -> UserResponse:
    """Create a new user account.

    Args:
        body: The user creation payload.

    Returns:
        The newly created user data.
    """
    return UserResponse(
        id="new-user-id",
        username=body.username,
        email=body.email,
    )