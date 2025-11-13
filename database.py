import mysql.connector
from mysql.connector import Error
from datetime import datetime

# FUNÇÃO DE CONEXÃO
def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost", #LOCALHOST
            user="root", #ROOT
            password="Escola21",  # troque pela sua senha do MySQL
            database="universidade" #ESSE MESMO
        )
        return conexao
    except Error as e:
        print("Erro ao conectar ao MySQL:", e)
        return None


# CURSOS
def inserir_curso(nome, duracao):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO tb_curso (nome_curso, duracao) VALUES (%s, %s)", (nome, duracao))
        con.commit()
        con.close()


def listar_cursos():
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM tb_curso")
        dados = cursor.fetchall()
        con.close()
        return dados


def atualizar_curso(id_curso, nome, duracao):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("UPDATE tb_curso SET nome_curso=%s, duracao=%s WHERE id_curso=%s",
                       (nome, duracao, id_curso))
        con.commit()
        con.close()


def excluir_curso(id_curso):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM tb_curso WHERE id_curso=%s", (id_curso,))
        con.commit()
        con.close()


# ALUNOS

from datetime import datetime

def formatar_data_nascimento(data_str: str) -> str:
    try:
        data_formatada = datetime.strptime(data_str, "%d%m%Y").strftime("%Y-%m-%d")
        return data_formatada
    except ValueError:
        raise ValueError("Data inválida. Digite no formato DDMMYYYY (ex: 12082005).")


def inserir_aluno(nome, cpf, data_nascimento, id_curso):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO tb_aluno (nome_aluno, cpf, data_nascimento, id_curso) VALUES (%s, %s, %s, %s)",
            (nome, cpf, data_nascimento, id_curso)
        )
        con.commit()
        con.close()


def listar_alunos():
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT a.id_aluno, a.nome_aluno, a.cpf, a.data_nascimento, c.nome_curso
            FROM tb_aluno a
            LEFT JOIN tb_curso c ON a.id_curso = c.id_curso
        """)
        dados = cursor.fetchall()
        con.close()
        return dados


def atualizar_aluno(id_aluno, nome, cpf, data_nascimento, id_curso):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            UPDATE tb_aluno 
            SET nome_aluno=%s, cpf=%s, data_nascimento=%s, id_curso=%s 
            WHERE id_aluno=%s
        """, (nome, cpf, data_nascimento, id_curso, id_aluno))
        con.commit()
        con.close()


def excluir_aluno(id_aluno):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM tb_aluno WHERE id_aluno=%s", (id_aluno,))
        con.commit()
        con.close()


# FUNCIONÁRIOS
def inserir_funcionario(nome, cargo, salario):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO tb_funcionario (nome_funcionario, cargo, salario)
            VALUES (%s, %s, %s)
        """, (nome, cargo, salario))
        con.commit()
        con.close()


def listar_funcionarios():
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM tb_funcionario")
        dados = cursor.fetchall()
        con.close()
        return dados


def atualizar_funcionario(id_funcionario, nome, cargo, salario):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            UPDATE tb_funcionario SET nome_funcionario=%s, cargo=%s, salario=%s
            WHERE id_funcionario=%s
        """, (nome, cargo, salario, id_funcionario))
        con.commit()
        con.close()


def excluir_funcionario(id_funcionario):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM tb_funcionario WHERE id_funcionario=%s", (id_funcionario,))
        con.commit()
        con.close()


# MATÉRIAS
def inserir_materia(nome, id_curso):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO tb_materia (nome_materia, id_curso)
            VALUES (%s, %s)
        """, (nome, id_curso))
        con.commit()
        con.close()


def listar_materias():
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT m.id_materia, m.nome_materia, c.nome_curso
            FROM tb_materia m
            LEFT JOIN tb_curso c ON m.id_curso = c.id_curso
        """)
        dados = cursor.fetchall()
        con.close()
        return dados


def atualizar_materia(id_materia, nome, id_curso):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            UPDATE tb_materia SET nome_materia=%s, id_curso=%s WHERE id_materia=%s
        """, (nome, id_curso, id_materia))
        con.commit()
        con.close()


def excluir_materia(id_materia):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM tb_materia WHERE id_materia=%s", (id_materia,))
        con.commit()
        con.close()


# MATRÍCULAS
def inserir_matricula(id_aluno, id_materia, semestre, ano):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            INSERT INTO tb_matricula (id_aluno, id_materia, semestre, ano)
            VALUES (%s, %s, %s, %s)
        """, (id_aluno, id_materia, semestre, ano))
        con.commit()
        con.close()


def listar_matriculas():
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("""
            SELECT m.id_matricula, a.nome_aluno, ma.nome_materia, m.semestre, m.ano
            FROM tb_matricula m
            LEFT JOIN tb_aluno a ON m.id_aluno = a.id_aluno
            LEFT JOIN tb_materia ma ON m.id_materia = ma.id_materia
        """)
        dados = cursor.fetchall()
        con.close()
        return dados


def excluir_matricula(id_matricula):
    con = conectar()
    if con:
        cursor = con.cursor()
        cursor.execute("DELETE FROM tb_matricula WHERE id_matricula=%s", (id_matricula,))
        con.commit()
        con.close()
