// =================================================================
// EXERCÍCIO 3 - NoSQL CRUD BÁSICO (MongoDB)
// =================================================================
// Aluno: [Seu Nome]
// Data: [Data]
// =================================================================

// PASSO 1: Selecionar/Criar o banco de dados
use orion_blog


// PASSO 2: Inserir primeiro documento (estrutura básica)
// Post básico com 3 campos

db.posts.insertOne({
    titulo: "Introdução ao MongoDB",
    autor: "Gabriel CH",
    conteudo: "MongoDB é um banco de dados NoSQL orientado a documentos. Ele armazena dados em formato JSON-like (BSON), oferecendo flexibilidade de schema e escalabilidade horizontal."
})


// PASSO 3: Inserir segundo documento (com campo adicional)
// Post com campo tags (array) - demonstrando Schema Flexível

db.posts.insertOne({
    titulo: "Schema Flexível no NoSQL",
    autor: "Maria Santos",
    conteudo: "Uma das principais vantagens dos bancos NoSQL é a flexibilidade de schema. Diferente dos bancos relacionais, você pode adicionar campos novos sem precisar alterar toda a estrutura.",
    tags: ["nosql", "mongodb", "flexivel", "schema"]
})


// PASSO 4: Consultar todos os documentos
// TODO: Usar find() para listar todos os posts

db.posts.find().pretty()


// =================================================================
// VERIFICAÇÕES
// =================================================================

// Contar quantos documentos foram inseridos
db.posts.countDocuments()

// Verificar quais documentos TÊM o campo 'tags'
db.posts.find({ tags: { $exists: true } }).pretty()

// Verificar quais documentos NÃO TÊM o campo 'tags'
db.posts.find({ tags: { $exists: false } }).pretty()

// Mostrar apenas os campos titulo e autor
db.posts.find({}, { titulo: 1, autor: 1, _id: 0 })
