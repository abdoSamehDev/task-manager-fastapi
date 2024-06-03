from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from .database import get_db
from .utils import ALGORITHM, SECRET_KEY
from .crud.user import get_user_by_email
from .schemas import TokenData
import logging

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Couldn't validate credentials",
        headers={"WWW_Authenticate": "Bearer"},
    )
    try:
        logging.info(f"Token: {token}")  # Log the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logging.info(f"Payload: {payload}")  # Log the payload
        email: str = payload.get("sub")
        if email is None:
            raise credential_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credential_exception
    user = get_user_by_email(db=db, email=token_data.email)
    if user is None:
        raise credential_exception
    return user
