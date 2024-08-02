from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import Column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlmodel import JSON, Field, Relationship, SQLModel


class User(SQLModel, AsyncAttrs, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    password: str
    scopes: list[str] = Field(sa_column=Column(JSON))
    disabled: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    tokens: list["Token"] = Relationship(
        back_populates="username", sa_relationship_kwargs={"cascade": ""}
    )


class RefreshToken(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="user.ID", unique=True)
    refresh_token: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    username: User | None = Relationship()


class Token(SQLModel, table=True):
    ID: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] | None = Field(default=None, foreign_key="user.ID")
    token: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    revoked: bool = False
    username: User | None = Relationship(back_populates="tokens")


class TokenData(SQLModel):
    username: Optional[str] = None
    scopes: list[str] = []
    exp: int


class UserName(SQLModel):
    username: str


class UserInput(SQLModel):
    username: str
    password: str = Field(max_length=256, min_length=6)
    scopes: list[str] = ["APIUser:Read"]
    disabled: bool = False


class UserResponse(SQLModel):
    username: str
    disabled: bool
    created_at: datetime
    scopes: list[str]


class RegistrationUserResponse(SQLModel):
    message: str
    data: UserResponse


class AccessTokenInfo(SQLModel):
    token_type: str
    access_token: str
    expires_in: int


class RefreshTokenInfo(SQLModel):
    token: str
    expires_in: int


class LoginResponse(SQLModel):
    message: str
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: RefreshTokenInfo
    scopes: list[str]
    status: int


class RefreshResponse(SQLModel):
    access_token: AccessTokenInfo
    refresh_token: RefreshTokenInfo
    status: int


class PassReset(SQLModel):
    username: str
    new_password: str = Field(max_length=256, min_length=6)


class MessageStatus(SQLModel):
    message: str
    status: int


class UserScopeChange(SQLModel):
    username: str
    scopes: list[str]
