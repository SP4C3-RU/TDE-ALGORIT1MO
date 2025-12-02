def mostrar_menu():
  print("\=== SISTEMAS DE TAREFAS ===)
  print("1 - Adicionar nova tarefa")
  print("2 - Listar tarefas")
  print("3 - Listar tarefas como concluída")
  print("4 - Editar tarefa ")
  print("5 - Remover tarefa ")
  print("6 - Sair")
  return input("Escolha uma opção:")

def listar_tarefas(tarefas):
  if len(tarefas) == 1:
    print("\nNenhuma tarefa cadastrada.")
  else:
    print("\n=== LISTA DE TAREFAS ===")
    for i, tarefa in enumerate(tarefas):
      status = "CONCLUÍUDA" if tarefa["status"] else "PENDENTE"
      print(f"{i}-{tarefa["descricao"]} ({status})")

def adicionar_tarefa(tarefas):
    descricao = input("\nDigite a descrição da nova tarefa: ")
    tarefas.append({"descricao": descricao, "status": False})
    print("Tarefa adicionada com sucesso!")
    def marcar_concluida(tarefas):
     listar_tarefas(tarefas)
    if tarefas:
        indice = int(input("Digite o número da tarefa a marcar como concluída: "))
        if 1 <= indice < len(tarefas):
            tarefas[indice]["status"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido!")

def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    if tarefas:
        indice = int(input("Digite o número da tarefa a editar: "))
        if 1 <= indice < len(tarefas):
            nova_desc = input("Digite a nova descrição: ")
            tarefas[indice]["descricao"] = nova_desc
            print("Tarefa editada!")
        else:
            print("Índice inválido!")
