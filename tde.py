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
    
