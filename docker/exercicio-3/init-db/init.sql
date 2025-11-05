-- Script de inicialização do banco de dados
-- Este arquivo será executado automaticamente quando o container do PostgreSQL for criado pela primeira vez

-- Criar tabela de tarefas
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserir dados de exemplo
INSERT INTO tasks (title, completed) VALUES
    ('Aprender Docker', false),
    ('Estudar Docker Compose', false),
    ('Criar aplicação multi-container', false),
    ('Configurar PostgreSQL', true),
    ('Implementar API REST', true);

-- Criar índice para melhorar performance
CREATE INDEX IF NOT EXISTS idx_tasks_created_at ON tasks(created_at DESC);

-- Exibir mensagem de sucesso
DO $$
BEGIN
    RAISE NOTICE 'Database initialized successfully!';
    RAISE NOTICE 'Table "tasks" created with sample data.';
END $$;
