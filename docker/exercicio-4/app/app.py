from flask import Flask, request, jsonify, send_file
import os
from datetime import datetime
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)

# Configurações
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', '/app/uploads')
DATA_FOLDER = os.getenv('DATA_FOLDER', '/app/data')
MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 10485760))  # 10MB
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx', 'zip'}

# Criar diretórios se não existirem
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs('/app/logs', exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_info(filepath):
    """Retorna informações sobre um arquivo"""
    stats = os.stat(filepath)
    return {
        'name': os.path.basename(filepath),
        'size': stats.st_size,
        'size_human': format_bytes(stats.st_size),
        'created': datetime.fromtimestamp(stats.st_ctime).isoformat(),
        'modified': datetime.fromtimestamp(stats.st_mtime).isoformat()
    }

def format_bytes(size):
    """Formata bytes em formato legível"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def log_action(action, details):
    """Registra ação em log"""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'action': action,
        'details': details
    }
    log_file = f'/app/logs/actions_{datetime.now().strftime("%Y-%m-%d")}.log'
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry) + '\n')

# Rota principal
@app.route('/')
def home():
    return jsonify({
        "message": "File Storage API com Docker Volumes",
        "version": "1.0.0",
        "exercise": "Exercício 4",
        "author": "Gabriel CH",
        "features": [
            "Upload de arquivos",
            "Persistência com volumes",
            "Bind mounts",
            "Backup e restore"
        ],
        "endpoints": {
            "GET /": "Informações da API",
            "GET /health": "Status e informações de armazenamento",
            "GET /files": "Lista todos os arquivos",
            "POST /upload": "Faz upload de arquivo",
            "GET /download/<filename>": "Faz download de arquivo",
            "DELETE /files/<filename>": "Remove arquivo",
            "GET /stats": "Estatísticas de armazenamento"
        }
    })

# Health check
@app.route('/health')
def health():
    try:
        # Verificar espaço em disco
        stat = os.statvfs(UPLOAD_FOLDER)
        free_space = stat.f_bavail * stat.f_frsize
        total_space = stat.f_blocks * stat.f_frsize
        used_space = total_space - free_space
        
        # Contar arquivos
        files = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
        
        return jsonify({
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "container": os.getenv('HOSTNAME', 'local'),
            "storage": {
                "upload_folder": UPLOAD_FOLDER,
                "data_folder": DATA_FOLDER,
                "total_files": len(files),
                "disk": {
                    "total": format_bytes(total_space),
                    "used": format_bytes(used_space),
                    "free": format_bytes(free_space),
                    "usage_percent": f"{(used_space / total_space * 100):.2f}%"
                }
            }
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 500

# Listar arquivos
@app.route('/files', methods=['GET'])
def list_files():
    try:
        files = []
        total_size = 0
        
        for filename in os.listdir(UPLOAD_FOLDER):
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            if os.path.isfile(filepath):
                info = get_file_info(filepath)
                files.append(info)
                total_size += info['size']
        
        # Ordenar por data de criação (mais recente primeiro)
        files.sort(key=lambda x: x['created'], reverse=True)
        
        return jsonify({
            "files": files,
            "total": len(files),
            "total_size": total_size,
            "total_size_human": format_bytes(total_size)
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Upload de arquivo
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Verificar se arquivo foi enviado
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({"error": "Nome de arquivo vazio"}), 400
        
        if not allowed_file(file.filename):
            return jsonify({
                "error": "Tipo de arquivo não permitido",
                "allowed": list(ALLOWED_EXTENSIONS)
            }), 400
        
        # Salvar arquivo
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        # Verificar se arquivo já existe
        if os.path.exists(filepath):
            # Adicionar timestamp ao nome
            name, ext = os.path.splitext(filename)
            filename = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        file.save(filepath)
        
        # Registrar ação
        log_action('upload', {'filename': filename})
        
        # Salvar metadados no volume de dados
        metadata_file = os.path.join(DATA_FOLDER, f"{filename}.meta.json")
        metadata = {
            'original_name': file.filename,
            'saved_name': filename,
            'upload_time': datetime.now().isoformat(),
            'size': os.path.getsize(filepath),
            'content_type': file.content_type
        }
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        return jsonify({
            "message": "Arquivo enviado com sucesso",
            "file": get_file_info(filepath)
        }), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Download de arquivo
@app.route('/download/<filename>')
def download_file(filename):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, secure_filename(filename))
        
        if not os.path.exists(filepath):
            return jsonify({"error": "Arquivo não encontrado"}), 404
        
        log_action('download', {'filename': filename})
        
        return send_file(filepath, as_attachment=True)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Remover arquivo
@app.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, secure_filename(filename))
        
        if not os.path.exists(filepath):
            return jsonify({"error": "Arquivo não encontrado"}), 404
        
        # Remover arquivo
        os.remove(filepath)
        
        # Remover metadados
        metadata_file = os.path.join(DATA_FOLDER, f"{filename}.meta.json")
        if os.path.exists(metadata_file):
            os.remove(metadata_file)
        
        log_action('delete', {'filename': filename})
        
        return jsonify({"message": "Arquivo removido com sucesso"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Estatísticas
@app.route('/stats')
def stats():
    try:
        files = os.listdir(UPLOAD_FOLDER)
        total_files = len([f for f in files if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))])
        
        # Calcular tamanho total
        total_size = sum(os.path.getsize(os.path.join(UPLOAD_FOLDER, f)) 
                        for f in files if os.path.isfile(os.path.join(UPLOAD_FOLDER, f)))
        
        # Contar por extensão
        extensions = {}
        for f in files:
            if os.path.isfile(os.path.join(UPLOAD_FOLDER, f)):
                ext = os.path.splitext(f)[1].lower()
                extensions[ext] = extensions.get(ext, 0) + 1
        
        return jsonify({
            "total_files": total_files,
            "total_size": total_size,
            "total_size_human": format_bytes(total_size),
            "by_extension": extensions,
            "folders": {
                "uploads": UPLOAD_FOLDER,
                "data": DATA_FOLDER,
                "logs": "/app/logs"
            }
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Tratamento de erros
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Rota não encontrada"}), 404

@app.errorhandler(413)
def too_large(error):
    return jsonify({"error": "Arquivo muito grande"}), 413

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Erro interno do servidor"}), 500

if __name__ == '__main__':
    print("🚀 File Storage API iniciada")
    print(f"📁 Upload folder: {UPLOAD_FOLDER}")
    print(f"📁 Data folder: {DATA_FOLDER}")
    print(f"📦 Max file size: {format_bytes(MAX_FILE_SIZE)}")
    print(f"🐳 Container: {os.getenv('HOSTNAME', 'local')}")
    print(f"📅 {datetime.now().isoformat()}")
    
    app.run(host='0.0.0.0', port=9000, debug=False)
