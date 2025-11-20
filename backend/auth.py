from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, Request
from pwdlib import PasswordHash
from database.orm import AsyncORM
from datetime import datetime, timedelta, timezone
from database import modelsDTO
import jwt
import os
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from models import Token, TokenData
from conf import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

password_hash = PasswordHash.recommended()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Shared exception used when token is missing or invalid
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


async def get_token_from_request(request: Request) -> str:
    """Extract bearer token from Authorization header or from cookie 'access_token'.

    Preference is given to Authorization header. If neither present, raise 401.
    """
    # auth_header = request.headers.get("Authorization")
    # if auth_header:
    #     parts = auth_header.split()
    #     if len(parts) == 2 and parts[0].lower() == "bearer":
    #         return parts[1]

    token = request.cookies.get("access_token")
    if token:
        return token

    raise credentials_exception

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password,hashed_password)


async def authenticate_user(login:str, password:str) -> modelsDTO.UserDTO | bool:
    user = await AsyncORM.get_user_by_login(login)
    if not user:
        return False
    if not verify_password(password, user.psw):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_active_user(
    token: Annotated[str, Depends(get_token_from_request)],
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login = payload.get("sub")
        if login is None:
            raise credentials_exception
        token_data = TokenData(login=login)
    except InvalidTokenError:
        raise credentials_exception

    user = await AsyncORM.get_user_by_login(login=token_data.login) # type: ignore
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user_login(
    token: Annotated[str, Depends(get_token_from_request)],
) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login = payload.get("sub")
        if login is None:
            raise credentials_exception
        token_data = TokenData(login=login)
    except InvalidTokenError:
        raise credentials_exception

    return token_data
