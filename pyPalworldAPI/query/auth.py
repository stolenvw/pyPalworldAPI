"""
Auth SQL querys

"""

from fastapi_pagination.ext.sqlmodel import paginate
from models.auth_models import RefreshToken, Token, User
from sqlalchemy.engine.result import ScalarResult
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession


async def get_user(db: AsyncSession, username: str) -> User | None:
    """
    Gets username info from the :py:class:`~pyPalworldAPI.models.auth_models.User` SQL table.

    Parameters
    ----------
    username : str
        Username to lookup.

    Returns
    -------
    User : object or None
        Users info from SQL table

    """
    result = await db.exec(select(User).where(User.username == username))
    return result.first()


async def refresh_token_delete(db: AsyncSession, user_id: int) -> RefreshToken | None:
    """
    Gets refresh token info from the :py:class:`~pyPalworldAPI.models.auth_models.RefreshToken` SQL table by `user_id`.

    Parameters
    ----------
    user_id : int
        User id to lookup.

    Returns
    -------
    RefreshToken : object or None
        Users refreshtoken from SQL table

    """
    result = await db.exec(select(RefreshToken).where(RefreshToken.user_id == user_id))
    refresh_token_check = result.first()
    return refresh_token_check


async def check_refresh_token(db: AsyncSession, user_name: str) -> RefreshToken | None:
    """
    Gets refresh token info from the :py:class:`~pyPalworldAPI.models.auth_models.RefreshToken` SQL table by `username`.

    Parameters
    ----------
    username : str
        Username to lookup.

    Returns
    -------
    RefreshToken : object or None
        Users refreshtoken from SQL table

    """
    result = await db.exec(
        select(RefreshToken).join(User).where(User.username == user_name)
    )
    refresh_token_check = result.first()
    return refresh_token_check


async def store_token(db: AsyncSession, user_id: int, token: str) -> None:
    """
    Stores access token in the :py:class:`~pyPalworldAPI.models.auth_models.Token` SQL table.

    Parameters
    ----------
    user_id : int
        User id to store access token for.
    token : str
        Access token.

    Returns
    -------
    None

    """
    add_token = Token(
        user_id=user_id,
        token=token,
    )
    db.add(add_token)
    await db.commit()
    await db.refresh(add_token)
    return


async def token_valid(db: AsyncSession, token: str) -> bool:
    """
    Checks if access token in the :py:class:`~pyPalworldAPI.models.auth_models.Token` SQL table is revoked.

    Parameters
    ----------
    token : str
        Access token to check.

    Returns
    -------
    revoked : bool
        True if access token is revoked else false

    """
    token_info = await db.exec(select(Token).where(Token.token == token))
    try:
        if token_info.first().revoked:
            return False
        else:
            return True
    except AttributeError:
        return False


async def list_tokens(db: AsyncSession) -> ScalarResult[Token]:
    """
    List all access token in the :py:class:`~pyPalworldAPI.models.auth_models.Token` SQL table.

    Returns
    -------
    access tokens : iterable object
        All access tokens from SQL table

    """
    token_list = await db.exec(select(Token))
    return token_list


async def list_users(db: AsyncSession):
    """
    List all users in the :py:class:`~pyPalworldAPI.models.auth_models.User` SQL table.

    Returns
    -------
    user : paginate object
        All users from SQL table

    """
    return await paginate(db, select(User))


async def change_password(db: AsyncSession, user: User, new_password: str) -> None:
    """
    Changes user password in the :py:class:`~pyPalworldAPI.models.auth_models.User` SQL table.
    Also removes the users current refresh token from the :py:class:`~pyPalworldAPI.models.auth_models.RefreshToken` SQL table.
    Set all current access tokens for the user in the :py:class:`~pyPalworldAPI.models.auth_models.Token` SQL table to revoked.

    Parameters
    ----------
    user : User
        User to change password for.
    new_password : str
        Users new password.

    Returns
    -------
    None

    """
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


async def delete_user(db: AsyncSession, user: User) -> None:
    """
    Deletes user in the :py:class:`~pyPalworldAPI.models.auth_models.User` SQL table.
    Also removes the users refresh token from the :py:class:`~pyPalworldAPI.models.auth_models.RefreshToken` SQL table.
    Set all access tokens for the user in the :py:class:`~pyPalworldAPI.models.auth_models.Token` SQL table to revoked.

    Parameters
    ----------
    user : User
        User to delete.

    Returns
    -------
    None

    """
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


async def change_user_status(db: AsyncSession, user: User, disabled: bool) -> None:
    """
    Changes the disabled status for user in the :py:class:`~pyPalworldAPI.models.auth_models.User` SQL table.
    Also removes the users refresh token from the :py:class:`~pyPalworldAPI.models.auth_models.RefreshToken` SQL table.
    Set all access tokens for the user in the :py:class:`~pyPalworldAPI.models.auth_models.Token` SQL table to revoked.

    Parameters
    ----------
    user : User
        User to delete.
    disabled : bool
        Mark if users account is disabled or not

    Returns
    -------
    None

    """
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


async def delete_old_tokens(db: AsyncSession, tokens: list) -> None:
    """
    Removes expired access tokens from the :py:class:`~pyPalworldAPI.models.auth_models.Token` SQL table.

    Parameters
    ----------
    tokens : list
        List of access tokens.

    Returns
    -------
    None

    """
    for token in tokens:
        result = await db.exec(select(Token).where(Token.token == token.token))
        user_tokens = result.first()
        await db.delete(user_tokens)
    await db.commit()
    return


async def change_scope(db: AsyncSession, user: User, new_scope: list) -> None:
    """
    Changes the users scopes in the :py:class:`~pyPalworldAPI.models.auth_models.User` SQL table.
    Also set all access tokens for the user in the :py:class:`~pyPalworldAPI.models.auth_models.Token` SQL table to revoked.

    Parameters
    ----------
    user : User
        User to delete.
    new_scope : list
        Users new scopes

    Returns
    -------
    None

    """
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
