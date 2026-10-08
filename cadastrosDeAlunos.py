estudantes = { }

def adicionarAlunos():
    nome = input("digite o nome do aluno: ")
    try:
        nota = float(input("digite a nota final: ").replace(",","."))
        estudantes[nome] = nota
    except ValueError as erro:
        print(f"comando invalido: {erro}")
        return
    print("aluno cadastrado com sucesso!!!")
    
def listarAlunos():
    if not estudantes:
        print("nenhum aluno cadastrado")
        return
    for nomes, notas in estudantes.items():
        print("\n=== Lista de alunos ===")
        print(f"{nomes} | nota {notas}")
        
def buscarNota():
        nome = input("digite o nome do aluno: ")
        while True:
            if nome not in estudantes:
                print("digite um nome valido")
                break
            else:
                print(f"nota: {estudantes[nome]}")
                break
        
def Main():
    while True:
        print("\n=== sistema de alunos === ")
        print("1 - adicionar aluno: ")
        print("2 - listar aluno: ")
        print("3 - Buscar nota: ")
        print("0 - Sair")
        try:
            opcao = int(input("opcao: "))
            if opcao == 0:
                print("fim do programa")
                break
            elif opcao == 1:
                adicionarAlunos()
            elif opcao == 2:
                listarAlunos()
            elif opcao == 3:
                if not estudantes:
                    print("estudante nao encontrado")
                else:
                    buscarNota()
        except ValueError as erro:
             print("entrada invalida!!!")

if __name__ == "__main__":
    Main()