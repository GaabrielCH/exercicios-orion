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

### Via MongoDB Compass
1. Conecte com: `mongodb://orion_admin:orion_admin_pass@localhost:27017/?authSource=admin`
2. Banco: `orion_blog`
3. Collection: `posts`
4. Use filtros para testar as queries
5. Capture screenshots de cada operação

### Via Terminal

```powershell
# Adicionar comentários a um post
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.updateOne({titulo:'Introducao ao MongoDB'},{`$set:{comentarios:[{usuario:'Joao Silva',texto:'Excelente!'},{usuario:'Ana Costa',texto:'Muito bom!'}]}})"

# Verificar atualização
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find({titulo:'Introducao ao MongoDB'}).forEach(printjson)"

# Buscar posts com tag específica
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find({tags:'nosql'}).forEach(printjson)"

# Buscar por autor
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find({autor:'Maria Santos'}).forEach(printjson)"

# Buscar posts com comentário de usuário específico (array aninhado)
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find({comentarios:{`$elemMatch:{usuario:'Joao Silva'}}}).forEach(printjson)"

# Contar posts com comentários
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "print(db.posts.countDocuments({comentarios:{`$exists:true}}))"

# Listar todas as tags únicas
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "printjson(db.posts.distinct('tags'))"

# Buscar posts que têm múltiplas tags específicas
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find({tags:{`$all:['nosql','mongodb']}}).forEach(printjson)"

# Projeção: mostrar apenas título e tags
docker exec orion_mongo_db mongosh --authenticationDatabase admin -u orion_admin -p orion_admin_pass orion_blog --eval "db.posts.find({},{titulo:1,tags:1,_id:0}).forEach(printjson)"
```

### Resultados Esperados

**updateOne**: Adiciona array comentarios ao post
**find com tags**: Retorna posts que contêm tag específica
**$elemMatch**: Busca em arrays aninhados
**distinct**: Lista tags únicas
**$all**: Posts com múltiplas tags específicas
**Projeção**: Mostra apenas campos selecionados

### Screenshots

![Queries gerais](screenshots/exercicio4-geralteste.jpg)
![Queries extras](screenshots/exercicio4-geralextra.jpg)
![Verificação final](screenshots/exercicio4-extraverificacao.jpg)

As imagens mostram operadores avançados como $elemMatch para buscar em arrays aninhados, $all para múltiplos critérios, distinct para valores únicos e projeções para selecionar campos específicos.

