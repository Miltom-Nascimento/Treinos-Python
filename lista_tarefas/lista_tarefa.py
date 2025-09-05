from lista_tarefa_classe import Lista

def main():
    lista = Lista()
    while True:
        escolha = int(input("Digite 1 para adicionar itens na lista\nDigte 2 para remover itens da lista\nDigite 3 para ver os itens da lista\n"))
        
        match escolha:
            case 1:
                tarefa = input("Digite a tarefa para adicionar: \n")
                lista.adicionar(tarefa)
            case 2:
                tarefa = input("Digite a tarefa para remover: \n")
                lista.remover(tarefa)
            case 3:
                lista.mostrar()
            case _:
                print("vc nao escolheu uma opcao valida")

main()