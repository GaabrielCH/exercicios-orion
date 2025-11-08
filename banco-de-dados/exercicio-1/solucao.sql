-- =================================================================
-- EXERCÍCIO 1 - SQL BÁSICO (CREATE TABLE, INSERT, SELECT)
-- =================================================================

CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    nome_curso VARCHAR(100) NOT NULL
);


CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    curso_id INTEGER NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES cursos(id) ON DELETE CASCADE
);


INSERT INTO cursos (nome_curso) VALUES
    ('Desenvolvimento Web'),
    ('Ciência de Dados'),
    ('DevOps e Cloud');


INSERT INTO alunos (nome, email, curso_id) VALUES
    ('João Silva', 'joao.silva@email.com', 1),
    ('Maria Santos', 'maria.santos@email.com', 1),
    ('Pedro Oliveira', 'pedro.oliveira@email.com', 2),
    ('Ana Costa', 'ana.costa@email.com', 3);


SELECT * FROM cursos;

SELECT * FROM alunos;

INSERT INTO alunos (nome, email, curso_id) VALUES ('Teste Erro', 'teste@erro.com', 999);

\d cursos

\d alunos

SELECT COUNT(*) as total_cursos FROM cursos;

SELECT COUNT(*) as total_alunos FROM alunos;
