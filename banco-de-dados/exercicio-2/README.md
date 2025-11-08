# Exercício 2 - SQL com JOINs e Filtros

## Objetivo
Aprender a consultar dados de múltiplas tabelas usando JOIN e filtrar resultados com WHERE.

## Pré-requisito
Complete o Exercício 1 antes de começar este exercício.

## Tarefas

### 1. INNER JOIN
Escrever um SELECT que mostre o nome do aluno e o nome do curso em uma única consulta.

### 2. WHERE + JOIN
Mostrar apenas os alunos de um curso específico (ex: "Desenvolvimento Web").

### 3. UPDATE
Alterar o `curso_id` de um aluno específico (ex: mover Maria para outro curso).

### 4. Verificar UPDATE
Fazer novo SELECT com JOIN para confirmar a mudança.

### 5. EXTRA (Avançado)
LEFT JOIN + WHERE para descobrir cursos sem alunos.

## Critérios de Sucesso
- [ ] JOIN retorna nomes corretos (aluno + curso)
- [ ] WHERE filtra corretamente
- [ ] UPDATE funciona e é refletido no SELECT
- [ ] Extra: LEFT JOIN identifica cursos vazios

## Como Executar

### Via Terminal
```bash
docker exec -it orion_postgres_db psql -U orion_user -d orion_db -f /tmp/solucao.sql
```

### Via DBeaver/pgAdmin
1. Conecte ao banco PostgreSQL
2. Abra o arquivo `solucao.sql`
3. Execute os comandos um por um

