# Exercícios Orion Bootcamp

Repositório com exercícios práticos de Docker e Banco de Dados do Orion Bootcamp - New Rizon.

## Estrutura do Projeto

```
exercicios-orion/
├── README.md
├── .gitignore
├── docker/                      # Exercícios de Docker
│   ├── README.md
│   ├── exercicio-1/            # Hello World com Node.js
│   ├── exercicio-2/            # API Flask + PostgreSQL
│   ├── exercicio-3/            # Ambientes dev/prod
│   └── exercicio-4/            # Stack Completa
│
└── banco-de-dados/             # Exercícios de Banco de Dados
    ├── README.md
    ├── docker-compose.yml      # PostgreSQL + MongoDB
    ├── exercicio-1/            # SQL Básico
    ├── exercicio-2/            # SQL JOINs
    ├── exercicio-3/            # NoSQL CRUD
    └── exercicio-4/            # NoSQL Avançado
```

## Pré-requisitos

- Docker Desktop instalado
- Git instalado
- Editor de código

## Módulos

### 📦 Docker
Exercícios práticos de containerização e orquestração.

```bash
cd docker
# Ver instruções detalhadas
cat README.md
```

**Exercícios:**
1. Hello World com Node.js
2. API REST com Flask + PostgreSQL
3. Boas Práticas + Ambientes dev/prod
4. Stack Completa (API + DB + Adminer)

### 🗄️ Banco de Dados
Exercícios de SQL (PostgreSQL) e NoSQL (MongoDB).

```bash
cd banco-de-dados
# Iniciar bancos de dados
docker compose up -d
# Ver instruções
cat README.md
```

**Exercícios:**
1. SQL Básico (CREATE, INSERT, SELECT)
2. SQL com JOINs e Filtros
3. NoSQL CRUD e Schema Flexível
4. NoSQL Consultas Avançadas

## Início Rápido

```bash
# Clone o repositório
git clone https://github.com/GaabrielCH/exercicios-orion.git
cd exercicios-orion

# Para exercícios de Docker
cd docker/exercicio-1
docker-compose up -d

# Para exercícios de Banco de Dados
cd banco-de-dados
docker compose up -d
```

## Workflow de Entrega

Cada exercício deve ser entregue via Pull Request:

```bash
# Criar branch para o exercício
git checkout -b exercicio-[modulo]-[numero]

# Exemplo para Docker exercício 1
git checkout -b exercicio-docker-1

# Exemplo para Banco de Dados exercício 1
git checkout -b exercicio-bd-1

# Fazer commit das alterações
git add .
git commit -m "feat: adiciona solução do exercício X"

# Push da branch
git push origin exercicio-[modulo]-[numero]

# Abrir Pull Request no GitHub
# Aguardar aprovação do mentor
```

## Branches

- **main**: Código completo e aprovado
- **develop**: Branch de desenvolvimento (opcional)
- **exercicio-docker-1 a 4**: Exercícios de Docker
- **exercicio-bd-1 a 4**: Exercícios de Banco de Dados

## Autor

Gabriel CH - Orion Bootcamp - New Rizon
