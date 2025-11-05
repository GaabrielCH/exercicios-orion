# Usa imagem oficial do Node.js (versão Alpine para ser mais leve)
FROM node:18-alpine

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências
COPY package*.json ./

# Instala as dependências
RUN npm install --production

# Copia o código da aplicação
COPY . .

# Expõe a porta que a aplicação usa
EXPOSE 3000

# Define o comando para iniciar a aplicação
CMD ["node", "app.js"]
