# Exercício 3 - NoSQL CRUD Básico (MongoDB)

## Objetivo
Aprender a estrutura básica de um banco NoSQL (MongoDB) e entender o conceito de Schema Flexível.

## Tarefas

### 1. Criar coleção
Nome: `posts`

### 2. Inserir documento básico
Campos: `titulo`, `autor`, `conteudo`

### 3. Inserir documento com campo adicional
Campos: `titulo`, `autor`, `conteudo`, `tags` (array)

### 4. Consultar todos os documentos
Usar `find()` ou `find().pretty()`

## Critérios de Sucesso
- [ ] `find()` retorna os dois documentos
- [ ] Segundo documento possui campo `tags`
- [ ] Primeiro documento NÃO possui campo `tags`
- [ ] Prova do Schema Flexível: estruturas diferentes na mesma coleção

## Como Executar

### Opção 1: Via MongoDB Compass
1. Conecte com: `mongodb://orion_admin:orion_admin_pass@localhost:27017/`
2. Crie o banco `orion_blog`
3. Crie a coleção `posts`
4. Use a interface para inserir e consultar

### Opção 2: Via Terminal (mongosh)
```bash
# Conectar ao MongoDB
docker exec -it orion_mongo_db mongosh -u orion_admin -p orion_admin_pass

# Executar os comandos do arquivo solucao.js
```

### Opção 3: Executar script diretamente
```bash
# Copiar o arquivo para o container
docker cp solucao.js orion_mongo_db:/tmp/

# Executar o script
docker exec -it orion_mongo_db mongosh -u orion_admin -p orion_admin_pass --file /tmp/solucao.js
```
