CREATE DATABASE Faculdade;
USE faculdade;

CREATE TABLE professor (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    data_admissao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE aluno (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES professor(id_professor)
);

CREATE TABLE disciplina (
    id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
    nome_disciplina VARCHAR(100) NOT NULL,
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES professor(id_professor)
);

-- Inserir dados na tabela professor
INSERT INTO professor (nome, email) VALUES
('Dr. João Silva', 'joao.silva@faculdade.com'),
('Profa. Maria Oliveira', 'maria.oliveira@faculdade.com');

-- Inserir dados na tabela aluno
INSERT INTO aluno (nome, cpf, data_nascimento, id_professor) VALUES
('Carlos Souza', '12345678901', '2000-05-12', 1),
('Ana Costa', '98765432100', '1999-08-22', 2);

-- Inserir dados na tabela disciplina
INSERT INTO disciplina (nome_disciplina, id_professor) VALUES
('Matemática', 1),
('Física', 2);

