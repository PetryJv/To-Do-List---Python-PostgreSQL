# 📝 To-Do List em Python + PostgreSQL

## 📌 Sobre o Projeto

Este projeto foi desenvolvido em Python com integração ao banco de dados PostgreSQL, com o objetivo de implementar um sistema de gerenciamento de tarefas no terminal (CLI).

O sistema permite criar, visualizar, atualizar e remover tarefas utilizando operações CRUD completas, aplicando conceitos fundamentais de banco de dados relacional e organização modular de código.

O foco principal do projeto é consolidar conhecimentos em:

- Conexão com banco de dados
- Manipulação de dados com SQL
- Estruturação de projetos em múltiplos arquivos
- Segurança básica utilizando variáveis de ambiente

---

## 🚀 Funcionalidades

- Menu interativo no terminal
- Criação de novas tarefas
- Listagem de tarefas cadastradas
- Atualização de status (Concluída / Pendente)
- Remoção de tarefas
- Validação de entrada numérica
- Uso de placeholders (%s) para evitar SQL Injection
- Separação de responsabilidades (`main.py` e `database.py`)

---

## 🛠 Tecnologias e Recursos Utilizados

- Python 3
- PostgreSQL
- psycopg2-binary
- SQL
- Variáveis de ambiente (`os.getenv`)

---

## 🧠 Conceitos Aplicados

- CRUD (Create, Read, Update, Delete)
- Conexão com banco de dados relacional
- Uso de cursor para execução de comandos SQL
- Transações e uso de `commit`
- Manipulação de dados retornados com `fetchall()` e `fetchone()`
- Uso de variáveis de ambiente para segurança
- Modularização de código
- Validação básica de entrada do usuário

---

## 📦 Instalação das Dependências

Antes de executar o projeto, instale as dependências com:

```bash
pip install -r requirements.txt
```

---

## 🗄 Estrutura do Banco de Dados

A tabela principal do projeto é composta pelos seguintes campos:

- `id` → Identificador único (SERIAL PRIMARY KEY)
- `titulo` → Título da tarefa (VARCHAR)
- `descricao` → Descrição detalhada (TEXT)
- `data_criacao` → Data automática de criação (TIMESTAMP)
- `concluida` → Status da tarefa (BOOLEAN)

O banco pode ser criado executando o arquivo:

```
schema.sql
```

---

## 🔐 Como Configurar a Conexão com o Banco (Variável de Ambiente)

O projeto utiliza variável de ambiente para armazenar a senha do banco de dados, evitando expor informações sensíveis no código.

A conexão é realizada através de:

```python
password = os.getenv("DB_SENHA")
```

Antes de executar o programa, é necessário definir a variável de ambiente `DB_SENHA`.

### ▶ Windows (PowerShell)

```powershell
$env:DB_SENHA="sua_senha_aqui"
python main.py
```

### ▶ Windows (CMD)

```cmd
set DB_SENHA=sua_senha_aqui
python main.py
```

### ▶ Linux / Git Bash

```bash
export DB_SENHA="sua_senha_aqui"
```

---

## ▶ Como Executar o Projeto

1. Clonar o repositório
2. Instalar as dependências:

```bash
pip install -r requirements.txt
```

3. Criar o banco de dados utilizando o arquivo `schema.sql`
4. Definir a variável de ambiente `DB_SENHA`
5. Executar o programa:

```bash
python main.py
```

---

## 📈 Melhorias Futuras

- Implementação de paginação de tarefas
- Filtro por status (concluídas / pendentes)
- Busca por título
- Tratamento de exceções com rollback
- Refatoração para arquitetura em camadas

---

## 👨‍💻 Autor

**João Victor Petry**  
Estudante de Ciência da Computação