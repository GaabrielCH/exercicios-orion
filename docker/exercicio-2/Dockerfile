# Usa imagem oficial do Python (versão slim para ser mais leve)
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY . .

# Expõe a porta que a aplicação usa
EXPOSE 5000

# Define variável de ambiente para Python
ENV PYTHONUNBUFFERED=1

# Define o comando para iniciar a aplicação
CMD ["python", "app.py"]
