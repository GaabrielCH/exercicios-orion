# Guia Completo: Git Workflow e Pull Requests

## 📋 Índice
1. [Entendendo Branches](#entendendo-branches)
2. [Workflow GitFlow](#workflow-gitflow)
3. [Como Criar Pull Requests](#como-criar-pull-requests)
4. [Review de Código](#review-de-código)
5. [Resolvendo Conflitos](#resolvendo-conflitos)
6. [Comandos Essenciais](#comandos-essenciais)

---

## 🌿 Entendendo Branches

### O que são Branches?
Branches (ramos) são linhas paralelas de desenvolvimento. Permitem trabalhar em features isoladas sem afetar o código principal.

### Estrutura Hierárquica
```
main (produção - código estável)
  ├── develop (desenvolvimento - integração)
  │    ├── exercicio-1 (feature específica)
  │    ├── exercicio-2 (feature específica)
  │    ├── exercicio-3 (feature específica)
  │    └── exercicio-4 (feature específica)
```

### Tipos de Branches

#### 1. Branch Principal (main/master)
- **Propósito**: Código em produção
- **Proteção**: Sempre estável e funcional
- **Acesso**: Apenas via Pull Requests aprovados

#### 2. Branch de Desenvolvimento (develop)
- **Propósito**: Integração de features
- **Proteção**: Código testado, mas pode ter instabilidades
- **Acesso**: Via Pull Requests de features

#### 3. Branches de Features (exercicio-1, exercicio-2, etc)
- **Propósito**: Desenvolvimento de funcionalidades específicas
- **Proteção**: Ambiente de experimentação
- **Acesso**: Direto pelo desenvolvedor

---

## 🔄 Workflow GitFlow

### Passo 1: Configuração Inicial

```powershell
# Clone o repositório (se ainda não fez)
git clone https://github.com/GaabrielCH/exercicios-orion.git
cd exercicios-orion

# Verifique a branch atual
git branch

# Liste todas as branches (locais e remotas)
git branch -a

# Configure seu usuário Git (se necessário)
git config user.name "Seu Nome"
git config user.email "seu.email@exemplo.com"
```

### Passo 2: Criar Branch de Desenvolvimento

```powershell
# Certifique-se de estar na main
git checkout main

# Crie a branch develop
git checkout -b develop

# Envie para o repositório remoto
git push -u origin develop
```

### Passo 3: Criar Branch de Feature

```powershell
# A partir da develop, crie uma branch de feature
git checkout develop
git checkout -b exercicio-1

# Ou em um único comando:
git checkout -b exercicio-1 develop
```

### Passo 4: Trabalhar na Feature

```powershell
# Faça suas alterações nos arquivos
# ... edite, crie, modifique arquivos ...

# Veja o status das alterações
git status

# Adicione os arquivos modificados
git add .
# Ou adicione arquivos específicos:
git add arquivo1.txt arquivo2.txt

# Faça o commit
git commit -m "feat: implementa Dockerfile para exercício 1"

# Envie para o repositório remoto
git push -u origin exercicio-1
```

### Passo 5: Manter Branch Atualizada

```powershell
# Busque as últimas atualizações
git fetch origin

# Atualize sua branch develop local
git checkout develop
git pull origin develop

# Volte para sua feature e integre as mudanças
git checkout exercicio-1
git merge develop

# Ou use rebase (mantém histórico linear):
git rebase develop
```

---

## 📤 Como Criar Pull Requests

### Método 1: GitHub Web Interface (Mais Fácil)

#### Passo a Passo Detalhado:

**1. Prepare sua branch**
```powershell
# Certifique-se de que tudo está commitado
git status

# Se houver alterações, commite:
git add .
git commit -m "feat: finaliza exercício 1"

# Envie para o GitHub
git push origin exercicio-1
```

**2. Acesse o GitHub**
- Abra seu navegador
- Vá para: https://github.com/GaabrielCH/exercicios-orion

**3. Inicie o Pull Request**
- Você verá um banner amarelo: "exercicio-1 had recent pushes"
- Clique em **"Compare & pull request"**
- OU vá em: Aba **"Pull requests"** → **"New pull request"**

**4. Configure o Pull Request**

**Base e Compare:**
```
base: develop  ← (para onde o código vai)
compare: exercicio-1  ← (de onde o código vem)
```

**5. Preencha o Formulário**

**Título:** (Seja descritivo)
```
✅ Bom: "Exercício 1: Implementa Hello World com Docker e Node.js"
❌ Ruim: "exercicio 1"
```

**Descrição:** (Use o template abaixo)
```markdown
## 📝 Descrição
Implementação do primeiro exercício: aplicação Hello World usando Node.js containerizada com Docker.

## 🎯 Exercício
- [x] Exercício 1 - Hello World Docker

## ✨ O que foi implementado
- Dockerfile com Node.js
- Aplicação Express.js simples
- Configuração de porta 3000
- README com instruções de uso

## ✅ Checklist
- [x] Código testado localmente
- [x] Dockerfile funcional
- [x] README atualizado
- [x] Comandos documentados

## 🧪 Como Testar
```bash
# Construir a imagem
docker build -t exercicio-1 .

# Executar o container
docker run -p 3000:3000 exercicio-1

# Testar no navegador
# Acesse: http://localhost:3000
```

## 📸 Screenshot
![Aplicação rodando](link-para-imagem-se-houver)

## 🔗 Recursos
- [Documentação Docker](https://docs.docker.com/)
- [Express.js](https://expressjs.com/)
```

**6. Revisar Alterações**
- Clique na aba **"Files changed"**
- Revise linha por linha
- Certifique-se de que não há código indesejado

**7. Criar o Pull Request**
- Clique em **"Create pull request"**
- Aguarde revisão (se houver reviewers)

**8. Interagir com Reviewers (se houver)**
- Responda comentários
- Faça ajustes solicitados
- Envie novos commits para a mesma branch

**9. Merge (quando aprovado)**

**Opções de Merge:**

**a) Squash and Merge** ⭐ (Recomendado)
- Combina todos os commits em um único
- Mantém histórico limpo
- Use quando: múltiplos commits pequenos

**b) Rebase and Merge**
- Mantém commits individuais
- Histórico linear
- Use quando: commits bem organizados

**c) Create a Merge Commit**
- Preserva todo histórico
- Cria commit de merge
- Use quando: quer manter contexto completo

### Método 2: GitHub CLI (Linha de Comando)

```powershell
# Instalar GitHub CLI
# Download: https://cli.github.com/
# Ou via winget:
winget install --id GitHub.cli

# Fazer login
gh auth login

# Criar Pull Request
gh pr create `
  --base develop `
  --head exercicio-1 `
  --title "Exercício 1: Hello World com Docker" `
  --body "Implementação do exercício 1 com Node.js e Docker"

# Listar PRs
gh pr list

# Ver detalhes de um PR
gh pr view 1

# Fazer merge de um PR
gh pr merge 1 --squash
```

### Método 3: VS Code + Extensão GitHub

**1. Instalar Extensão**
- Abra VS Code
- Vá para Extensions (Ctrl+Shift+X)
- Procure: "GitHub Pull Requests and Issues"
- Instale

**2. Fazer Login**
- Clique no ícone do GitHub na barra lateral
- Clique em "Sign in to GitHub"
- Autorize no navegador

**3. Criar Pull Request**
- Clique no ícone do GitHub
- Seção "Pull Requests"
- Clique no botão "+" ou "Create Pull Request"
- Preencha os campos
- Clique em "Create"

---

## 👀 Review de Código

### Como Revisar um Pull Request

**1. Acesse o PR no GitHub**
```
https://github.com/GaabrielCH/exercicios-orion/pull/1
```

**2. Vá para "Files changed"**

**3. Revise o Código**
- Clique no número da linha para comentar
- Arraste para selecionar múltiplas linhas
- Adicione sugestões:

```suggestion
// Código sugerido aqui
const melhorCodigo = "assim";
```

**4. Finalize a Review**
- Clique em "Review changes"
- Escolha:
  - **Comment**: Apenas comentário
  - **Approve**: Aprovar PR ✅
  - **Request changes**: Solicitar mudanças ❌
- Clique em "Submit review"

### Checklist de Review

- [ ] O código funciona?
- [ ] Segue padrões do projeto?
- [ ] Há testes?
- [ ] A documentação está atualizada?
- [ ] Não há código duplicado?
- [ ] Variáveis têm nomes claros?
- [ ] Há comentários onde necessário?
- [ ] Não há informações sensíveis?
- [ ] O Dockerfile está otimizado?

---

## ⚔️ Resolvendo Conflitos

### O que são Conflitos?

Conflitos ocorrem quando:
- Duas branches modificam a mesma linha
- Uma branch deleta arquivo que outra modifica
- Mudanças incompatíveis

### Como Resolver

**Cenário: develop foi atualizada, sua branch tem conflitos**

```powershell
# 1. Atualize sua develop local
git checkout develop
git pull origin develop

# 2. Volte para sua feature
git checkout exercicio-1

# 3. Tente fazer merge
git merge develop

# 4. Se houver conflitos, você verá algo assim:
# Auto-merging arquivo.txt
# CONFLICT (content): Merge conflict in arquivo.txt
```

**Arquivos com conflito terão marcadores:**

```javascript
<<<<<<< HEAD (sua versão)
const mensagem = "Minha versão";
=======
const mensagem = "Versão da develop";
>>>>>>> develop
```

**Resolva manualmente:**

```javascript
// Escolha uma versão ou combine:
const mensagem = "Versão final combinada";
```

**Finalize:**

```powershell
# Marque como resolvido
git add arquivo.txt

# Complete o merge
git commit -m "merge: resolve conflitos com develop"

# Envie
git push origin exercicio-1
```

### Ferramentas de Merge

**VS Code:**
- Mostra conflitos visualmente
- Botões: "Accept Current Change" | "Accept Incoming" | "Accept Both"

**Git Mergetool:**
```powershell
git mergetool
```

---

## 🛠️ Comandos Essenciais

### Branches

```powershell
# Criar branch
git checkout -b nome-branch

# Mudar de branch
git checkout nome-branch

# Listar branches
git branch              # Locais
git branch -r           # Remotas
git branch -a           # Todas

# Deletar branch local
git branch -d nome-branch

# Deletar branch remota
git push origin --delete nome-branch

# Renomear branch
git branch -m novo-nome
```

### Commits

```powershell
# Commit simples
git commit -m "mensagem"

# Commit com descrição detalhada
git commit -m "título" -m "descrição detalhada"

# Adicionar ao último commit
git commit --amend

# Ver histórico
git log
git log --oneline
git log --graph --oneline --all
```

### Sincronização

```powershell
# Baixar atualizações
git fetch origin

# Baixar e integrar
git pull origin develop

# Enviar
git push origin exercicio-1

# Primeira vez
git push -u origin exercicio-1
```

### Desfazer Alterações

```powershell
# Descartar mudanças não commitadas
git checkout -- arquivo.txt

# Descartar todas as mudanças
git reset --hard

# Voltar commit (mantém mudanças)
git reset --soft HEAD~1

# Voltar commit (descarta mudanças)
git reset --hard HEAD~1

# Criar commit que reverte outro
git revert <commit-hash>
```

### Stash (Guardar temporariamente)

```powershell
# Guardar mudanças
git stash

# Listar stashes
git stash list

# Aplicar último stash
git stash apply

# Aplicar e remover stash
git stash pop

# Remover stash
git stash drop
```

---

## 📚 Fluxo Completo de Trabalho

### Exemplo Prático: Exercício 1

```powershell
# 1. Clone e configure
git clone https://github.com/GaabrielCH/exercicios-orion.git
cd exercicios-orion

# 2. Crie develop (se não existir)
git checkout -b develop
git push -u origin develop

# 3. Crie branch do exercício
git checkout -b exercicio-1

# 4. Trabalhe no exercício
# ... crie arquivos, edite, etc ...

# 5. Commit e push
git add .
git commit -m "feat: implementa exercício 1"
git push -u origin exercicio-1

# 6. Abra PR no GitHub
# Via web: GitHub.com → Pull Requests → New

# 7. Aguarde review e aprove

# 8. Após merge, atualize localmente
git checkout develop
git pull origin develop

# 9. Delete branch local (opcional)
git branch -d exercicio-1

# 10. Comece próximo exercício
git checkout -b exercicio-2
```

---

## 🎯 Boas Práticas

### Commits

✅ **Faça commits pequenos e frequentes**
```powershell
git commit -m "feat: adiciona Dockerfile"
git commit -m "feat: adiciona aplicação Node.js"
git commit -m "docs: atualiza README"
```

❌ **Evite commits grandes**
```powershell
git commit -m "adiciona tudo"  # Ruim!
```

### Mensagens de Commit

Use **Conventional Commits**:

```
<tipo>(<escopo>): <descrição>

feat: nova funcionalidade
fix: correção de bug
docs: documentação
style: formatação
refactor: refatoração
test: testes
chore: tarefas gerais
```

**Exemplos:**
```powershell
git commit -m "feat(docker): adiciona Dockerfile para Node.js"
git commit -m "fix(app): corrige porta da aplicação"
git commit -m "docs(readme): adiciona instruções de uso"
```

### Pull Requests

✅ **Bom PR:**
- Título descritivo
- Descrição completa
- Testes incluídos
- README atualizado
- Foco em uma funcionalidade

❌ **PR Ruim:**
- Título vago: "update"
- Sem descrição
- Múltiplas funcionalidades
- Arquivos não relacionados

### Branches

✅ **Boas práticas:**
- Nomes descritivos: `exercicio-1`, `fix-port-issue`
- Uma funcionalidade por branch
- Mantenha atualizada com develop
- Delete após merge

❌ **Evite:**
- Nomes genéricos: `test`, `temp`
- Acumular muitas mudanças
- Deixar branches abandonadas

---

## 🆘 Problemas Comuns

### "Cannot push to protected branch"

```powershell
# Solução: Use Pull Request
# Não é possível push direto na main/develop
```

### "Merge conflict"

```powershell
# Solução: Resolva conflitos manualmente
git merge develop
# Edite arquivos com conflito
git add .
git commit
```

### "Divergent branches"

```powershell
# Solução: Pull antes de push
git pull origin exercicio-1
git push origin exercicio-1
```

### "Already up to date" ao fazer merge

```powershell
# Normal! Significa que não há mudanças novas
```

---

## 🎓 Recursos de Aprendizado

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs - Pull Requests](https://docs.github.com/pt/pull-requests)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Git Branching Interactive](https://learngitbranching.js.org/)

---

**Dúvidas? Consulte este guia ou a [documentação oficial](https://docs.github.com/)!** 🚀
