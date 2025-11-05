# Exercício 2: API REST com Python Flask

## Objetivos
- Criar uma API REST usando Flask
- Implementar múltiplos endpoints
- Trabalhar com JSON
- Containerizar aplicação Python

## Estrutura do Projeto
```
exercicio-2/
├── Dockerfile
├── requirements.txt
├── app.py
└── README.md
```

## O que foi implementado

### 1. API Flask (app.py)
- CRUD de usuários (Create, Read, Update, Delete)
- Endpoints RESTful
- Manipulação de dados em memória
- Tratamento de erros

### 2. Dockerfile
- Baseado em `python:3.11-slim`
- Instalação de dependências
- Configuração de ambiente
- Porta 5000 exposta

### 3. requirements.txt
- Flask e dependências necessárias

## Endpoints da API

### GET /
Informações sobre a API
```json
{
  "message": "API REST com Flask e Docker",
  "version": "1.0.0",
  "endpoints": [...]
}
```

### GET /health
Status da aplicação
```json
{
  "status": "healthy",
  "timestamp": "..."
}
```

### GET /users
Lista todos os usuários
```json
[
  {
    "id": 1,
    "name": "João",
    "email": "joao@example.com"
  }
]
```

### GET /users/:id
Busca usuário por ID
```json
{
  "id": 1,
  "name": "João",
  "email": "joao@example.com"
}
```

### POST /users
Cria novo usuário
```json
// Request
{
  "name": "Maria",
  "email": "maria@example.com"
}

// Response
{
  "id": 2,
  "name": "Maria",
  "email": "maria@example.com",
  "message": "Usuário criado com sucesso"
}
```

### PUT /users/:id
Atualiza usuário
```json
// Request
{
  "name": "João Silva",
  "email": "joao.silva@example.com"
}

// Response
{
  "id": 1,
  "name": "João Silva",
  "email": "joao.silva@example.com",
  "message": "Usuário atualizado com sucesso"
}
```

### DELETE /users/:id
Remove usuário
```json
{
  "message": "Usuário removido com sucesso"
}
```

## Como Executar

### Passo 1: Navegar até o diretório
```bash
cd exercicio-2
```

### Passo 2: Construir a imagem Docker
```bash
docker build -t exercicio-2-flask .
```

### Passo 3: Executar o container
```bash
docker run -d -p 5000:5000 --name api-flask exercicio-2-flask
```

### Passo 4: Testar a API

**Ver informações da API:**
```powershell
curl http://localhost:5000
```

**Listar usuários:**
```powershell
curl http://localhost:5000/users
```

**Criar usuário:**
```powershell
curl -X POST http://localhost:5000/users `
  -H "Content-Type: application/json" `
  -d '{\"name\":\"Ana\",\"email\":\"ana@example.com\"}'
```

**Buscar usuário:**
```powershell
curl http://localhost:5000/users/1
```

**Atualizar usuário:**
```powershell
curl -X PUT http://localhost:5000/users/1 `
  -H "Content-Type: application/json" `
  -d '{\"name\":\"Ana Silva\",\"email\":\"ana.silva@example.com\"}'
```

**Deletar usuário:**
```powershell
curl -X DELETE http://localhost:5000/users/1
```

## Testando com Postman ou Insomnia

### 1. Importar Collection

Crie uma nova collection com os seguintes requests:

**GET** `http://localhost:5000/`
**GET** `http://localhost:5000/health`
**GET** `http://localhost:5000/users`
**GET** `http://localhost:5000/users/1`

**POST** `http://localhost:5000/users`
```json
{
  "name": "Teste",
  "email": "teste@example.com"
}
```

**PUT** `http://localhost:5000/users/1`
```json
{
  "name": "Teste Atualizado",
  "email": "teste.atualizado@example.com"
}
```

**DELETE** `http://localhost:5000/users/1`

## Comandos Úteis

### Ver logs em tempo real
```bash
docker logs -f api-flask
```

### Acessar shell do container
```bash
docker exec -it api-flask sh
```

### Verificar processos Python no container
```bash
docker exec api-flask ps aux
```

### Parar e remover
```bash
docker stop api-flask
docker rm api-flask
```

## Conceitos Aprendidos

### 1. RESTful API
- Verbos HTTP (GET, POST, PUT, DELETE)
- Status codes corretos
- JSON como formato de dados
- Rotas RESTful

### 2. Flask Framework
- Roteamento
- Request/Response
- JSON handling
- Error handling

### 3. Python + Docker
- Gerenciamento de dependências
- requirements.txt
- Imagens Python slim
- Variáveis de ambiente

### 4. API Design
- Estrutura de endpoints
- Validação de dados
- Respostas consistentes
- Tratamento de erros

## Troubleshooting

### Porta 5000 em uso (Windows)
No Windows, a porta 5000 pode estar sendo usada pelo AirPlay Receiver.

Solução 1: Use outra porta
```bash
docker run -d -p 5001:5000 --name api-flask exercicio-2-flask
```

Solução 2: Desabilite AirPlay Receiver
- Configurações → Compartilhamento → Desmarcar "AirPlay Receiver"

### Erro ao instalar dependências
```
ERROR: Could not find a version that satisfies the requirement
```
Solução: Verifique o requirements.txt e conexão com internet

### CORS Error
Se estiver acessando de um frontend, pode precisar de CORS:
```python
from flask_cors import CORS
CORS(app)
```

## Próximos Passos

- Exercício 3: Multi-container com Docker Compose
- Exercício 4: Persistência com Volumes

## Desafios Extras

1. Adicionar validação de email com regex
2. Integrar com banco de dados SQLite
3. Implementar autenticação JWT
4. Adicionar testes unitários
5. Documentar API com Swagger/OpenAPI
6. Implementar paginação na listagem
7. Adicionar filtros de busca

## Recursos

- [Flask Documentation](https://flask.palletsprojects.com/)
- [REST API Best Practices](https://restfulapi.net/)
- [Python Docker Best Practices](https://docs.docker.com/language/python/)
