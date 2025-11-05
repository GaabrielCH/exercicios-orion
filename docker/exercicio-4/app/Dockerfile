# Usa imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY app.py .

# Cria diretórios necessários
RUN mkdir -p /app/uploads /app/data /app/logs

# Expõe a porta 9000
EXPOSE 9000

# Define variável de ambiente para Python
ENV PYTHONUNBUFFERED=1

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
