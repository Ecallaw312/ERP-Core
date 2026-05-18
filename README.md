📦 Core ERP API

API central do sistema ERP responsável por autenticação, autorização e gerenciamento de módulos.
Desenvolvida em Python + FastAPI, seguindo padrões REST e preparada para integração com frontend e outros serviços.

🚀 Tecnologias Utilizadas
Python 3.13
FastAPI
SQLAlchemy
SQLite (pode ser trocado por PostgreSQL)
JWT (JSON Web Token)
Passlib (hash de senha)
Pytest (testes automatizados)
Uvicorn (servidor ASGI)
📁 Estrutura do Projeto
app/
 ├── core/
 │   ├── auth.py
 │   ├── database.py
 │   ├── deps.py
 │   └── security.py
 │
 ├── models/
 │   ├── user.py
 │   ├── module.py
 │   └── refresh_token.py
 │
 ├── schemas/
 │   ├── user.py
 │   └── module.py
 │
 ├── routers/
 │   ├── auth.py
 │   └── module.py
 │
 └── main.py

tests/
 ├── test_auth.py
 └── test_module.py
⚙️ Como Rodar o Projeto
1. Clonar repositório
git clone https://github.com/seu-usuario/core-erp.git
cd core-erp
2. Criar ambiente virtual
python -m venv venv
Ativar:

Windows

venv\Scripts\activate

Linux/Mac

source venv/bin/activate
3. Instalar dependências
pip install -r requirements.txt
4. Rodar aplicação
uvicorn app.main:app --reload
5. Acessar documentação

Swagger:

http://localhost:8000/docs
🔐 Autenticação

A API utiliza JWT Bearer Token.

📌 Login
POST /auth/login
{
  "email": "usuario@email.com",
  "senha": "123456"
}
✅ Resposta:
{
  "access_token": "TOKEN",
  "refresh_token": "TOKEN",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "nome": "Usuário",
    "email": "usuario@email.com",
    "perfil": "user"
  }
}
📌 Verify Token
GET /auth/verify

Header obrigatório:

Authorization: Bearer SEU_TOKEN
✅ Resposta:
{
  "valid": true,
  "user": {
    "id": 1,
    "nome": "Usuário",
    "email": "usuario@email.com",
    "perfil": "user"
  }
}
📌 Refresh Token
POST /auth/refresh
{
  "token": "REFRESH_TOKEN"
}
✅ Resposta:
{
  "access_token": "NOVO_TOKEN",
  "token_type": "bearer"
}
🧩 Módulos
📌 Criar módulo
POST /modules/

Header:

Authorization: Bearer TOKEN

Body:

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
{
  "status": "ok"
}
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

http://localhost:3000
🧪 Testes

Rodar testes:

python -m pytest
🔒 Segurança
Senhas criptografadas com bcrypt
Autenticação via JWT
Proteção de rotas com dependência (Depends)
Refresh token com expiração
📌 Integração com Frontend

O backend segue padrão esperado pelo frontend:

Token JWT no header
Respostas em JSON padronizadas
Endpoint /auth/verify para validação de sessão
👨‍💻 Autor

Projeto desenvolvido para disciplina de Engenharia de Software / Sistemas Distribuídos.

📄 Licença

Uso acadêmico.

🚀 Observação Final

Este projeto implementa o Core de autenticação de um ERP, servindo como base para integração com múltiplos módulos independentes.
