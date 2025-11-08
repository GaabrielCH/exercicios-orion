# Exercícios de Banco de Dados - Orion Bootcamp

Este diretório contém os exercícios práticos de banco de dados relacionais (SQL) e não relacionais (NoSQL).

## Estrutura dos Exercícios

```
banco-de-dados/
├── docker-compose.yml          # Ambiente com PostgreSQL e MongoDB
├── exercicio-1/                # SQL Básico (CREATE, INSERT, SELECT)
├── exercicio-2/                # SQL Avançado (JOINs, WHERE, UPDATE)
├── exercicio-3/                # NoSQL Básico (CRUD, Schema Flexível)
└── exercicio-4/                # NoSQL Avançado (Consultas Complexas)
```

## Pré-Requisitos

### 1. Iniciar os Bancos de Dados

```bash
cd banco-de-dados
docker compose up -d
```

Isso iniciará:
- **PostgreSQL** na porta `5432`
- **MongoDB** na porta `27017`

### 2. Dados de Conexão

#### PostgreSQL (Exercícios 1 e 2)
- **Host**: localhost
- **Porta**: 5432
- **Banco de Dados**: orion_db
- **Usuário**: orion_user
- **Senha**: orion_password

**Ferramentas sugeridas**: DBeaver, Beekeeper Studio, pgAdmin

#### MongoDB (Exercícios 3 e 4)
- **Connection String**: `mongodb://orion_admin:orion_admin_pass@localhost:27017/`

**Ferramentas sugeridas**: MongoDB Compass, Studio 3T

## Exercícios

### Exercício 1: SQL Básico
**Objetivo**: Aprender CREATE TABLE, INSERT e SELECT

- Criar tabelas `cursos` e `alunos`
- Definir chaves primárias e estrangeiras
- Inserir dados de teste

📁 Pasta: `exercicio-1/`

---

### Exercício 2: SQL com JOINs
**Objetivo**: Aprender INNER JOIN, WHERE e UPDATE

- Consultar dados de múltiplas tabelas
- Filtrar resultados com WHERE
- Atualizar registros

📁 Pasta: `exercicio-2/`

---

### Exercício 3: NoSQL CRUD
**Objetivo**: Schema Flexível no MongoDB

- Criar coleção `posts`
- Inserir documentos com estruturas diferentes
- Consultar com `find()`

📁 Pasta: `exercicio-3/`

---

### Exercício 4: NoSQL Avançado
**Objetivo**: Consultas complexas com arrays e documentos aninhados

- Atualizar documentos com `updateOne()`
- Filtrar por campos em arrays
- Consultas em documentos aninhados

📁 Pasta: `exercicio-4/`

## Execução dos Exercícios

Todos os exercícios foram testados e executados com sucesso usando PowerShell no Windows. Os comandos incluem formatação com `Write-Host` para melhor visualização dos resultados.

### Exercício 1: SQL Básico
Criadas tabelas `cursos` e `alunos` com foreign key. Inseridos 3 cursos e 4 alunos. Screenshots mostram a estrutura das tabelas e os dados inseridos.

### Exercício 2: SQL JOINs
Testados INNER JOIN, WHERE, UPDATE e LEFT JOIN. Maria Santos foi movida do curso de Desenvolvimento Web para Ciência de Dados. Screenshots mostram os resultados de cada query.

### Exercício 3: NoSQL CRUD
Inseridos 2 posts demonstrando schema flexível. Post do Gabriel sem tags, post da Maria com array de 4 tags. Screenshots mostram a diferença de estrutura.

### Exercício 4: NoSQL Avançado
Adicionado array de comentários aninhado. Testados operadores `$elemMatch`, `$all`, `distinct`, projeções. Screenshots mostram queries complexas funcionando.

## Comandos Úteis

### Docker Compose

```powershell
# Iniciar os bancos
docker compose up -d

# Ver logs
docker compose logs -f

# Parar os bancos (mantém os dados)
docker compose down

# Parar e remover volumes (apaga os dados)
docker compose down -v

# Verificar status
docker compose ps
```

### PostgreSQL

```powershell
# Executar script SQL
Get-Content solucao.sql | docker exec -i orion_postgres_db psql -U orion_user -d orion_db

# Conectar ao PostgreSQL
docker exec -it orion_postgres_db psql -U orion_user -d orion_db

# Dentro do psql:
\dt          # Listar tabelas
\d alunos    # Descrever tabela alunos
\q           # Sair
```

### MongoDB

```powershell
# Executar comandos individuais
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find().forEach(printjson)"

# Conectar ao MongoDB
docker exec -it orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass

# Dentro do mongosh:
show dbs                    # Listar bancos
use orion_blog              # Usar banco
show collections            # Listar coleções
db.posts.find()             # Ver posts
exit                        # Sair
```

## Como Entregar

1. Cada exercício deve ter sua pasta com:
   - Scripts SQL (`.sql`) para exercícios 1 e 2
   - Scripts MongoDB (`.js` ou `.txt`) para exercícios 3 e 4
   - Screenshots dos resultados

2. Criar branch para cada exercício:
```bash
git checkout -b exercicio-bd-1
git add banco-de-dados/exercicio-1/
git commit -m "feat: adiciona solução do exercício 1 de banco de dados"
git push origin exercicio-bd-1
```

3. Abrir Pull Request para `main`

4. Enviar link do repositório para o mentor

## Ordem Recomendada

1. **Exercício 1**: Fundamentos SQL (30min)
2. **Exercício 2**: JOINs e filtros (45min)
3. **Exercício 3**: NoSQL básico (30min)
4. **Exercício 4**: NoSQL avançado (45min)

## Troubleshooting

### Porta já em uso
```bash
# Verificar o que está usando a porta
netstat -ano | findstr :5432
netstat -ano | findstr :27017

# Parar containers
docker compose down
```

### Resetar banco de dados
```bash
# Apagar todos os dados e começar do zero
docker compose down -v
docker compose up -d
```

### Erro de conexão
```bash
# Verificar se containers estão rodando
docker compose ps

# Ver logs de erro
docker compose logs db_postgres
docker compose logs db_mongo
```

## Recursos Adicionais

### PostgreSQL
- [Documentação Oficial](https://www.postgresql.org/docs/)
- [SQL Tutorial](https://www.postgresqltutorial.com/)

### MongoDB
- [Documentação Oficial](https://docs.mongodb.com/)
- [MongoDB University](https://university.mongodb.com/)

## Sobre

Exercícios criados para o Orion Bootcamp - New Rizon

Objetivo: Ensinar SQL e NoSQL de forma prática e progressiva.
