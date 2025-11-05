# Exercícios Docker - Orion Bootcamp

Repositório com exercícios práticos de Docker do bootcamp New Rizon.

## Estrutura do Projeto

- **main**: Branch principal com documentação
- **develop**: Branch de desenvolvimento
- **exercicio-1**: Hello World com Docker e Node.js
- **exercicio-2**: API REST com Python Flask
- **exercicio-3**: Aplicação Multi-container com Docker Compose
- **exercicio-4**: Persistência de dados com Docker Volumes

## Exercícios

### Exercício 1: Hello World com Docker
Branch: `exercicio-1`

Aplicação Node.js simples containerizada.

Objetivos:
- Criar um Dockerfile básico
- Construir uma imagem Docker
- Executar um container

### Exercício 2: API REST com Python Flask
Branch: `exercicio-2`

API REST simples usando Flask.

Objetivos:
- Criar aplicação Python com dependências
- Configurar Dockerfile para Python
- Expor portas corretamente

### Exercício 3: Multi-container com Docker Compose
Branch: `exercicio-3`

Aplicação web conectada a banco de dados.

Objetivos:
- Configurar Docker Compose
- Conectar múltiplos containers
- Gerenciar redes Docker

### Exercício 4: Persistência com Volumes
Branch: `exercicio-4`

Persistência de dados usando volumes Docker.

Objetivos:
- Criar e gerenciar volumes
- Mapear diretórios
- Garantir persistência de dados

## Pré-requisitos

- Docker Desktop instalado
- Git instalado
- Terminal/PowerShell
- Editor de código (VS Code recomendado)

## Como Usar Este Repositório

### 1. Clone o repositório
```bash
git clone https://github.com/GaabrielCH/exercicios-orion.git
cd exercicios-orion
```

### 2. Navegue entre os exercícios
```bash
# Listar todas as branches
git branch -a

# Mudar para um exercício específico
git checkout exercicio-1
```

### 3. Execute os exercícios
Cada branch contém instruções específicas no README.md local.

## Workflow Git e Pull Requests

### Estrutura de Branches

```
main (produção)
  └── develop (desenvolvimento)
       ├── exercicio-1 (feature)
       ├── exercicio-2 (feature)
       ├── exercicio-3 (feature)
       └── exercicio-4 (feature)
```

### Como Trabalhar com Branches

#### Criar uma nova branch
```bash
# A partir da develop
git checkout develop
git checkout -b minha-feature

# Fazer alterações
git add .
git commit -m "Descrição das alterações"
git push origin minha-feature
```

#### Atualizar sua branch com develop
```bash
git checkout minha-feature
git merge develop
# ou
git rebase develop
```

### Como Fazer Pull Requests

#### Método 1: Via GitHub Web
1. Acesse o repositório no GitHub
2. Clique em "Pull requests" → "New pull request"
3. Selecione:
   - **Base branch**: `develop` (destino)
   - **Compare branch**: `exercicio-1` (origem)
4. Preencha o título e descrição
5. Clique em "Create pull request"

#### Método 2: Via GitHub CLI
```bash
# Instalar GitHub CLI: https://cli.github.com/

# Fazer login
gh auth login

# Criar PR
gh pr create --base develop --head exercicio-1 --title "Exercício 1: Hello World Docker" --body "Implementação do exercício 1"
```

#### Método 3: Via VS Code
1. Instale a extensão "GitHub Pull Requests and Issues"
2. Clique no ícone do GitHub na barra lateral
3. Clique em "Create Pull Request"
4. Preencha os campos e crie

### Template de Pull Request

Ao criar um PR, use este template:

```markdown
## 📝 Descrição
Breve descrição do que foi implementado

## 🎯 Exercício
- [ ] Exercício 1
- [ ] Exercício 2
- [ ] Exercício 3
- [ ] Exercício 4

## ✅ Checklist
- [ ] Código testado localmente
- [ ] Dockerfile funcional
- [ ] README atualizado
- [ ] Comandos documentados

## 🧪 Como Testar
```bash
docker build -t exercicio .
docker run -p 3000:3000 exercicio
```

## 📸 Screenshots
(Se aplicável)
```

### Revisar e Aprovar Pull Requests

#### Como Revisor:
1. Acesse o PR no GitHub
2. Vá para "Files changed"
3. Revise o código linha por linha
4. Adicione comentários se necessário
5. Clique em "Review changes"
6. Escolha: Approve, Request changes, ou Comment
7. Submit review

#### Mergear o Pull Request:
```bash
# Método 1: Squash and merge (recomendado)
# - Combina todos os commits em um
# - Mantém histórico limpo

# Método 2: Rebase and merge
# - Mantém commits individuais
# - Reaplica sobre a base

# Método 3: Merge commit
# - Cria commit de merge
# - Preserva todo histórico
```

### Boas Práticas

1. **Commits Pequenos e Frequentes**
   ```bash
   git commit -m "feat: adiciona Dockerfile"
   git commit -m "docs: atualiza README"
   ```

2. **Mensagens de Commit Convencionais**
   - `feat:` nova funcionalidade
   - `fix:` correção de bug
   - `docs:` documentação
   - `refactor:` refatoração
   - `test:` testes
   - `chore:` tarefas de manutenção

3. **Mantenha Branches Atualizadas**
   ```bash
   git fetch origin
   git merge origin/develop
   ```

4. **Resolva Conflitos Localmente**
   ```bash
   git checkout exercicio-1
   git merge develop
   # Resolver conflitos
   git add .
   git commit
   git push
   ```

## Comandos Docker Úteis

### Imagens
```bash
# Construir imagem
docker build -t nome-imagem .

# Listar imagens
docker images

# Remover imagem
docker rmi nome-imagem
```

### Containers
```bash
# Executar container
docker run -d -p 3000:3000 --name meu-container nome-imagem

# Listar containers rodando
docker ps

# Listar todos containers
docker ps -a

# Parar container
docker stop meu-container

# Remover container
docker rm meu-container

# Ver logs
docker logs meu-container

# Acessar terminal do container
docker exec -it meu-container sh
```

### Docker Compose
```bash
# Iniciar serviços
docker-compose up -d

# Parar serviços
docker-compose down

# Ver logs
docker-compose logs -f

# Reconstruir e iniciar
docker-compose up -d --build
```

### Limpeza
```bash
# Remover containers parados
docker container prune

# Remover imagens não usadas
docker image prune

# Remover tudo não usado
docker system prune -a
```

## Recursos Adicionais

- [Documentação Oficial Docker](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Guia Git](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)

## Autor

Gabriel CH - Orion Bootcamp - New Rizon

## Licença

Este projeto é para fins educacionais.
