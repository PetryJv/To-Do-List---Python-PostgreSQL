import psycopg2
from database import conexao, conexao_cursor

if conexao is None:
    print("Sem conexao com o banco de dados...")
    exit()

# ========= FUNÇÃO MENU PRINCIPAL =========
def menu():
    print("\n===== TO-DO LIST =====")
    print("[1] Adicionar tarefa")
    print("[2] Exibir tarefas")
    print("[3] Status tarefas")
    print("[4] Remover tarefa")
    print("[5] Sair")
    print("======================")

# ========= FUNÇÃO CRIAR TAREFA =========
def criar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")

    conexao_cursor.execute("INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)",(titulo, descricao))
    conexao.commit() #.commit() -> salvar dado no db

    print("Tarefa criada com sucesso!")

#obs: nao precisa de tratativa de dados - titulo e descrição (opicional)

# ========= FUNÇÃO EXIBIR TAREFAS =========
def exibir_tarefas():
    conexao_cursor.execute("SELECT id, titulo, descricao, data_criacao, concluida FROM tarefas")
    tarefas = conexao_cursor.fetchall()

#conexao_cursor.execute -> envia o comando SQL para o BD
#conexao_cursor.fetchall() -> busca TODOS os resultados da ultima consulta executada

#usa o fetchall() para trazer os dados do BD para o python pelo SELECT
#pega todas as linhas retornadas no SELECT e armazena em tarefas
#ele retorna uma lista de tuplas(cada tupla representa uma linha da tabela)

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")

# ----- EXIBIR STATUS DA TAREFA -----
    for tarefa in tarefas:
        if tarefa[4] == True: #tarefa[4] porque esta pegando o concluida - 5 item da tupla | começa em 0 a contagem
            status = "✓"
        else:
            status = "✗"
# ----- EXIBIÇÃO DAS TAREFAS -----
        print(f"\n| ID: {tarefa[0]} |")
        print(f"| Título: {tarefa[1]} |")
        print(f"| Descrição: {tarefa[2]} |")
        print(f"| Data de criação: {tarefa[3]} |")
        print(f"| Status: {status}\n")
        print("----------------------")

    print("\n=============================")

# ========= FUNÇÃO STATUS DA TAREFA =========
def status_tarefa():
    exibir_tarefas()

    id_tarefa = input("Digite o ID da tarefa que deseja alterar: ")

    while not id_tarefa.isdigit():
        print("Digite apenas números.")
        id_tarefa = input("Digite o ID da tarefa que deseja alterar: ") 

    # Verificar se a tarefa existe e pegar o status atual
    conexao_cursor.execute("SELECT concluida FROM tarefas WHERE id = %s", (id_tarefa,))

    resultado = conexao_cursor.fetchone() 
    #pega a linha retornada na consulta SQL - buscou a linha da coluna 'concluida' - valores booleano
    #resultado = (true,) ou none

    if resultado is None:
        print("Tarefa não encontrada.")
        return

    status_atual = resultado[0] 
    #resultado[0] - me da o primeiro valor da linha da tabela
    #se fosse resultado[1] - estaria puxando o segundo valor da linha da tabela - mas vai dar erro porque no comando SQL so pedi a posição 1
    # valor recebido é booleano - 'concluida' na tabela é booleano, por isso aqui é T/F

    if status_atual is True: #verifica valor booleano para exibir string
        status_exibir = "✓ "
    else:
        status_exibir = "✗ "

    print(f"\nStatus atual da tarefa: {status_exibir}\n")
    print("1 - Marcar como CONCLUÍDA")
    print("2 - Marcar como PENDENTE")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if status_atual: # usando valor booleano - caso ja estaja como true, informa a msg abaixo e retorna 
            print("Essa tarefa já está concluída.")
            return
        else:
            conexao_cursor.execute("UPDATE tarefas SET concluida = TRUE WHERE id = %s", (id_tarefa,))
            conexao.commit()
            print("Tarefa marcada como concluída!")

    elif opcao == "2":
        if status_atual:
            print("Essa tarefa já está pendente.")
            return
        conexao_cursor.execute("UPDATE tarefas SET concluida = FALSE WHERE id = %s",(id_tarefa,))

        conexao.commit()
        print("Tarefa marcada como pendente!")

    else:
        print("Opção inválida.")
        return

# ========= FUNÇÃO REMOVER TAREFA =========
def remover_tarefa():
    exibir_tarefas()

    id_tarefa = input("Digite o ID da tarefa que deseja remover: ")

    while not id_tarefa.isdigit():
        print("Digite apenas números.")
        id_tarefa = input("Digite o ID da tarefa que deseja remover: ")

    # Verificar se a tarefa existe
    conexao_cursor.execute("SELECT id FROM tarefas WHERE id = %s",(id_tarefa,))

    resultado = conexao_cursor.fetchone()

    if resultado is None:
        print("Tarefa não encontrada.")
        return

    # Confirmação antes de deletar
    confirmacao = input("Tem certeza que deseja remover essa tarefa? (s/n): ").strip().lower()

    if confirmacao != "s":
        print("Remoção cancelada.")
        return

    conexao_cursor.execute("DELETE FROM tarefas WHERE id = %s", (id_tarefa,))

    conexao.commit()

    print("Tarefa removida com sucesso!")

# ========= LAÇO MENU =========
while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("\n+----------------------------------+\n")
        print("| ADICIONANDO uma tarefa |")
        print("\n+----------------------------------+\n")
        criar_tarefa()
        
    elif escolha == "2":
        print("\n+----------------------------------+")
        print("| EXIBINDO tarefas |\n")
        print("+----------------------------------+")
        exibir_tarefas()
        
    elif escolha == "3":
        print("\n+----------------------------------+")
        print("| Status das tarefas |\n")
        status_tarefa()
        
    elif escolha == "4":
        print("\n+----------------------------------+")
        print("| REMOVENDO tarefas |\n")
        remover_tarefa()
        
    elif escolha == "5":
        print("\n+----------------------------------+\n")
        print("| Saindo do programa..... |")
        print("\n+----------------------------------+\n")
        exit()
        conexao.close()
        conexao_cursor.close()
        break

    else:
        print("Opção inválida!")


'''
INSERT INTO -> inserir dados
tarefas -> nome da tabela
(titulo, descricao) -> colunas que vamos preencher
VALUES (%s, %s) -> valores que virão do Python
%s -> placeholders
'''
    