CREATE DATABASE to_do_list_db;

\c to_do_list_db

CREATE TABLE tarefas(

	id SERIAL PRIMARY KEY, -- SERIAL -> numero interio que auto incrementa
	titulo VARCHAR(50) NOT NULL, -- varchar() -> permite até X caracteres
	descricao TEXT,
	data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
