tasks = []

def add_task():
    task = input("Digite a nova tarefa: ")
    tasks.append(task)
    print("Tarefa adicionada com sucesso!")

def delete_task():
    try:
        task_index = int(input("Digite o número da tarefa que deseja deletar: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f"Tarefa '{removed_task}' removida com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

def list_tasks():
    if tasks:
        print("Lista de tarefas:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Nenhuma tarefa encontrada.")

if __name__ == "__main__":
    print("Welcome to the to-do list app :)")
    while True:
        print("\n")
        print("Por favor, selecione uma das seguintes opções")
        print("-------------------------------------------")
        print("1. Adicionar uma nova tarefa")
        print("2. Deletar uma tarefa")
        print("3. Lista de tarefas")
        print("4. Sair")

        choice = input("Faça uma escolha: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            print("Goodbye, wave, wave")
            break
        else:
            print("Entrada inválida. Por favor, tente novamente.")
