# Exercício 1 - SQL Básico (CREATE TABLE, INSERT, SELECT)

## Objetivo
Aprender os comandos básicos de SQL para Definição (CREATE TABLE) e Manipulação (INSERT, SELECT).

## Tarefas

### 1. Criar tabela de cursos
- Colunas: `id` (PK), `nome_curso`

### 2. Criar tabela de alunos
- Colunas: `id` (PK), `nome`, `email`, `curso_id` (FK)
- `curso_id` referencia `cursos.id`

### 3. Inserir dados
- 2-3 cursos
- 3-4 alunos (relacionados aos cursos)

### 4. Consultar dados
- `SELECT * FROM cursos;`
- `SELECT * FROM alunos;`

## Critérios de Sucesso
- [ ] Tabelas criadas sem erros
- [ ] Chave estrangeira impede inserção de `curso_id` inválido
- [ ] Dados inseridos corretamente
- [ ] SELECT retorna todos os registros

## Como Executar

### Opção 1: Via DBeaver/pgAdmin
1. Conecte ao banco PostgreSQL (dados em `banco-de-dados/README.md`)
2. Abra o arquivo `solucao.sql`
3. Execute os comandos

### Opção 2: Via Terminal
```bash
# Copiar o arquivo SQL para o container
docker cp solucao.sql orion_postgres_db:/tmp/

# Executar o script
docker exec -it orion_postgres_db psql -U orion_user -d orion_db -f /tmp/solucao.sql

# Ou conectar e executar manualmente
docker exec -it orion_postgres_db psql -U orion_user -d orion_db
```

