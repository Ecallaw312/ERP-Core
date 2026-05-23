from pydantic import BaseModel, EmailStr, Field

#Schema de Usuário
class UserCreate(BaseModel):
    nome: str = Field(
        ...,
        description="Nome completo do usuário.",
        example="João Silva"
    )
    email: EmailStr = Field(
        ...,
        description="Email válido do usuário.",
        example="joao@email.com"
    )
    senha: str = Field(
        ...,
        description="Senha do usuário.",
        example="123456"
    )
    perfil: str = Field(
        default="user",
        description="Perfil do usuário (ex: admin, user).",
        example="user"
    )