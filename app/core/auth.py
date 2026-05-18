from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verificar_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verificar_token(token)
    return payload