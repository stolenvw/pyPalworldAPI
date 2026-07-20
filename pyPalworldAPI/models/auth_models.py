"""SQL table and data verification models for OAuth data."""

from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlmodel import JSON, Field, Relationship, SQLModel


class User(SQLModel, AsyncAttrs, table=True):
    """Represent an authenticated API user."""

    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    username: str = Field(index=True, unique=True)
    password: str
    """Hashed users password."""
    scopes: list[str] = Field(sa_column=Column(JSON))
    disabled: bool = False
    """Marks if users account is disabled or not."""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    """Auto generated datetime of when users account was made."""
    tokens: list["Token"] = Relationship(
        back_populates="username", sa_relationship_kwargs={"cascade": ""}
    )
    """Table relationship to `Token` table"""


class RefreshToken(SQLModel, table=True):
    """Represent a stored refresh token."""

    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    user_id: int | None = Field(default=None, foreign_key="user.ID", unique=True)
    """User id foreign key to `User` table."""
    refresh_token: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    """Auto generated datetime of when users account was made."""
    username: User | None = Relationship()
    """Table relationship to `User` table"""


class Token(SQLModel, table=True):
    """Represent a stored access token."""

    ID: Optional[int] = Field(default=None, primary_key=True)
    """Auto incremented database primary key."""
    user_id: Optional[int] | None = Field(default=None, foreign_key="user.ID")
    """User id foreign key to `User` table."""
    token: str
    """Users access token."""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    """Auto generated datetime of when access token was made."""
    revoked: bool = False
    """Mark if access token has be revoked or not."""
    username: User | None = Relationship(back_populates="tokens")
    """Table relationship to `User` table."""


class TokenData(SQLModel):
    """Represent decoded token payload data."""

    username: Optional[str] = None
    scopes: list[str] = []
    exp: int


class UserName(SQLModel):
    """Represent a username payload."""

    username: str


class UserInput(SQLModel):
    """Represent user registration input."""

    username: str
    password: str = Field(max_length=256, min_length=6)
    """min_length=``6``, max_length=``256``"""
    scopes: list[str] = ["APIUser:Read"]
    """Users scopes default ``['APIUser:Read']``"""
    disabled: bool = False


class UserResponse(SQLModel):
    """Represent public user response data."""

    username: str
    disabled: bool
    created_at: datetime
    scopes: list[str]


class RegistrationUserResponse(SQLModel):
    """Represent a successful user registration response."""

    message: str
    data: UserResponse


class AccessTokenInfo(SQLModel):
    """Represent access token response data."""

    token_type: str
    access_token: str
    expires_in: int


class RefreshTokenInfo(SQLModel):
    """Represent refresh token response data."""

    token: str
    expires_in: int


class LoginResponse(SQLModel):
    """Represent a successful login response."""

    message: str
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: RefreshTokenInfo
    scopes: list[str]
    status: int


class RefreshResponse(SQLModel):
    """Represent a refreshed token response."""

    access_token: AccessTokenInfo
    refresh_token: RefreshTokenInfo
    status: int


class PassReset(SQLModel):
    """Represent a password reset request."""

    username: str
    new_password: str = Field(max_length=256, min_length=6)
    """min_length=``6``, max_length=``256``"""


class MessageStatus(SQLModel):
    """Represent a status message response."""

    message: str
    status: int


class UserScopeChange(SQLModel):
    """Represent a user scope update request."""

    username: str
    scopes: list[str]


class ValidateResponse(SQLModel):
    """Represent token validation response data."""

    username: str
    scopes: list[str]
    expires_in: int
