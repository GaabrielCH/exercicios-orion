-- =================================================================
-- EXERCÍCIO 2 - SQL COM JOINS E FILTROS
-- =================================================================

SELECT 
    alunos.nome AS nome_aluno,
    alunos.email,
    cursos.nome_curso
FROM alunos
INNER JOIN cursos ON alunos.curso_id = cursos.id
ORDER BY cursos.nome_curso, alunos.nome;


SELECT 
    alunos.nome AS nome_aluno,
    alunos.email,
    cursos.nome_curso
FROM alunos
INNER JOIN cursos ON alunos.curso_id = cursos.id
WHERE cursos.nome_curso = 'Desenvolvimento Web';


UPDATE alunos
SET curso_id = 2
WHERE nome = 'Maria Santos';


SELECT 
    alunos.id,
    alunos.nome,
    alunos.email,
    cursos.nome_curso
FROM alunos
INNER JOIN cursos ON alunos.curso_id = cursos.id
WHERE alunos.nome = 'Maria Santos';


-- =================================================================
-- EXTRA (AVANÇADO)
-- =================================================================

SELECT 
    cursos.id,
    cursos.nome_curso,
    COUNT(alunos.id) as total_alunos
FROM cursos
LEFT JOIN alunos ON cursos.id = alunos.curso_id
GROUP BY cursos.id, cursos.nome_curso
HAVING COUNT(alunos.id) = 0;


SELECT 
    cursos.nome_curso,
    alunos.nome,
    alunos.email
FROM alunos
INNER JOIN cursos ON alunos.curso_id = cursos.id
ORDER BY cursos.nome_curso, alunos.nome;


SELECT 
    cursos.nome_curso,
    COUNT(alunos.id) as total_alunos
FROM cursos
LEFT JOIN alunos ON cursos.id = alunos.curso_id
GROUP BY cursos.id, cursos.nome_curso
ORDER BY total_alunos DESC;
