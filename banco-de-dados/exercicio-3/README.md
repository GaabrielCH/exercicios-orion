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
1. Conecte com: `mongodb://orion_admin:orion_admin_pass@localhost:27017/?authSource=admin`
2. Crie o banco `orion_blog`
3. Crie a coleção `posts`
4. Use a interface para inserir e consultar
5. Capture screenshots mostrando os dois posts com estruturas diferentes

### Opção 2: Via Terminal

```powershell
# Inserir primeiro post (sem tags)
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.insertOne({titulo:'Introducao ao MongoDB',autor:'Gabriel CH',conteudo:'MongoDB e um banco NoSQL orientado a documentos'})"

# Inserir segundo post (com tags)
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.insertOne({titulo:'Schema Flexivel no NoSQL',autor:'Maria Santos',conteudo:'NoSQL permite diferentes estruturas na mesma colecao',tags:['nosql','mongodb','flexivel','schema']})"

# Ver todos os posts
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find().forEach(printjson)"

# Consultar posts SEM tags
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find({tags:{`$exists:false}}).forEach(printjson)"

# Consultar posts COM tags
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find({tags:{`$exists:true}}).forEach(printjson)"
```

### Resultados Esperados

**Post 1** (Gabriel): titulo, autor, conteudo
**Post 2** (Maria): titulo, autor, conteudo, tags

O segundo documento tem um campo adicional que o primeiro não tem. Isso demonstra o schema flexível do MongoDB.

### Screenshots

![Schema flexível](screenshots/exercicio3-geralteste.jpg)

A imagem mostra os dois documentos com estruturas diferentes na mesma coleção, provando a flexibilidade do schema no MongoDB.
