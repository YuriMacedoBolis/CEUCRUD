CREATE DATABASE IF NOT EXISTS universidade;
USE universidade;

CREATE TABLE tb_curso(
    id_curso INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    duracao_semestres INT NOT NULL
);

CREATE TABLE tb_aluno(
    id_aluno INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    data_nascimento DATE,
    id_curso INT,
    FOREIGN KEY(id_curso) REFERENCES tb_curso(id_curso)
        ON DELETE SET NULL
);

CREATE TABLE tb_funcionario(
    id_funcionario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    salario DECIMAL(10,2)
);

CREATE TABLE tb_materia(
    id_materia INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    id_curso INT,
    FOREIGN KEY(id_curso) REFERENCES tb_curso(id_curso)
        ON DELETE SET NULL
);

CREATE TABLE tb_matricula (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    semestre VARCHAR(10),
    ano INT,
    id_aluno INT,
    id_materia INT,
    FOREIGN KEY (id_aluno) REFERENCES tb_aluno(id_aluno)
        ON DELETE SET NULL,
    FOREIGN KEY (id_materia) REFERENCES tb_materia(id_materia)
        ON DELETE SET NULL
);

-- INSERÇÃO DE DADOS FICTÍCIOS -- 

INSERT INTO tb_curso (nome, duracao_semestres) VALUES
('Engenharia de Software', 8),
('Direito', 10),
('Administração', 8),
('Ciência da Computação', 8),
('Enfermagem', 10),
('Arquitetura e Urbanismo', 10),
('Psicologia', 10),
('Marketing Digital', 6),
('Biomedicina', 8),
('Educação Física', 8);

INSERT INTO tb_aluno (nome, cpf, data_nascimento, id_curso) VALUES
('Lucas Andrade', '12345678901', '2002-05-14', 1),
('Mariana Silva', '23456789012', '2001-11-29', 2),
('Thiago Ramos', '34567890123', '2003-03-07', 3),
('Clara Martins', '45678901234', '2004-01-22', 4),
('Renato Souza', '56789012345', '1999-07-10', 5),
('Jéssica Lima', '67890123456', '2002-09-03', 6),
('Bruno Carvalho', '78901234567', '2001-12-17', 7),
('Patrícia Gomes', '89012345678', '2000-08-05', 8),
('Eduardo Pires', '90123456789', '2003-10-28', 9),
('Ana Beatriz', '01234567890', '2004-04-09', 10);

INSERT INTO tb_funcionario (nome, cargo, salario) VALUES
('Carlos Pereira', 'Professor', 5500.00),
('Fernanda Dias', 'Coordenadora', 7200.00),
('João Henrique', 'Secretário', 2800.00),
('Luciana Castro', 'Professora', 5600.00),
('Eduardo Rocha', 'Auxiliar Administrativo', 2500.00),
('Patrícia Mello', 'Professora', 5900.00),
('André Santos', 'Professor', 5300.00),
('Rafael Lima', 'TI', 4500.00),
('Gabriela Siqueira', 'Bibliotecária', 3000.00),
('Marcelo Farias', 'Professor', 5800.00);

INSERT INTO tb_materia (nome, id_curso) VALUES
('Algoritmos e Programação', 1),
('Introdução ao Direito Civil', 2),
('Gestão Empresarial', 3),
('Cálculo I', 4),
('Anatomia Humana', 5),
('Projeto Arquitetônico I', 6),
('Psicologia Geral', 7),
('Marketing e Vendas', 8),
('Microbiologia', 9),
('Fisiologia do Exercício', 10);

INSERT INTO tb_matricula (semestre, ano, id_aluno, id_materia) VALUES
('1º', 2024, 1, 1),
('2º', 2024, 2, 2),
('1º', 2024, 3, 3),
('2º', 2024, 4, 4),
('1º', 2024, 5, 5),
('2º', 2024, 6, 6),
('1º', 2024, 7, 7),
('2º', 2024, 8, 8),
('1º', 2024, 9, 9),
('2º', 2024, 10, 10);


