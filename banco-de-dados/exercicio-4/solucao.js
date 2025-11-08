// =================================================================
// EXERCÍCIO 4 - NoSQL CONSULTAS AVANÇADAS (MongoDB)
// =================================================================
// Aluno: [Seu Nome]
// Data: [Data]
// =================================================================

// PASSO 1: Selecionar o banco de dados
use orion_blog


// PASSO 2: Atualizar um post para adicionar comentários
// Adicionar array de comentários ao primeiro post

db.posts.updateOne(
    { titulo: "Introdução ao MongoDB" },
    {
        $set: {
            comentarios: [
                {
                    usuario: "João Silva",
                    texto: "Excelente introdução! Muito esclarecedor.",
                    data: new Date("2025-11-01")
                },
                {
                    usuario: "Ana Costa",
                    texto: "MongoDB realmente facilita muito o desenvolvimento.",
                    data: new Date("2025-11-02")
                },
                {
                    usuario: "Pedro Oliveira",
                    texto: "Gostei da explicação sobre BSON.",
                    data: new Date("2025-11-03")
                }
            ]
        }
    }
)


// PASSO 3: Consultar posts com uma tag específica
// Buscar posts que contêm "nosql" no array de tags

db.posts.find({
    tags: "nosql"
}).pretty()


// PASSO 4: Consultar posts de um autor específico
// Buscar todos os posts da Maria Santos

db.posts.find({
    autor: "Maria Santos"
}).pretty()


// =================================================================
// EXTRA (AVANÇADO)
// =================================================================

// PASSO 5: Consultar posts que têm comentários de um usuário específico
// Buscar posts que têm comentários do João Silva

db.posts.find({
    comentarios: {
        $elemMatch: {
            usuario: "João Silva"
        }
    }
}).pretty()


// =================================================================
// CONSULTAS ADICIONAIS PARA VERIFICAÇÃO
// =================================================================

// Mostrar todos os posts com seus comentários
db.posts.find({ comentarios: { $exists: true } }).pretty()

// Contar quantos posts têm a tag "nosql"
db.posts.countDocuments({ tags: "nosql" })

// Contar quantos posts têm comentários
db.posts.countDocuments({ comentarios: { $exists: true } })

// Listar todas as tags únicas
db.posts.distinct("tags")

// Buscar posts que tenham MÚLTIPLAS tags específicas
db.posts.find({
    tags: { $all: ["nosql", "mongodb"] }
}).pretty()

// Buscar posts onde o array de tags tenha EXATAMENTE 2 elementos
db.posts.find({
    tags: { $size: 2 }
}).pretty()

// Buscar posts e mostrar apenas o título e as tags
db.posts.find(
    {},
    { titulo: 1, tags: 1, _id: 0 }
)
