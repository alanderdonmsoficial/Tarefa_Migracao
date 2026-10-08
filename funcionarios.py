
MAX = 1
escritorio = [ ]

def adicionarFuncionario():

    if len(escritorio) >= MAX:
        print(f"limite de funcionarios atingidos")
        return
    
    nome = input("digite o nome do funcionario: ")
    cargo = input("digite o cargo do funcionario: ")

    while True:
        try:
            salario = float(input("entre com o salario do funcionario: ").replace(",","."))
            break
        except ValueError as erro:
            print(f"entre com um valor valido: {erro}")

    novo_funcionario = {"nome": nome, "cargo":cargo, "salario":salario}
    escritorio.append(novo_funcionario)

    print("funcionarios cadastrado com sucesso!!!")

def listarFuncionario():
    if not escritorio:
        print("nenhum funcionario foi cadastrado")
        return
    print("\n === lista de funcionarios === ")
    for i, empregado in enumerate(escritorio,start = 1):
        print(f"{i}) - nome: {empregado["nome"]} , cargo: {empregado["cargo"]}, salario: {empregado["salario"]:.3f} ")

def buscarFuncionario():
    if not escritorio:
        print("não existe funcionario cadastrado")
        return
    
    busca_empregado = input("digite o nome de um funcionario: ")
    encontrado = False
    for funcionario in escritorio:
        if funcionario["nome"].lower() == busca_empregado.lower():
            print(f"cargo: {funcionario["cargo"]} | salario: {funcionario["salario"]:.3f}")
            encontrado = True
            break
    if not encontrado:
        print(f"digite um nome valido , nome buscado nao foi encontrado : {busca_empregado}")    

def Main():
    while True:
        print("\n=== sistema de alunos === ")
        print("1 - adicionar funcionario: ")
        print("2 - listar funcionario: ")
        print("3 - buscar funcionario: ")
        print("0 - Sair")
        try:
            opcao = int(input("opcao: "))
            if opcao == 0:
                print("fim do programa")
                break
            elif opcao == 1:
                adicionarFuncionario()
            elif opcao == 2:
                listarFuncionario()
            elif opcao == 3:
                buscarFuncionario()
        except ValueError as erro:
            print("entrada invalida!!!")
if __name__ == "__main__":
    Main()