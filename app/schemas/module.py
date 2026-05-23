from pydantic import BaseModel, Field

# Schema de Módulo
class ModuleCreate(BaseModel):
    nome: str = Field(
        ...,
        description="Nome do módulo.",
        example="Financeiro"
    )
    url: str = Field(
        ...,
        description="URL base do módulo.",
        example="http://localhost"
    )
    porta: int = Field(
        ...,
        description="Porta de execução do módulo.",
        example=8000
    )