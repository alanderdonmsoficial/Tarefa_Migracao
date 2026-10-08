candidatos = ["opcao 1" , "opcao 2" , "opcao 3"]
votos = [0,0,0]
print("=== votacao ===")
print("opcoes: ")
for i in range(len(candidatos)):
    print(f"{i+1} - {candidatos[i]}")
votacaoAtiva = True
while votacaoAtiva:
    try:
            escolha = int(input(f"\nescolha os opcoes (1 a {len(candidatos)}) ou digite 0 para sair: "))
            if escolha == 0:
                votacaoAtiva = False
            elif escolha >= 1 and escolha <= len(candidatos):
                votos[escolha - 1] +=1
                print(f"voce votou na " + candidatos[escolha -1])
            else:
                 print("opcao invalida, tente novamente!!!")
    except ValueError as erro:
           print("Entrada invalida digite apenas numeros. ")
print("=== resultado finais ===")
for i in range(len(candidatos)):
    print(f"{candidatos[i]} : {votos[i]} voto(s)")