# Exercício 4: Persistência de Dados com Docker Volumes

## 🎯 Objetivos
- Entender volumes Docker
- Implementar persistência de dados
- Trabalhar com bind mounts
- Compartilhar dados entre containers
- Fazer backup e restore

## 📁 Estrutura do Projeto
```
exercicio-4/
├── docker-compose.yml
├── app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── data/
│   └── uploads/
├── backup/
└── README.md
```

## 🛠️ O que foi implementado

### Aplicação de Upload de Arquivos
- API para fazer upload de arquivos
- Armazenamento persistente
- Listagem de arquivos
- Download de arquivos
- Exclusão de arquivos

### Três Tipos de Volumes

#### 1. Named Volume (Volume Nomeado)
```yaml
volumes:
  - app-data:/app/data
```
- Gerenciado pelo Docker
- Melhor para dados de produção
- Fácil backup e migração

#### 2. Bind Mount (Montagem de Diretório)
```yaml
volumes:
  - ./uploads:/app/uploads
```
- Mapeia diretório do host
- Útil para desenvolvimento
- Acesso direto aos arquivos

#### 3. Anonymous Volume (Volume Anônimo)
```yaml
volumes:
  - /app/logs
```
- Criado automaticamente
- Temporário
- Usado para dados efêmeros

## 🚀 Como Executar

### Passo 1: Navegar até o diretório
```bash
cd exercicio-4
```

### Passo 2: Criar diretórios necessários
```bash
mkdir -p data/uploads backup
```

### Passo 3: Iniciar a aplicação
```bash
docker-compose up -d
```

### Passo 4: Verificar volumes criados
```bash
docker volume ls
```

## 🌐 Endpoints da API

### GET /
Informações da API

### GET /health
Status e informações de armazenamento

### GET /files
Lista todos os arquivos
```json
{
  "files": [
    {
      "name": "documento.pdf",
      "size": 1024000,
      "created": "2025-11-05T10:00:00",
      "path": "/uploads/documento.pdf"
    }
  ],
  "total": 1,
  "total_size": 1024000
}
```

### POST /upload
Faz upload de arquivo
```bash
curl -X POST -F "file=@documento.pdf" http://localhost:9000/upload
```

### GET /download/:filename
Faz download de arquivo
```bash
curl -O http://localhost:9000/download/documento.pdf
```

### DELETE /files/:filename
Remove arquivo
```bash
curl -X DELETE http://localhost:9000/files/documento.pdf
```

## 🧪 Testando Persistência

### Teste 1: Upload e Verificação

```powershell
# Criar arquivo de teste
"Conteúdo de teste" | Out-File -FilePath test.txt

# Fazer upload
curl -X POST -F "file=@test.txt" http://localhost:9000/upload

# Listar arquivos
curl http://localhost:9000/files

# Verificar diretório local
ls data/uploads
```

### Teste 2: Persistência após Restart

```bash
# Parar container
docker-compose stop

# Iniciar novamente
docker-compose start

# Verificar se arquivos ainda existem
curl http://localhost:9000/files
```

### Teste 3: Persistência após Recreação

```bash
# Remover container (mantém volume)
docker-compose down

# Recriar container
docker-compose up -d

# Arquivos devem persistir
curl http://localhost:9000/files
```

### Teste 4: Perda de Dados (sem volume)

```bash
# Remover tudo incluindo volumes
docker-compose down -v

# Recriar
docker-compose up -d

# Arquivos foram perdidos
curl http://localhost:9000/files
```

## 📦 Gerenciamento de Volumes

### Listar Volumes

```bash
# Todos os volumes
docker volume ls

# Volumes do projeto
docker volume ls | findstr exercicio-4
```

### Inspecionar Volume

```bash
# Ver detalhes do volume
docker volume inspect exercicio-4_app-data

# Ver localização no host
docker volume inspect exercicio-4_app-data --format '{{ .Mountpoint }}'
```

### Criar Volume Manualmente

```bash
# Criar volume
docker volume create meu-volume

# Usar em container
docker run -v meu-volume:/data alpine sh
```

### Remover Volumes

```bash
# Remover volume específico
docker volume rm exercicio-4_app-data

# Remover volumes não usados
docker volume prune

# Forçar remoção
docker volume rm -f exercicio-4_app-data
```

## 💾 Backup e Restore

### Backup de Volume

#### Método 1: Usando tar

```bash
# Criar backup
docker run --rm `
  -v exercicio-4_app-data:/data `
  -v ${PWD}/backup:/backup `
  alpine tar czf /backup/app-data-backup.tar.gz -C /data .

# Verificar backup
ls backup/
```

#### Método 2: Copiando arquivos

```bash
# Criar container temporário
docker run -d --name temp -v exercicio-4_app-data:/data alpine sleep 3600

# Copiar dados
docker cp temp:/data ./backup/data-copy

# Remover container temporário
docker rm -f temp
```

### Restore de Volume

```bash
# Criar novo volume
docker volume create exercicio-4_app-data-restore

# Restaurar dados
docker run --rm `
  -v exercicio-4_app-data-restore:/data `
  -v ${PWD}/backup:/backup `
  alpine tar xzf /backup/app-data-backup.tar.gz -C /data
```

### Script de Backup Automatizado

Criar arquivo `backup.ps1`:

```powershell
# backup.ps1
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupName = "app-data-backup-$timestamp.tar.gz"

Write-Host "Criando backup: $backupName"

docker run --rm `
  -v exercicio-4_app-data:/data `
  -v ${PWD}/backup:/backup `
  alpine tar czf /backup/$backupName -C /data .

Write-Host "Backup criado com sucesso!"
```

Executar:
```powershell
.\backup.ps1
```

## 🎓 Conceitos Aprendidos

### 1. Tipos de Volumes

**Named Volumes:**
- ✅ Gerenciados pelo Docker
- ✅ Fácil backup
- ✅ Portáveis entre hosts
- ❌ Localização abstrata

**Bind Mounts:**
- ✅ Acesso direto
- ✅ Útil para desenvolvimento
- ✅ Edição em tempo real
- ❌ Dependente do sistema de arquivos do host

**Anonymous Volumes:**
- ✅ Criação automática
- ✅ Útil para dados temporários
- ❌ Difícil gerenciamento
- ❌ Removidos facilmente

### 2. Ciclo de Vida dos Volumes

```
Criar → Usar → Backup → Restore → Remover
```

### 3. Persistência de Dados

- Dados sobrevivem à remoção de containers
- Compartilhamento entre containers
- Isolamento de dados
- Performance otimizada

### 4. Boas Práticas

✅ Use named volumes para produção
✅ Use bind mounts para desenvolvimento
✅ Faça backups regulares
✅ Nomeie volumes descritivamente
✅ Documente estrutura de volumes
❌ Não armazene dados sensíveis sem criptografia
❌ Não use volumes anônimos para dados importantes

## 📊 Comparação de Volumes

| Característica | Named Volume | Bind Mount | Anonymous |
|----------------|--------------|------------|-----------|
| Gerenciamento | Docker | Manual | Docker |
| Portabilidade | Alta | Baixa | Média |
| Performance | Alta | Variável | Alta |
| Backup | Fácil | Manual | Difícil |
| Dev/Prod | Prod | Dev | Temp |
| Compartilhamento | Sim | Sim | Não |

## 🔧 Troubleshooting

### Volume não encontrado

```bash
# Verificar se existe
docker volume ls | findstr app-data

# Recriar volume
docker volume create exercicio-4_app-data
```

### Permissões negadas

```bash
# Verificar permissões no bind mount
ls -la data/uploads

# Ajustar permissões (Linux/Mac)
chmod -R 777 data/uploads
```

### Espaço em disco

```bash
# Ver uso de disco dos volumes
docker system df -v

# Limpar volumes não usados
docker volume prune
```

### Dados não persistem

```bash
# Verificar configuração do docker-compose.yml
docker-compose config

# Verificar se volume está montado
docker inspect nome-container | grep -A 10 Mounts
```

## 📚 Próximos Passos

Após completar este exercício, explore:
- Docker Swarm para orquestração
- Kubernetes para produção
- Docker Registry para compartilhar imagens
- CI/CD com Docker

## 🎯 Desafios Extras

1. **Encryption**: Criptografar volume
2. **NFS**: Usar volume NFS
3. **S3**: Backup para AWS S3
4. **Monitoring**: Monitorar uso de disco
5. **Replication**: Replicar volume entre hosts
6. **Compression**: Comprimir dados automaticamente
7. **Cleanup**: Script de limpeza automática

### Exemplo: Volume com NFS

```yaml
volumes:
  nfs-volume:
    driver: local
    driver_opts:
      type: nfs
      o: addr=192.168.1.100,rw
      device: ":/path/to/share"
```

## 📖 Recursos

- [Docker Volumes Documentation](https://docs.docker.com/storage/volumes/)
- [Docker Storage Drivers](https://docs.docker.com/storage/storagedriver/)
- [Backup Best Practices](https://docs.docker.com/storage/volumes/#backup-restore-or-migrate-data-volumes)
- [Volume Plugins](https://docs.docker.com/engine/extend/plugins_volume/)

## 💡 Dicas Importantes

1. **Sempre use volumes para dados importantes**
2. **Teste backups regularmente**
3. **Documente estrutura de dados**
4. **Monitore uso de espaço**
5. **Use .dockerignore para build mount**
6. **Considere segurança em bind mounts**
7. **Automatize backups em produção**
