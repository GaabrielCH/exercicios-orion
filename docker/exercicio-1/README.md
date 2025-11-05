# Exercício 1: Hello World com Docker e Node.js

## Objetivos
- Criar uma aplicação Node.js simples
- Containerizar usando Docker
- Expor a aplicação em uma porta
- Executar e testar o container

## Estrutura do Projeto
```
exercicio-1/
├── Dockerfile
├── package.json
├── app.js
└── README.md
```

## O que foi implementado

### 1. Aplicação Node.js (app.js)
Servidor web simples usando Express que responde com "Hello World from Docker!"

### 2. Dockerfile
- Baseado em `node:18-alpine` (imagem leve)
- Define diretório de trabalho
- Copia dependências e código
- Instala pacotes
- Expõe porta 3000
- Define comando de inicialização

### 3. package.json
- Dependência do Express
- Scripts de inicialização

## Como Executar

### Pré-requisitos
- Docker Desktop instalado e rodando
- Terminal/PowerShell

### Passo 1: Navegar até o diretório
```bash
cd exercicio-1
```

### Passo 2: Construir a imagem Docker
```bash
docker build -t exercicio-1-nodejs .
```

Explicação:
- `docker build`: Comando para construir imagem
- `-t exercicio-1-nodejs`: Nome (tag) da imagem
- `.`: Contexto de build (diretório atual)

### Passo 3: Executar o container
```bash
docker run -d -p 3000:3000 --name meu-hello-world exercicio-1-nodejs
```

Explicação:
- `docker run`: Executa um container
- `-d`: Modo detached (background)
- `-p 3000:3000`: Mapeia porta do host:container
- `--name meu-hello-world`: Nome do container
- `exercicio-1-nodejs`: Nome da imagem

### Passo 4: Testar a aplicação

No navegador:
```
http://localhost:3000
```

Ou via curl/PowerShell:
```powershell
curl http://localhost:3000
# ou
Invoke-WebRequest -Uri http://localhost:3000
```

Resposta esperada:
```json
{
  "message": "Hello World from Docker!",
  "timestamp": "2025-11-05T...",
  "container": "..."
}
```

## Comandos Úteis

### Ver logs do container
```bash
docker logs meu-hello-world
```

### Ver logs em tempo real
```bash
docker logs -f meu-hello-world
```

### Acessar o terminal do container
```bash
docker exec -it meu-hello-world sh
```

### Parar o container
```bash
docker stop meu-hello-world
```

### Iniciar o container novamente
```bash
docker start meu-hello-world
```

### Remover o container
```bash
docker rm meu-hello-world
```

### Remover a imagem
```bash
docker rmi exercicio-1-nodejs
```

### Verificar containers rodando
```bash
docker ps
```

### Verificar todos os containers
```bash
docker ps -a
```

### Verificar imagens
```bash
docker images
```

## Informações da Imagem

### Ver detalhes da imagem
```bash
docker inspect exercicio-1-nodejs
```

### Ver histórico de layers
```bash
docker history exercicio-1-nodejs
```

### Ver tamanho da imagem
```bash
docker images exercicio-1-nodejs
```

## Testando

### Teste 1: Aplicação responde
```powershell
curl http://localhost:3000
```

### Teste 2: Container está rodando
```bash
docker ps | findstr meu-hello-world
```

### Teste 3: Ver logs
```bash
docker logs meu-hello-world
```

## Conceitos Aprendidos

### 1. Dockerfile
- `FROM`: Define imagem base
- `WORKDIR`: Define diretório de trabalho
- `COPY`: Copia arquivos para a imagem
- `RUN`: Executa comandos durante o build
- `EXPOSE`: Documenta portas expostas
- `CMD`: Comando padrão ao iniciar container

### 2. Docker Build
- Processo de criação de imagens
- Layers e cache
- Contexto de build

### 3. Docker Run
- Criação e execução de containers
- Port mapping
- Modo detached vs attached

### 4. Gerenciamento de Containers
- Listar, parar, iniciar, remover
- Logs e inspeção
- Acesso ao terminal

## Troubleshooting

### Porta já em uso
```
Error: bind: address already in use
```
Solução: Use outra porta
```bash
docker run -d -p 3001:3000 --name meu-hello-world exercicio-1-nodejs
```

### Container já existe
```
Error: The container name is already in use
```
Solução: Remova o container existente
```bash
docker rm meu-hello-world
# ou force remove
docker rm -f meu-hello-world
```

### Imagem não encontrada
```
Error: No such image
```
Solução: Construa a imagem primeiro
```bash
docker build -t exercicio-1-nodejs .
```

## Próximos Passos

Após completar este exercício:
- Exercício 2: API REST com Python Flask
- Exercício 3: Multi-container com Docker Compose
- Exercício 4: Persistência com Volumes

## Desafios Extras

1. Modificar a mensagem da API
2. Adicionar mais rotas (ex: `/health`, `/about`)
3. Usar variáveis de ambiente no Dockerfile
4. Otimizar o tamanho da imagem
5. Implementar multi-stage build

## Recursos

- [Documentação Docker](https://docs.docker.com/)
- [Node.js Best Practices](https://github.com/goldbergyoni/nodebestpractices)
- [Express.js Guide](https://expressjs.com/en/starter/installing.html)
