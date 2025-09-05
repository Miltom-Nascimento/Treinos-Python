class Lista:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, tarefa):
        self.tarefas.append(tarefa)

    def remover(self, tarefa):
        self.tarefas.remove(tarefa)

    def mostrar(self):
        if not self.tarefas:
            print("Nenhuma tarefa adicionada na lista!")
        else:
            print("\nTarefas:")
            for i, tarefa in enumerate(self.tarefas, 1):
                print(f"{i}. {tarefa}")