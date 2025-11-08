// =================================================================
// EXERCÍCIO 4 - NoSQL CONSULTAS AVANÇADAS (MongoDB)
// =================================================================

use orion_blog


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

db.posts.find({
    tags: "nosql"
}).pretty()

db.posts.find({
    autor: "Maria Santos"
}).pretty()


// =================================================================
// EXTRA (AVANÇADO)
// =================================================================


db.posts.find({
    comentarios: {
        $elemMatch: {
            usuario: "João Silva"
        }
    }
}).pretty()


db.posts.find({ comentarios: { $exists: true } }).pretty()

db.posts.countDocuments({ tags: "nosql" })

db.posts.countDocuments({ comentarios: { $exists: true } })

db.posts.distinct("tags")

db.posts.find({
    tags: { $all: ["nosql", "mongodb"] }
}).pretty()

db.posts.find({
    tags: { $size: 2 }
}).pretty()

db.posts.find(
    {},
    { titulo: 1, tags: 1, _id: 0 }
)
