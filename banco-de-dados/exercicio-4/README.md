# Exercício 4 - NoSQL Consultas Avançadas (MongoDB)

## Objetivo
Aprender a consultar (filtrar) dados com base em campos específicos, arrays e documentos aninhados.

## Pré-requisito
Complete o Exercício 3 antes de começar este exercício.

## Tarefas

### 1. Atualizar documento com comentários
Usar `updateOne()` para adicionar campo `comentarios` (array de documentos).

### 2. Consultar por tag
Escrever `find()` que retorne apenas posts com tag "nosql".

### 3. Consultar por autor
Escrever `find()` que retorne apenas posts de um autor específico.

### 4. Consultar comentários (extra)
Filtrar posts que têm comentários de um usuário específico.

## Critérios de Sucesso
- [ ] `updateOne()` adiciona array de comentários
- [ ] Query por tag retorna resultado correto
- [ ] Query por autor retorna resultado correto
- [ ] Query em array aninhado funciona (extra)

## Como Executar

### Via Terminal
```bash
# Conectar ao MongoDB
docker exec -it orion_mongo_db mongosh -u orion_admin -p orion_admin_pass

# Usar o banco
use orion_blog

# Executar comandos do solucao.js manualmente
```

