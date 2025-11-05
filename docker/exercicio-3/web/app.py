from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from datetime import datetime
import time

app = Flask(__name__)

# Configurações do banco de dados
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': os.getenv('DB_PORT', '5432'),
    'database': os.getenv('DB_NAME', 'tododb'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'postgres123')
}

def get_db_connection():
    """Cria conexão com o banco de dados"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def init_db():
    """Inicializa o banco de dados"""
    max_retries = 5
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            conn = get_db_connection()
            if conn is None:
                raise Exception("Falha na conexão")
            
            cursor = conn.cursor()
            
            # Criar tabela se não existir
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    completed BOOLEAN DEFAULT FALSE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            cursor.close()
            conn.close()
            print("✅ Banco de dados inicializado com sucesso!")
            return True
            
        except Exception as e:
            retry_count += 1
            print(f"❌ Tentativa {retry_count}/{max_retries} falhou: {e}")
            if retry_count < max_retries:
                print("⏳ Aguardando 5 segundos antes de tentar novamente...")
                time.sleep(5)
            else:
                print("❌ Não foi possível inicializar o banco de dados")
                return False

# Rota principal
@app.route('/')
def home():
    return jsonify({
        "message": "To-Do List API com Docker Compose",
        "version": "1.0.0",
        "exercise": "Exercício 3",
        "author": "Gabriel CH",
        "services": ["Web (Flask)", "Database (PostgreSQL)", "Adminer"],
        "endpoints": {
            "GET /": "Informações da API",
            "GET /health": "Status da aplicação",
            "GET /tasks": "Lista todas as tarefas",
            "GET /tasks/<id>": "Busca tarefa por ID",
            "POST /tasks": "Cria nova tarefa",
            "PUT /tasks/<id>": "Atualiza tarefa",
            "DELETE /tasks/<id>": "Remove tarefa"
        }
    })

# Health check
@app.route('/health')
def health():
    conn = get_db_connection()
    db_status = "connected" if conn else "disconnected"
    
    if conn:
        conn.close()
    
    return jsonify({
        "status": "healthy" if db_status == "connected" else "unhealthy",
        "database": db_status,
        "timestamp": datetime.now().isoformat(),
        "container": os.getenv('HOSTNAME', 'local')
    }), 200 if db_status == "connected" else 503

# GET - Listar todas as tarefas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erro na conexão com banco de dados"}), 500
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
        tasks = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return jsonify([dict(task) for task in tasks]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET - Buscar tarefa por ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erro na conexão com banco de dados"}), 500
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
        task = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if task is None:
            return jsonify({"error": "Tarefa não encontrada"}), 404
        
        return jsonify(dict(task)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST - Criar nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "Título é obrigatório"}), 400
    
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erro na conexão com banco de dados"}), 500
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(
            'INSERT INTO tasks (title) VALUES (%s) RETURNING *',
            (data['title'],)
        )
        new_task = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({
            **dict(new_task),
            "message": "Tarefa criada com sucesso"
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT - Atualizar tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Dados não fornecidos"}), 400
    
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erro na conexão com banco de dados"}), 500
    
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        # Verificar se tarefa existe
        cursor.execute('SELECT * FROM tasks WHERE id = %s', (task_id,))
        if cursor.fetchone() is None:
            cursor.close()
            conn.close()
            return jsonify({"error": "Tarefa não encontrada"}), 404
        
        # Construir query de atualização dinamicamente
        update_fields = []
        values = []
        
        if 'title' in data:
            update_fields.append('title = %s')
            values.append(data['title'])
        
        if 'completed' in data:
            update_fields.append('completed = %s')
            values.append(data['completed'])
        
        if not update_fields:
            return jsonify({"error": "Nenhum campo para atualizar"}), 400
        
        values.append(task_id)
        query = f"UPDATE tasks SET {', '.join(update_fields)} WHERE id = %s RETURNING *"
        
        cursor.execute(query, values)
        updated_task = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({
            **dict(updated_task),
            "message": "Tarefa atualizada com sucesso"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE - Remover tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Erro na conexão com banco de dados"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = %s RETURNING id', (task_id,))
        deleted = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        
        if deleted is None:
            return jsonify({"error": "Tarefa não encontrada"}), 404
        
        return jsonify({"message": "Tarefa removida com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Tratamento de erros
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Rota não encontrada"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    print("🚀 Iniciando API To-Do List...")
    print(f"🐳 Container: {os.getenv('HOSTNAME', 'local')}")
    print(f"🗄️  Banco: {DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}")
    
    # Inicializar banco de dados
    init_db()
    
    # Iniciar servidor
    port = int(os.getenv('PORT', 8000))
    print(f"✨ Servidor rodando na porta {port}")
    print(f"📅 {datetime.now().isoformat()}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
