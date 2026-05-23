from pydantic import BaseModel, EmailStr, Field

# Schema de Login
class Login(BaseModel):
    email: EmailStr = Field(
        ...,
        description="Email cadastrado do usuário.",
        example="joao@email.com"
    )
    senha: str = Field(
        ...,
        description="Senha cadastrada do usuário.",
        example="123456"
    )