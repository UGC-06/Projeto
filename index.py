tarefas = []

def exibir_menu():
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa que deseja adicionar: ")
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print(f'Tarefa "{tarefa}" adicionada com sucesso!')

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.")
        return
    
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "[Concluída]" if tarefa["concluida"] else "[Pendente]"
        print(f"{i}. {tarefa['tarefa']} {status}")

def marcar_concluida():
    listar_tarefas()
    try:
        indice = int(input("\nDigite o número da tarefa a marcar como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print(f'Tarefa "{tarefas[indice]["tarefa"]}" marcada como concluída!')
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

def excluir_tarefa():
    listar_tarefas()
    try:
        indice = int(input("\nDigite o número da tarefa a excluir: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefa_removida = tarefas.pop(indice)
            print(f'Tarefa "{tarefa_removida["tarefa"]}" excluída com sucesso!')
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "5":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
