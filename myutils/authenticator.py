from fastapi import status, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from myutils import tokenizer


oauth_scheme = OAuth2PasswordBearer(tokenUrl='login')


def get_curent_user(token: str = Depends(oauth_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return tokenizer.verify_token(token, credentials_exception)
