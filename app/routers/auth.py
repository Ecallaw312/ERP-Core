from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.models.user import User
from app.core.deps import get_db
from app.core.security import hash_senha

from app.schemas.auth import Login
from app.core.security import verificar_senha, criar_token

from app.core.auth import get_current_user

from app.models.refresh_token import RefreshToken
from datetime import datetime, timedelta
from app.core.security import criar_refresh_token


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        nome=user.nome,
        email=user.email,
        senha_hash=hash_senha(user.senha),
        perfil=user.perfil
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"msg": "Usuário criado com sucesso"}

@router.post("/login")
def login(dados: Login, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == dados.email).first()

    if not user:
        return {"erro": "Usuário não encontrado"}

    if not verificar_senha(dados.senha, user.senha_hash):
        return {"erro": "Senha inválida"}

    access_token = criar_token({"sub": user.email})
    refresh_token = criar_refresh_token({"sub": user.email})

    db_refresh = RefreshToken(
        user_id=user.id,
        refresh_token=refresh_token,
        expira_em=datetime.utcnow() + timedelta(days=7)
    )

    db.add(db_refresh)
    db.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

@router.get("/verify")
def verify(user = Depends(get_current_user)):
    return {"msg": "Token válido", "user": user}

@router.get("/private")
def private(user = Depends(get_current_user)):
    return {"msg": "Você está autenticado", "user": user}

@router.post("/refresh")
def refresh(token: str, db: Session = Depends(get_db)):
    db_token = db.query(RefreshToken).filter(RefreshToken.refresh_token == token).first()

    if not db_token:
        return {"erro": "Refresh token inválido"}

    if db_token.expira_em < datetime.utcnow():
        return {"erro": "Refresh token expirado"}

    new_access = criar_token({"sub": "user"})

    return {"access_token": new_access}