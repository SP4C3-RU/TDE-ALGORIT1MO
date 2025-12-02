def mostrar_menu():
  print("\n\033[1;35;45m=-= SISTEMAS DE TAREFAS =-=\033[m")
  print("\033[1;34;40m[1] - Adicionar nova tarefa.\033[m")
  print("\033[1;34;40m[2] - Listar tarefas.\033[m")
  print("\033[1;34;40m[3] - Marcar tarefa como concluída.\033[m")
  print("\033[1;34;40m[4] - Editar tarefa.\033[m")
  print("\033[1;34;40m[5] - Remover tarefa.\033[m")
  print("\033[1;34;40m[6] - Sair.\033[m")
  return input("\033[7;35;45m   Escolha uma opção:   \033[m")

def listar_tarefas(tarefas):
  if len(tarefas) == 0:
    print("\n\033[1;31;41mNenhuma tarefa cadastrada.\033[m")
  else:
    print("\n\033[1;35;45m=== LISTA DE TAREFAS ===\033[m")
    for i, tarefa in enumerate(tarefas):
      status = "\033[1;32;40mCONCLUÍUDA\033[m" if tarefa["status"] else "\033[1;31;40mPENDENTE\033[m"
      print(f"{i}-{tarefa['descricao']} ({status})")

def adicionar_tarefa(tarefas):
    descricao = input("\n\033[1;35;45mDigite a descrição da nova tarefa:\033[m ")
    tarefas.append({"descricao": descricao, "status": False})
    print("\033[1;32;42mTarefa adicionada com sucesso!\033[m")

def marcar_concluida(tarefas):
  listar_tarefas(tarefas)
  if tarefas:
    indice = int(input("\033[7;35;45mDigite o número da tarefa a marcar como concluída:\033[m "))
  if 0 <= indice < len(tarefas):
    tarefas[indice]["status"] = True
    print("\033[1;32;42mTarefa marcada como concluída!\033[m")
  else:
    print("\033[7;31;41mÍndice inválido!\033[m")

def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    if tarefas:
        indice = int(input("\033[7;35;45mDigite o número da tarefa a editar:\033[m "))
        if 0 <= indice < len(tarefas):
            nova_desc = input("\033[7;35;45mDigite a nova descrição:\033[m")
            tarefas[indice]["descricao"] = nova_desc
            print("\033[7;32;42mTarefa editada!\033[m")
        else:
            print("\033[7;31;41mÍndice inválido!\033[m")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    if tarefas:
        indice = int(input("\033[7;35;45mDigite o número da tarefa a remover:\033[m "))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("\033[7;32;42mTarefa removida!\033[m")
        else:
            print("\033[7;31;41mÍndice inválido!\033[m")
tarefas = []
while True:
    opcao = mostrar_menu()
    if opcao == '1':
       adicionar_tarefa(tarefas)
    elif opcao == '2':
       listar_tarefas(tarefas)
    elif opcao == '3':
        marcar_concluida (tarefas)
    elif opcao == '4':
       editar_tarefa(tarefas)
    elif opcao == '5':
       remover_tarefa (tarefas)
    elif opcao == '6':
       print('\033[7;31;40mSAINDO DO PROGRAMA...\033[m')
       break
    else:
       print('\033[7;31;40mOPÇÃO INVÁLIDA, TENTE NOVAMENTE.\033[m')