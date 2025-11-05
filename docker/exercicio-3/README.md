# Exercício 3: Multi-container com Docker Compose

## 🎯 Objetivos
- Trabalhar com múltiplos containers
- Usar Docker Compose
- Conectar aplicação web a banco de dados
- Gerenciar redes e volumes
- Orquestrar serviços

## 📁 Estrutura do Projeto
```
exercicio-3/
├── docker-compose.yml
├── web/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── init-db/
│   └── init.sql
└── README.md
```

## 🛠️ O que foi implementado

### Serviços

#### 1. Web (Flask)
- API REST para gerenciar tarefas (To-Do List)
- Conecta ao PostgreSQL
- Porta: 8000

#### 2. Database (PostgreSQL)
- Banco de dados relacional
- Persistência com volume
- Porta: 5432

#### 3. Adminer (Opcional)
- Interface web para gerenciar banco
- Porta: 8080

## 🌐 Arquitetura

```
┌─────────────────┐
│   Cliente       │
│  (Browser/curl) │
└────────┬────────┘
         │
         │ HTTP (8000)
         ▼
┌─────────────────┐
│   Web Service   │
│   (Flask App)   │
└────────┬────────┘
         │
         │ PostgreSQL (5432)
         ▼
┌─────────────────┐
│   Database      │
│  (PostgreSQL)   │
└─────────────────┘
         │
         │ HTTP (8080)
         ▼
┌─────────────────┐
│    Adminer      │
│  (DB Manager)   │
└─────────────────┘
```

## 🚀 Como Executar

### Passo 1: Navegar até o diretório
```bash
cd exercicio-3
```

### Passo 2: Iniciar todos os serviços
```bash
docker-compose up -d
```

**Explicação:**
- `docker-compose up`: Inicia os serviços
- `-d`: Modo detached (background)

### Passo 3: Verificar status dos serviços
```bash
docker-compose ps
```

### Passo 4: Ver logs
```bash
# Todos os serviços
docker-compose logs -f

# Apenas web
docker-compose logs -f web

# Apenas database
docker-compose logs -f db
```

## 🌐 Endpoints da API

### GET /
Informações da API

### GET /health
Status da aplicação e conexão com banco

### GET /tasks
Lista todas as tarefas
```json
[
  {
    "id": 1,
    "title": "Minha tarefa",
    "completed": false,
    "created_at": "2025-11-05T10:00:00"
  }
]
```

### POST /tasks
Cria nova tarefa
```json
// Request
{
  "title": "Nova tarefa"
}

// Response
{
  "id": 1,
  "title": "Nova tarefa",
  "completed": false,
  "message": "Tarefa criada com sucesso"
}
```

### PUT /tasks/:id
Atualiza tarefa
```json
// Request
{
  "title": "Tarefa atualizada",
  "completed": true
}
```

### DELETE /tasks/:id
Remove tarefa

## 🧪 Testando a Aplicação

### Usando curl

**Listar tarefas:**
```powershell
curl http://localhost:8000/tasks
```

**Criar tarefa:**
```powershell
curl -X POST http://localhost:8000/tasks `
  -H "Content-Type: application/json" `
  -d '{\"title\":\"Estudar Docker\"}'
```

**Atualizar tarefa:**
```powershell
curl -X PUT http://localhost:8000/tasks/1 `
  -H "Content-Type: application/json" `
  -d '{\"title\":\"Estudar Docker Compose\",\"completed\":true}'
```

**Deletar tarefa:**
```powershell
curl -X DELETE http://localhost:8000/tasks/1
```

### Usando Adminer

1. Acesse: http://localhost:8080
2. Faça login:
   - **Sistema**: PostgreSQL
   - **Servidor**: db
   - **Usuário**: postgres
   - **Senha**: postgres123
   - **Base de dados**: tododb

3. Navegue pelas tabelas e dados

## 🔍 Comandos Docker Compose

### Gerenciamento Básico

```bash
# Iniciar serviços
docker-compose up -d

# Parar serviços (mantém containers)
docker-compose stop

# Parar e remover containers
docker-compose down

# Parar e remover containers + volumes
docker-compose down -v

# Parar e remover tudo (containers, volumes, redes, imagens)
docker-compose down -v --rmi all
```

### Logs e Monitoramento

```bash
# Ver logs de todos os serviços
docker-compose logs

# Ver logs em tempo real
docker-compose logs -f

# Ver logs de serviço específico
docker-compose logs web
docker-compose logs db

# Últimas 100 linhas
docker-compose logs --tail=100
```

### Build e Reconstrução

```bash
# Construir imagens
docker-compose build

# Construir sem usar cache
docker-compose build --no-cache

# Reconstruir e iniciar
docker-compose up -d --build

# Forçar recriação de containers
docker-compose up -d --force-recreate
```

### Execução de Comandos

```bash
# Executar comando no serviço
docker-compose exec web sh
docker-compose exec db psql -U postgres -d tododb

# Executar sem estar no container
docker-compose run web python -c "print('Hello')"
```

### Status e Informações

```bash
# Ver status dos serviços
docker-compose ps

# Ver processos rodando
docker-compose top

# Ver configuração processada
docker-compose config

# Ver portas mapeadas
docker-compose port web 8000
```

## 🎓 Conceitos Aprendidos

### 1. Docker Compose
- Definição de múltiplos serviços
- Arquivo YAML de configuração
- Orquestração de containers
- Dependências entre serviços

### 2. Redes Docker
- Rede bridge automática
- Comunicação entre containers
- DNS interno (nome do serviço)
- Isolamento de rede

### 3. Volumes Docker
- Persistência de dados
- Named volumes
- Bind mounts
- Compartilhamento entre containers

### 4. Variáveis de Ambiente
- Configuração de serviços
- Credenciais de banco
- Comunicação entre containers

### 5. Integração com Banco de Dados
- Conexão Python + PostgreSQL
- Connection pooling
- Migrations/Inicialização

## 📊 Estrutura do docker-compose.yml

```yaml
version: '3.8'

services:
  # Serviço web (Flask)
  web:
    build: ./web
    ports:
      - "8000:8000"
    environment:
      - DB_HOST=db
    depends_on:
      - db
    networks:
      - app-network

  # Serviço de banco (PostgreSQL)
  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_PASSWORD=postgres123
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - app-network

volumes:
  postgres-data:

networks:
  app-network:
    driver: bridge
```

## 🔧 Troubleshooting

### Serviço não inicia
```bash
# Ver logs detalhados
docker-compose logs web

# Verificar configuração
docker-compose config
```

### Erro de conexão com banco
```bash
# Verificar se banco está rodando
docker-compose ps db

# Verificar logs do banco
docker-compose logs db

# Testar conexão manualmente
docker-compose exec web ping db
```

### Porta já em uso
```yaml
# Mudar porta no docker-compose.yml
ports:
  - "8001:8000"  # Host:Container
```

### Dados não persistem
```bash
# Verificar volumes
docker volume ls

# Ver detalhes do volume
docker volume inspect exercicio-3_postgres-data
```

### Reconstruir do zero
```bash
# Parar tudo e limpar
docker-compose down -v --rmi all

# Construir novamente
docker-compose up -d --build
```

## 📚 Próximos Passos

- ✅ Exercício 4: Persistência avançada com Volumes

## 🎯 Desafios Extras

1. **Redis Cache**: Adicionar Redis para cache
2. **Nginx**: Adicionar proxy reverso
3. **Autenticação**: Implementar login
4. **Frontend**: Criar interface web
5. **Backup**: Script de backup do banco
6. **Monitoring**: Adicionar Prometheus + Grafana
7. **Load Balancer**: Escalar serviço web
8. **Environment Files**: Usar arquivos .env

### Exemplo: Adicionar Redis

```yaml
services:
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    networks:
      - app-network
```

## 📖 Recursos

- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [PostgreSQL Docker Image](https://hub.docker.com/_/postgres)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- [Docker Networking](https://docs.docker.com/network/)
