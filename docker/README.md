# Exercícios Docker

Esta pasta contém 4 exercícios práticos de Docker, organizados de forma progressiva.

## IMPORTANTE: Antes de Começar

**Certifique-se de que o Docker Desktop está rodando!**

1. Abra o Docker Desktop
2. Aguarde até o ícone ficar verde
3. Teste com: `docker --version`

Se o Docker não estiver instalado, baixe em: https://www.docker.com/products/docker-desktop

## Estrutura dos Exercícios

```
docker/
├── exercicio-1/     # Hello World com Node.js
├── exercicio-2/     # API REST com Python Flask
├── exercicio-3/     # Multi-container com Docker Compose
└── exercicio-4/     # Persistência com Docker Volumes
```

## Exercícios

### Exercício 1: Hello World com Docker
Conceitos: Dockerfile, Build, Run, Container básico

Aplicação Node.js simples containerizada.

Branch: `exercicio-1`

```bash
cd docker/exercicio-1
docker-compose up -d
```

Acesse: http://localhost:3000

Para parar:
```bash
docker-compose down
```

---

### Exercício 2: API REST com Python Flask
Conceitos: API REST, Python em containers, Gerenciamento de dependências

API REST completa com operações CRUD.

Branch: `exercicio-2`

```bash
cd docker/exercicio-2
docker-compose up -d
```

Acesse: http://localhost:5000

Para parar:
```bash
docker-compose down
```

---

### Exercício 3: Multi-container com Docker Compose
Conceitos: Docker Compose, Redes, Banco de dados, Orquestração

Aplicação To-Do List com Flask + PostgreSQL + Adminer.

Branch: `exercicio-3`

```bash
cd docker/exercicio-3
docker-compose up -d
```

Acessos:
- API: http://localhost:8000
- Adminer: http://localhost:8080

Para parar:
```bash
docker-compose down
```

---

### Exercício 4: Persistência com Docker Volumes
Conceitos: Volumes, Persistência, Backup, Named/Bind mounts

Upload de arquivos com diferentes tipos de volumes.

Branch: `exercicio-4`

```bash
cd docker/exercicio-4
docker-compose up -d
```

Acesse: http://localhost:9000

Para parar:
```bash
docker-compose down
```

---

## Como Usar Este Projeto

### 1. Clone o Repositório
```bash
git clone https://github.com/GaabrielCH/exercicios-orion.git
cd exercicios-orion
```

### 2. Navegue pelos Exercícios

Opção A: Trabalhar na branch main (todos os exercícios juntos)
```bash
cd docker/exercicio-1
# Execute o exercício
```

Opção B: Trabalhar por branches (exercícios isolados)
```bash
# Ver todas as branches
git branch -a

# Mudar para branch do exercício 1
git checkout exercicio-1

# Ver o código do exercício
cd docker/exercicio-1
```

### 3. Execute os Exercícios

Cada exercício tem seu próprio README.md com instruções detalhadas.

```bash
# Exemplo: Executar exercício 1
cd docker/exercicio-1
cat README.md  # Ler instruções
docker build -t ex1 .
docker run -p 3000:3000 ex1
```

## Ordem Recomendada

1. Exercício 1: Fundamentos de containers
2. Exercício 2: Aplicações reais
3. Exercício 3: Múltiplos containers
4. Exercício 4: Persistência de dados

Siga esta ordem para melhor aproveitamento.

## Pré-requisitos

- Docker Desktop instalado
- Git instalado
- Terminal/PowerShell
- Editor de código
- Conhecimento básico de terminal

## Comparação dos Exercícios

| Exercício | Dificuldade | Tempo | Conceitos |
|-----------|-------------|-------|-----------|
| 1 | Iniciante | 30min | Dockerfile, Build, Run |
| 2 | Iniciante | 45min | API, Dependencies |
| 3 | Intermediário | 60min | Compose, Networks, DB |
| 4 | Intermediário | 60min | Volumes, Persistence |

## O Que Você Vai Aprender

### Exercício 1
- Criar Dockerfiles
- Construir imagens
- Executar containers
- Port mapping
- Comandos básicos

### Exercício 2
- Containerizar aplicações Python
- Gerenciar dependências
- Variáveis de ambiente
- APIs em containers

### Exercício 3
- Docker Compose
- Multi-container
- Redes Docker
- Banco de dados
- Orquestração

### Exercício 4
- Named volumes
- Bind mounts
- Persistência
- Backup e restore
- Gerenciamento de dados

## Comandos Úteis

### Containers
```bash
# Listar containers rodando
docker ps

# Listar todos
docker ps -a

# Parar container
docker stop <container>

# Remover container
docker rm <container>

# Ver logs
docker logs <container>

# Acessar terminal
docker exec -it <container> sh
```

### Imagens
```bash
# Listar imagens
docker images

# Construir imagem
docker build -t <nome> .

# Remover imagem
docker rmi <nome>

# Baixar imagem
docker pull <nome>
```

### Docker Compose
```bash
# Iniciar serviços
docker-compose up -d

# Parar serviços
docker-compose down

# Ver logs
docker-compose logs -f

# Reconstruir
docker-compose up -d --build
```

### Volumes
```bash
# Listar volumes
docker volume ls

# Criar volume
docker volume create <nome>

# Remover volume
docker volume rm <nome>

# Limpar volumes não usados
docker volume prune
```

### Limpeza
```bash
# Remover containers parados
docker container prune

# Remover imagens não usadas
docker image prune

# Limpeza geral
docker system prune -a
```

## Recursos Adicionais

### Documentação
- [Docker Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Tutoriais
- [Docker Getting Started](https://docs.docker.com/get-started/)
- [Play with Docker](https://labs.play-with-docker.com/)

### Comunidade
- [Docker Community Forums](https://forums.docker.com/)
- [Stack Overflow - Docker](https://stackoverflow.com/questions/tagged/docker)

## Comandos Rápidos

### Para todos os exercícios

Iniciar:
```bash
docker-compose up -d
```

Ver logs:
```bash
docker-compose logs -f
```

Parar:
```bash
docker-compose down
```

Reconstruir e iniciar:
```bash
docker-compose up -d --build
```

Ver containers rodando:
```bash
docker ps
```

## Troubleshooting

### Docker Desktop não inicia
- Verifique se WSL 2 está instalado (Windows)
- Verifique requisitos do sistema
- Reinicie o computador

### Porta já em uso
```bash
# Verificar o que está usando a porta
netstat -ano | findstr :3000

# Parar o container que está usando
docker-compose down
```

### Erro ao construir
```bash
# Reconstruir sem cache
docker-compose build --no-cache
docker-compose up -d
```

## Próximos Passos

Após completar todos os exercícios:

1. Explore Docker Swarm
2. Aprenda Kubernetes
3. Implemente CI/CD
4. Estude segurança em containers
5. Pratique com projetos reais

## Sobre

Exercícios criados para o Orion Bootcamp - New Rizon

Objetivo: Ensinar Docker de forma prática e progressiva.

## Licença

Projeto educacional - Uso livre para aprendizado
