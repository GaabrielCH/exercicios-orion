// =================================================================
// EXERCÍCIO 3 - NoSQL CRUD BÁSICO (MongoDB)
// =================================================================

use orion_blog

db.posts.insertOne({
    titulo: "Introdução ao MongoDB",
    autor: "Gabriel CH",
    conteudo: "MongoDB é um banco de dados NoSQL orientado a documentos. Ele armazena dados em formato JSON-like (BSON), oferecendo flexibilidade de schema e escalabilidade horizontal."
})

db.posts.insertOne({
    titulo: "Schema Flexível no NoSQL",
    autor: "Maria Santos",
    conteudo: "Uma das principais vantagens dos bancos NoSQL é a flexibilidade de schema. Diferente dos bancos relacionais, você pode adicionar campos novos sem precisar alterar toda a estrutura.",
    tags: ["nosql", "mongodb", "flexivel", "schema"]
})

db.posts.find().pretty()


// =================================================================
// VERIFICAÇÕES
// =================================================================

db.posts.countDocuments()

db.posts.find({ tags: { $exists: true } }).pretty()

db.posts.find({ tags: { $exists: false } }).pretty()

db.posts.find({}, { titulo: 1, autor: 1, _id: 0 })
