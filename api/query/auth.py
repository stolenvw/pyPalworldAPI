from fastapi_pagination.ext.sqlmodel import paginate
from models.auth_models import RefreshToken, Token, User
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_user(db: AsyncSession, username: str):
    result = await db.exec(select(User).where(User.username == username))
    return result.first()


async def authenticate_user(db: AsyncSession, username: str):
    user = await get_user(db, username)
    return user


async def refresh_token_delete(db: AsyncSession, user_id: str):
    result = await db.exec(select(RefreshToken).where(RefreshToken.user_id == user_id))
    refresh_token_check = result.first()
    return refresh_token_check


async def check_refresh_token(db: AsyncSession, user_name: str):
    result = await db.exec(
        select(RefreshToken).join(User).where(User.username == user_name)
    )
    refresh_token_check = result.first()
    return refresh_token_check


async def store_token(db: AsyncSession, user_id: int, token: str):
    add_token = Token(
        user_id=user_id,
        token=token,
    )
    db.add(add_token)
    await db.commit()
    await db.refresh(add_token)
    return


async def token_valid(db: AsyncSession, token: str) -> bool:
    token_info = await db.exec(select(Token).where(Token.token == token))
    try:
        if token_info.first().revoked:
            return False
        else:
            return True
    except AttributeError:
        return False


async def list_tokens(db: AsyncSession):
    token_list = await db.exec(select(Token))
    return token_list


async def list_users(db: AsyncSession):
    return await paginate(db, select(User))


async def change_password(db: AsyncSession, user: User, new_password: str):
    user_tokens = await db.exec(select(Token).where(Token.user_id == user.ID))
    user.password = new_password
    refresh_token_check = await refresh_token_delete(db, user_id=user.ID)
    if refresh_token_check:
        await db.delete(refresh_token_check)
    db.add(user)
    for token in user_tokens:
        token.revoked = True
        db.add(token)
    await db.commit()
    return


async def delete_user(db: AsyncSession, user: User):
    user_tokens = await db.exec(select(Token).where(Token.user_id == user.ID))
    refresh_token_check = await refresh_token_delete(db, user_id=user.ID)
    if refresh_token_check:
        await db.delete(refresh_token_check)
    await db.delete(user)
    for token in user_tokens:
        token.revoked = True
        db.add(token)
    await db.commit()
    return


async def change_user_status(db: AsyncSession, user: User, disabled: bool):
    user_tokens = await db.exec(select(Token).where(Token.user_id == user.ID))
    refresh_token_check = await refresh_token_delete(db, user_id=user.ID)
    if refresh_token_check:
        await db.delete(refresh_token_check)
    user.disabled = disabled
    db.add(user)
    for token in user_tokens:
        token.revoked = True
        db.add(token)
    await db.commit()
    return


async def delete_old_tokens(db: AsyncSession, tokens: list):
    for token in tokens:
        result = await db.exec(select(Token).where(Token.token == token.token))
        user_tokens = result.first()
        await db.delete(user_tokens)
    await db.commit()
    return


async def change_scope(db: AsyncSession, user: User, new_scope: list):
    user_tokens = await db.exec(select(Token).where(Token.user_id == user.ID))
    user.scopes = new_scope
    db.add(user)
    for token in user_tokens:
        token.revoked = True
        db.add(token)
    await db.commit()
    return


# async def revoke_token(db: AsyncSession, token: str):
#    user_tokens = await db.exec(select(Token).where(Token.token == token))
#    if user_tokens.all():
#        for tok in user_tokens:
#            tok.revoked = True
#            db.add(tok)
#        await db.commit()
#    return user_tokens.first()
