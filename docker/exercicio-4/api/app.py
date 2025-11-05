from flask import Flask, request, jsonify
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASS', 'postgres123'),
        database=os.getenv('DB_NAME', 'appdb'),
        cursor_factory=RealDictCursor
    )

def init_db():
    max_retries = 10
    for i in range(max_retries):
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    price DECIMAL(10, 2) NOT NULL,
                    stock INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            cur.close()
            conn.close()
            print("Database initialized successfully")
            return
        except psycopg2.OperationalError as e:
            if i < max_retries - 1:
                print(f"Database not ready, retrying... ({i+1}/{max_retries})")
                time.sleep(3)
            else:
                print(f"Failed to connect to database: {e}")
                raise

@app.route('/')
def home():
    return jsonify({
        "message": "Stack Completa - API, Database e Adminer",
        "version": "1.0.0",
        "exercise": "Desafio Extra",
        "author": "Gabriel CH",
        "services": ["API (Flask)", "Database (PostgreSQL)", "Adminer"],
        "endpoints": {
            "GET /": "Informações da API",
            "GET /health": "Status da aplicação e database",
            "GET /products": "Lista todos os produtos",
            "GET /products/<id>": "Busca produto por ID",
            "POST /products": "Cria novo produto",
            "PUT /products/<id>": "Atualiza produto",
            "DELETE /products/<id>": "Remove produto"
        },
        "adminer": "http://localhost:8080"
    })

@app.route('/health')
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return jsonify({
            "status": "ok",
            "database": "connected",
            "timestamp": datetime.now().isoformat(),
            "container": os.getenv('HOSTNAME', 'local')
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "database": "disconnected",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route('/products', methods=['GET'])
def get_products():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM products ORDER BY id')
        products = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(products), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM products WHERE id = %s', (product_id,))
        product = cur.fetchone()
        cur.close()
        conn.close()
        
        if product is None:
            return jsonify({"error": "Produto não encontrado"}), 404
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Nome e preço são obrigatórios"}), 400
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO products (name, description, price, stock) VALUES (%s, %s, %s, %s) RETURNING *',
            (data['name'], data.get('description', ''), data['price'], data.get('stock', 0))
        )
        new_product = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            **new_product,
            "message": "Produto criado com sucesso"
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Dados não fornecidos"}), 400
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM products WHERE id = %s', (product_id,))
        if cur.fetchone() is None:
            cur.close()
            conn.close()
            return jsonify({"error": "Produto não encontrado"}), 404
        
        updates = []
        params = []
        
        if 'name' in data:
            updates.append("name = %s")
            params.append(data['name'])
        
        if 'description' in data:
            updates.append("description = %s")
            params.append(data['description'])
        
        if 'price' in data:
            updates.append("price = %s")
            params.append(data['price'])
        
        if 'stock' in data:
            updates.append("stock = %s")
            params.append(data['stock'])
        
        if not updates:
            cur.close()
            conn.close()
            return jsonify({"error": "Nenhum campo para atualizar"}), 400
        
        params.append(product_id)
        query = f"UPDATE products SET {', '.join(updates)} WHERE id = %s RETURNING *"
        
        cur.execute(query, params)
        updated_product = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({
            **updated_product,
            "message": "Produto atualizado com sucesso"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM products WHERE id = %s RETURNING *', (product_id,))
        product = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        if product is None:
            return jsonify({"error": "Produto não encontrado"}), 404
        
        return jsonify({"message": "Produto removido com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Rota não encontrada"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    print("Iniciando Stack Completa - Desafio Extra")
    print(f"Container: {os.getenv('HOSTNAME', 'local')}")
    print(f"Database: {os.getenv('DB_HOST')}:{os.getenv('DB_NAME')}")
    
    init_db()
    
    port = int(os.getenv('PORT', 5000))
    print(f"API rodando na porta {port}")
    print(f"{datetime.now().isoformat()}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
