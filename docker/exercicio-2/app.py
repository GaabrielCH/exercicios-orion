from flask import Flask, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Dados em memória (simulando banco de dados)
users = [
    {"id": 1, "name": "João Silva", "email": "joao@example.com"},
    {"id": 2, "name": "Maria Santos", "email": "maria@example.com"},
    {"id": 3, "name": "Pedro Oliveira", "email": "pedro@example.com"}
]

next_id = 4

# Rota principal
@app.route('/')
def home():
    return jsonify({
        "message": "API REST com Flask e Docker",
        "version": "1.0.0",
        "exercise": "Exercício 2",
        "author": "Gabriel CH",
        "endpoints": {
            "GET /": "Informações da API",
            "GET /health": "Status da aplicação",
            "GET /users": "Lista todos os usuários",
            "GET /users/<id>": "Busca usuário por ID",
            "POST /users": "Cria novo usuário",
            "PUT /users/<id>": "Atualiza usuário",
            "DELETE /users/<id>": "Remove usuário"
        }
    })

# Health check
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "container": os.getenv('HOSTNAME', 'local')
    })

# GET - Listar todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET - Buscar usuário por ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is None:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user), 200

# POST - Criar novo usuário
@app.route('/users', methods=['POST'])
def create_user():
    global next_id
    
    data = request.get_json()
    
    # Validação
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Nome e email são obrigatórios"}), 400
    
    # Verificar se email já existe
    if any(u['email'] == data['email'] for u in users):
        return jsonify({"error": "Email já cadastrado"}), 400
    
    new_user = {
        "id": next_id,
        "name": data['name'],
        "email": data['email']
    }
    
    users.append(new_user)
    next_id += 1
    
    return jsonify({
        **new_user,
        "message": "Usuário criado com sucesso"
    }), 201

# PUT - Atualizar usuário
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user is None:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Dados não fornecidos"}), 400
    
    # Atualizar campos
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        # Verificar se email já existe em outro usuário
        existing = next((u for u in users if u['email'] == data['email'] and u['id'] != user_id), None)
        if existing:
            return jsonify({"error": "Email já cadastrado"}), 400
        user['email'] = data['email']
    
    return jsonify({
        **user,
        "message": "Usuário atualizado com sucesso"
    }), 200

# DELETE - Remover usuário
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    
    user = next((u for u in users if u['id'] == user_id), None)
    
    if user is None:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    users = [u for u in users if u['id'] != user_id]
    
    return jsonify({"message": "Usuário removido com sucesso"}), 200

# Tratamento de erro 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Rota não encontrada"}), 404

# Tratamento de erro 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f"🚀 API Flask iniciada na porta {port}")
    print(f"🐳 Container: {os.getenv('HOSTNAME', 'local')}")
    print(f"📅 {datetime.now().isoformat()}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
