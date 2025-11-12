CREATE DATABASE IF NOT EXISTS db_universidade;
USE db_universidade;

CREATE TABLE tb_curso(
id_curso int not null primary key auto_increment,
nome varchar(100) not null,
duracao_semestres int not null
);

CREATE TABLE tb_aluno(
id_aluno int not null primary key auto_increment,
nome varchar(100) not null,
cpf char(11) unique not null,
data_nascimento date,
id_curso int,
foreign key(id_curso) references tb_curso(id_curso)
);

CREATE TABLE tb_funcionario(
id_funcionario int not null primary key auto_increment,
nome varchar(100) not null,
cargo varchar(50),
salario decimal(10,2)
);

CREATE TABLE tb_materia(
id_materia int not null primary key auto_increment,
nome varchar(100) not null,
id_curso int,
foreign key(id_curso) references tb_curso(id_curso)
);

CREATE TABLE tb_professor_materia(
id_funcionario int,
id_materia int,
primary key(id_funcionario , id_materia),
foreign key(id_funcionario) references tb_funcionario(id_funcionario),
foreign key(id_materia) references tb_materia(id_materia)
);

CREATE TABLE tb_matricula (
    id_matricula INT AUTO_INCREMENT PRIMARY KEY,
    semestre VARCHAR(10),
    ano INT,
    id_aluno INT,
    id_materia INT,
    FOREIGN KEY (id_aluno) REFERENCES tb_aluno(id_aluno),
    FOREIGN KEY (id_materia) REFERENCES tb_materia(id_materia)
);


