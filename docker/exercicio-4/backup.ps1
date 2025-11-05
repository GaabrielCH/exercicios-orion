# Script de Backup Automatizado
# Este script cria backup do volume Docker

param(
    [string]$VolumeName = "file-storage-data",
    [string]$BackupDir = ".\backup"
)

# Criar diretório de backup se não existir
if (-not (Test-Path $BackupDir)) {
    New-Item -ItemType Directory -Path $BackupDir | Out-Null
}

# Timestamp para o arquivo
$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupFile = "backup-$timestamp.tar.gz"
$backupPath = Join-Path $BackupDir $backupFile

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "  Docker Volume Backup Script" -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Volume: $VolumeName" -ForegroundColor Yellow
Write-Host "Backup: $backupFile" -ForegroundColor Yellow
Write-Host ""

# Verificar se volume existe
$volumeExists = docker volume ls --format "{{.Name}}" | Select-String -Pattern "^$VolumeName$"

if (-not $volumeExists) {
    Write-Host "❌ Erro: Volume '$VolumeName' não encontrado!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Volumes disponíveis:" -ForegroundColor Yellow
    docker volume ls
    exit 1
}

Write-Host "🔍 Volume encontrado!" -ForegroundColor Green
Write-Host "📦 Criando backup..." -ForegroundColor Yellow

# Criar backup usando container temporário
$result = docker run --rm `
    -v "${VolumeName}:/data" `
    -v "${PWD}/${BackupDir}:/backup" `
    alpine tar czf "/backup/$backupFile" -C /data .

if ($LASTEXITCODE -eq 0) {
    $fileSize = (Get-Item $backupPath).Length
    $fileSizeMB = [math]::Round($fileSize / 1MB, 2)
    
    Write-Host ""
    Write-Host "✅ Backup criado com sucesso!" -ForegroundColor Green
    Write-Host ""
    Write-Host "Detalhes do backup:" -ForegroundColor Cyan
    Write-Host "  Arquivo: $backupFile" -ForegroundColor White
    Write-Host "  Tamanho: $fileSizeMB MB" -ForegroundColor White
    Write-Host "  Local: $backupPath" -ForegroundColor White
    Write-Host ""
    
    # Listar todos os backups
    Write-Host "Backups disponíveis:" -ForegroundColor Cyan
    Get-ChildItem -Path $BackupDir -Filter "backup-*.tar.gz" | 
        Sort-Object LastWriteTime -Descending | 
        Format-Table Name, @{Label="Tamanho (MB)"; Expression={[math]::Round($_.Length / 1MB, 2)}}, LastWriteTime -AutoSize
    
} else {
    Write-Host ""
    Write-Host "❌ Erro ao criar backup!" -ForegroundColor Red
    exit 1
}
