import customtkinter as ctk
from database import *



# CONFIGURAÇÕES GERAIS
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("roxo_theme.json")


class UniversidadeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        #CONFIGURAÇÕES INICIAIS
        self.title("CEUCRUD")
        self.geometry("1920x1080")
        self.resizable(True , True)
        
        #TITULO PRINCIPAL
        titulo = ctk.CTkLabel(self, text="Sistema de Gerenciamento Universitário", font=("Arial", 30, "bold") , text_color="black")
        titulo.place(x=960 , y=50 , anchor="center")

        #TITULO CEUCRUD
        ceucrud = ctk.CTkLabel(self, text="CEUCRUD" , font=("Arial", 30,"bold") , text_color="purple")
        ceucrud.place(x=100 , y=50,anchor="center")
        
        # Tabs principais
        abas = ctk.CTkTabview(self, width=1280, height=720)
        abas.place(relx=0.5,rely=0.5,anchor="center")

        # Criação das abas
        aba_cursos = abas.add("Cursos")
        aba_alunos = abas.add("Alunos")
        aba_funcionarios = abas.add("Funcionários")
        aba_materias = abas.add("Matérias")
        aba_matriculas = abas.add("Matrículas")

        # ABA CURSOS
        self.curso_nome = ctk.CTkEntry(aba_cursos, placeholder_text="Nome do Curso")
        self.curso_nome.place(relx=0.5 - 0.1 , rely=0.2 , anchor="center")
        self.curso_duracao = ctk.CTkEntry(aba_cursos, placeholder_text="Duração (em semestres)")
        self.curso_duracao.place(relx=0.5 + 0.1 , rely=0.2 , anchor="center")
        self.txt_cursos = ctk.CTkTextbox(aba_cursos, width=700, height=300)
        self.txt_cursos.place(relx=0.5 , rely=0.5 , anchor="center")

        ctk.CTkButton(aba_cursos, text="Adicionar Curso", command=self.adicionar_curso).place(relx=0.5 -0.22 , rely=0.85 , anchor="center")
        ctk.CTkButton(aba_cursos, text="Listar Cursos", command=self.listar_cursos).place(relx=0.5 -0.1 , rely=0.85 , anchor="center")
        self.txt_exc_curso = ctk.CTkEntry(aba_cursos,placeholder_text="Id para Excluir")
        self.txt_exc_curso.place(relx=0.5 + 0.1 , rely=0.85 , anchor="center")
        ctk.CTkButton(aba_cursos, text="Excluir" , command=self.deletar_curso).place(relx=0.5 + 0.22, rely=0.85 , anchor="center")

        # ABA ALUNOS
        self.aluno_nome = ctk.CTkEntry(aba_alunos, placeholder_text="Nome do Aluno")
        self.aluno_nome.pack(pady=5)
        self.aluno_cpf = ctk.CTkEntry(aba_alunos, placeholder_text="CPF (somente números)")
        self.aluno_cpf.pack(pady=5)
        self.aluno_data = ctk.CTkEntry(aba_alunos, placeholder_text="Data de Nascimento - Somente Numeros")
        self.aluno_data.pack(pady=5)
        self.aluno_curso = ctk.CTkEntry(aba_alunos, placeholder_text="ID do Curso")
        self.aluno_curso.pack(pady=5)

        self.txt_alunos = ctk.CTkTextbox(aba_alunos, width=700, height=300)
        self.txt_alunos.place(relx=0.5 , rely=0.5 , anchor="center")
        
        ctk.CTkButton(aba_alunos, text="Adicionar Aluno", command=self.adicionar_aluno).pack(pady=5)
        ctk.CTkButton(aba_alunos, text="Listar Alunos", command=self.listar_alunos).pack(pady=10)
        
        self.txt_exc_aluno = ctk.CTkEntry(aba_alunos,placeholder_text="Id para Excluir")
        self.txt_exc_aluno.place(relx=0.5 + 0.1 , rely=0.85 , anchor="center")
        ctk.CTkButton(aba_alunos, text="Excluir" , command=self.deletar_aluno).place(relx=0.5 + 0.22, rely=0.85 , anchor="center")

        # ABA FUNCIONÁRIOS
        self.func_nome = ctk.CTkEntry(aba_funcionarios, placeholder_text="Nome do Funcionário")
        self.func_nome.pack(pady=5)
        self.func_cargo = ctk.CTkEntry(aba_funcionarios, placeholder_text="Cargo")
        self.func_cargo.pack(pady=5)
        self.func_salario = ctk.CTkEntry(aba_funcionarios, placeholder_text="Salário (ex: 3500.00)")
        self.func_salario.pack(pady=5)

        ctk.CTkButton(aba_funcionarios, text="Adicionar Funcionário", command=self.adicionar_funcionario).pack(pady=5)
        self.txt_funcionarios = ctk.CTkTextbox(aba_funcionarios, width=700, height=300)
        self.txt_funcionarios.place(relx=0.5 , rely=0.5 , anchor="center")
        ctk.CTkButton(aba_funcionarios, text="Listar Funcionários", command=self.listar_funcionarios).pack()
        
        self.txt_exc_funcionario = ctk.CTkEntry(aba_funcionarios,placeholder_text="Id para Excluir")
        self.txt_exc_funcionario.place(relx=0.5 + 0.1 , rely=0.85 , anchor="center")
        ctk.CTkButton(aba_funcionarios, text="Excluir" , command=self.deletar_funcionario).place(relx=0.5 + 0.22, rely=0.85 , anchor="center")

        # ABA MATÉRIAS
        self.materia_nome = ctk.CTkEntry(aba_materias, placeholder_text="Nome da Matéria")
        self.materia_nome.pack(pady=5)
        self.materia_curso = ctk.CTkEntry(aba_materias, placeholder_text="ID do Curso")
        self.materia_curso.pack(pady=5)

        ctk.CTkButton(aba_materias, text="Adicionar Matéria", command=self.adicionar_materia).pack(pady=5)
        self.txt_materias = ctk.CTkTextbox(aba_materias, width=700, height=300)
        self.txt_materias.place(relx=0.5 , rely=0.5 , anchor="center")
        ctk.CTkButton(aba_materias, text="Listar Matérias", command=self.listar_materias).pack()
        
        self.txt_exc_materias = ctk.CTkEntry(aba_materias,placeholder_text="Id para Excluir")
        self.txt_exc_materias.place(relx=0.5 + 0.1 , rely=0.85 , anchor="center")
        ctk.CTkButton(aba_materias, text="Excluir" , command=self.deletar_materia).place(relx=0.5 + 0.22, rely=0.85 , anchor="center")

        # ABA MATRÍCULAS
        self.matricula_aluno = ctk.CTkEntry(aba_matriculas, placeholder_text="ID do Aluno")
        self.matricula_aluno.pack(pady=5)
        self.matricula_materia = ctk.CTkEntry(aba_matriculas, placeholder_text="ID da Matéria")
        self.matricula_materia.pack(pady=5)
        self.matricula_semestre = ctk.CTkEntry(aba_matriculas, placeholder_text="Semestre (ex: 1º, 2º, etc.)")
        self.matricula_semestre.pack(pady=5)
        self.matricula_ano = ctk.CTkEntry(aba_matriculas, placeholder_text="Ano (ex: 2025)")
        self.matricula_ano.pack(pady=5)

        ctk.CTkButton(aba_matriculas, text="Adicionar Matrícula", command=self.adicionar_matricula).pack(pady=5)
        self.txt_matriculas = ctk.CTkTextbox(aba_matriculas, width=700, height=300)
        self.txt_matriculas.place(relx=0.5 , rely=0.5 , anchor="center")
        ctk.CTkButton(aba_matriculas, text="Listar Matrículas", command=self.listar_matriculas).pack()
        
        self.txt_exc_matriculas = ctk.CTkEntry(aba_matriculas,placeholder_text="Id para Excluir")
        self.txt_exc_matriculas.place(relx=0.5 + 0.1 , rely=0.85 , anchor="center")
        ctk.CTkButton(aba_matriculas, text="Excluir" , command=self.deletar_matricula).place(relx=0.5 + 0.22, rely=0.85 , anchor="center")


    # FUNÇÕES DE CADA ABA

    def adicionar_curso(self):
        nome = self.curso_nome.get()
        duracao = self.curso_duracao.get()
        if nome and duracao:
            inserir_curso(nome, duracao)
            self.listar_cursos()
            self.curso_nome.delete(0, 'end')
            self.curso_duracao.delete(0, 'end')

    def listar_cursos(self):
        self.txt_cursos.delete("1.0", "end")
        for c in listar_cursos():
            self.txt_cursos.insert("end", f"ID: {c[0]} | Nome: {c[1]} | Duração: {c[2]} semestres\n")

    def deletar_curso(self):
        excluir_curso(
            self.txt_exc_curso.get()
        )
        self.listar_cursos()

    def adicionar_aluno(self):
        inserir_aluno(
            self.aluno_nome.get(),
            self.aluno_cpf.get(),
            formatar_data_nascimento(self.aluno_data.get()),
            self.aluno_curso.get()
        )
        self.listar_alunos()

    def listar_alunos(self):
        alunos = listar_alunos()
        self.txt_alunos.delete("1.0", "end")
        for a in alunos:
            self.txt_alunos.insert("end", f"ID: {a[0]} | Nome: {a[1]} | CPF: {a[2]} | Curso: {a[4]}\n")

    def deletar_aluno(self):
        excluir_aluno(
            self.txt_exc_aluno.get()
        )
        self.listar_alunos()
    
    #FUNCIONARIOS
    
    def adicionar_funcionario(self):
        inserir_funcionario(self.func_nome.get(), self.func_cargo.get(), self.func_salario.get())
        self.listar_funcionarios()

    def listar_funcionarios(self):
        funcionarios = listar_funcionarios()
        self.txt_funcionarios.delete("1.0", "end")
        for f in funcionarios:
            self.txt_funcionarios.insert("end", f"ID: {f[0]} | Nome: {f[1]} | Cargo: {f[2]} | Salário: R${f[3]}\n")
            
    def deletar_funcionario(self):
        excluir_funcionario(
            self.txt_exc_funcionario.get()
        )
        self.listar_funcionarios()

    def adicionar_materia(self):
        inserir_materia(self.materia_nome.get(), self.materia_curso.get())
        self.listar_materias()

    def listar_materias(self):
        materias = listar_materias()
        self.txt_materias.delete("1.0", "end")
        for m in materias:
            self.txt_materias.insert("end", f"ID: {m[0]} | Matéria: {m[1]} | Curso: {m[2]}\n")
            
    def deletar_materia(self):
        excluir_materia(
            self.txt_exc_materias.get()
        )
        self.listar_materias()

    def adicionar_matricula(self):
        inserir_matricula(
            self.matricula_aluno.get(),
            self.matricula_materia.get(),
            self.matricula_semestre.get(),
            self.matricula_ano.get()
        )
        self.listar_matriculas()

    def listar_matriculas(self):
        matriculas = listar_matriculas()
        self.txt_matriculas.delete("1.0", "end")
        for m in matriculas:
            self.txt_matriculas.insert("end", f"ID: {m[0]} | Aluno: {m[1]} | Matéria: {m[2]} | {m[3]} - {m[4]}\n")

    def deletar_matricula(self):
        excluir_matricula(
            self.txt_exc_matriculas.get()
        )
        self.listar_matriculas()

# EXECUÇÃO

if __name__ == "__main__":
    app = UniversidadeApp()
    app.mainloop()
