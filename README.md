# 📦 API ERP Núcleo

API central do sistema ERP responsável por autenticação, autorização e gerenciamento de módulos.  
Desenvolvida em **Python + FastAPI**, seguindo padrões REST e preparada para integração com frontend e outros serviços.

---

## 🚀 Tecnologias Utilizadas
- Python 3.13  
- FastAPI  
- SQLAlchemy  
- SQLite (pode ser substituído por PostgreSQL)  
- JWT (JSON Web Token)  
- Passlib (hash de senha)  
- Pytest (testes automatizados)  
- Uvicorn (servidor ASGI)  

---

## 📁 Estrutura do Projeto
app/
├── núcleo/
│   ├── auth.py
│   ├── database.py
│   ├── deps.py
│   └── security.py
│
├── modelos/
│   ├── user.py
│   ├── module.py
│   └── refresh_token.py
│
├── esquemas/
│   ├── user.py
│   └── module.py
│
├── roteadores/
│   ├── auth.py
│   └── module.py
│
└── main.py

tests/
├── test_auth.py
└── test_module.py

---

## ⚙️ Como Rodar o Projeto

1. **Clonar repositório**  
   ```bash
   git clone https://github.com/seu-usuario/core-erp.git núcleo-erp
   cd núcleo-erp
Criar ambiente virtual

bash
python -m venv venv
Ativar ambiente:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Instalar dependências

bash
pip install -r requirements.txt
Rodar aplicação

bash
uvicorn app.main:app --reload
Acessar documentação  
👉 http://localhost:8000/docs

🔐 Autenticação
A API utiliza JWT Bearer Token.

📌 Login
POST /auth/login

json
{
  "email": "usuario@email.com",
  "senha": "123456"
}
Resposta:

json
{
  "access_token": "TOKEN",
  "refresh_token": "TOKEN",
  "token_type": "bearer",
  "usuario": {
    "id": 1,
    "nome": "Usuário",
    "email": "usuario@email.com",
    "perfil": "usuario"
  }
}
📌 Verificação de Token
GET /auth/verify  
Cabeçalho obrigatório:  
Authorization: Bearer SEU_TOKEN

Resposta:

json
{
  "valido": true,
  "usuario": {
    "id": 1,
    "nome": "Usuário",
    "email": "usuario@email.com",
    "perfil": "usuario"
  }
}
📌 Refresh Token
POST /auth/refresh

json
{
  "token": "REFRESH_TOKEN"
}
Resposta:

json
{
  "access_token": "NOVO_TOKEN",
  "token_type": "bearer"
}
🧩 Módulos
📌 Criar módulo
POST /modules/  
Cabeçalho: Authorization: Bearer TOKEN

Corpo:

json
{
  "nome": "Financeiro",
  "url": "http://localhost",
  "porta": 8001
}
📌 Listar módulos
GET /modules/  
Retorna todos os módulos cadastrados.

🩺 Health Check
GET /health  
Resposta:

json
{ "status": "OK" }
⚠️ Códigos HTTP
Código	Significado
200	Sucesso
400	Requisição inválida
401	Não autorizado
403	Acesso negado
404	Não encontrado
500	Erro interno


🌐 CORS
Configurado para permitir acesso do frontend:
👉 http://localhost:3000

🧪 Testes
Rodar testes:

bash
python -m pytest
🔒 Segurança
Senhas criptografadas com bcrypt

Autenticação via JWT

Proteção de rotas com Depends

Refresh token com expiração

📌 Integração com Frontend
Token JWT no header

Respostas em JSON padronizadas

Endpoint /auth/verify para validação de sessão

👨‍💻 Autor
Projeto desenvolvido para disciplina de Sistemas Distribuídos.

📄 Licença
Uso acadêmico.

🚀 Observação Final
Este projeto implementa o Core de autenticação de um ERP, servindo como base para integração com múltiplos módulos independentes.

---
