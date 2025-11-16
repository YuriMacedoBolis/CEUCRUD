#  CEUCRUD — Sistema de Gerenciamento Universitário
<img width="1916" height="1032" alt="CEUCRUD-DARK" src="https://github.com/user-attachments/assets/bafd0d3d-b8e7-4bb1-89a2-5506ae805abe" />
<img width="1920" height="1040" alt="CEUCRUD-LIGHT" src="https://github.com/user-attachments/assets/df38007d-3246-4090-94d8-f71a6a05ac3c" />

O **CEUCRUD** é um sistema desktop desenvolvido em **Python**, utilizando a biblioteca **CustomTkinter**, para gerenciamento completo de dados universitários.  
Ele se conecta a um banco MySQL e permite realizar **CRUD (Create, Read, Update, Delete)** das seguintes entidades:

- Cursos  
- Alunos  
- Funcionários  
- Matérias  
- Matrículas  

Este projeto foi criado para fins de estudo e prática de lógica, GUI com Python e integração com banco de dados.

---

##  Tecnologias Utilizadas

- **Python 3**
- **CustomTkinter**
- **MySQL**
- **mysql-connector-python**
- **Tkinter (CTkTabview, CTkToplevel, CTkSwitch)**

---

##  Estrutura do Projeto

├── main.py # Interface gráfica e lógica do sistema
├── database.py # Conexão com o MySQL e funções CRUD
├── bd_universidade.sql # Script do banco de dados completo
└── roxo_theme.json # Tema personalizado (caso utilizado)


---

##  Funcionalidades

###  Cursos
- Adicionar curso  
- Listar cursos  
- Atualizar curso  
- Excluir curso  

###  Alunos
- Adicionar aluno  
- Conversão automática da data (DDMMYYYY → YYYY-MM-DD)  
- Listar alunos com nome do curso  
- Atualizar aluno  
- Excluir aluno  

###  Funcionários
- Adicionar  
- Listar  
- Editar  
- Excluir  

###  Matérias
- Associar matérias a cursos  
- CRUD completo  

###  Matrículas
- Matricular aluno em matéria  
- Listar com nomes completos  
- Atualizar matrícula  
- Excluir matrícula  

---

##  Banco de Dados

O script `bd_universidade.sql` cria automaticamente:

- Banco `universidade`
- Tabelas:
  - `tb_curso`
  - `tb_aluno`
  - `tb_funcionario`
  - `tb_materia`
  - `tb_matricula`
- E ainda insere **dados fictícios** para teste.

Para criar o banco, execute:

```sql
SOURCE bd_universidade.sql;
```
1️⃣ Instale as dependências
```
pip install customtkinter
pip install mysql-connector-python
```
2️⃣ Configure sua conexão MySQL

No arquivo database.py, altere:
```
host="localhost",
user="root",
password="SUA_SENHA",
database="universidade"
```
3️⃣ Certifique-se de que o MySQL está rodando  
▶️ Como executar a aplicação
```
python main.py
```

A interface será aberta automaticamente.

## Interface

A interface utiliza o CustomTkinter com:

Abas organizadas por categorias (Cursos, Alunos, Funcionários, Matérias, Matrículas)

Inputs de preenchimento

Janelas de atualização

Tema claro/escuro com um switch

Caixa de listagem dinâmica (CTkTextbox)

## Objetivo do Projeto

Este projeto foi desenvolvido para fins educacionais, com foco em:

Aprender CRUD em Python

Criar interfaces gráficas modernas

Praticar integração com MySQL

Entender relacionamentos entre tabelas

 Contribuições

Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests.

 Licença

Este projeto está sob a licença MIT.
Use, modifique e aprimore livremente.

