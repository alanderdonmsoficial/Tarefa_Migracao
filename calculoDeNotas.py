print(" === sistema de cadastro de alunos ===")

alunos = [ ]
notas = [ ]

for i in range(1,6):
    nome_aluno = input(f"digite o nome do {i}º aluno: ")
    alunos.append(nome_aluno)
    while True:
            try:
                nota_aluno = float(input(f"digite a nota de {nome_aluno}: ").replace(",","."))
                notas.append(nota_aluno)
                break
            except ValueError as erro:
                 print("comando invalido")
                               
media = sum(notas)/len(notas)

for i in range(len(alunos)):
    print(f"nome: {alunos[i]} , nota: {notas[i]}")
    
print(f"media final da turma: {media}")