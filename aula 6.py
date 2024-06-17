vetor = [] #Declarar Vetor
vetor.append("Enzo") # Add Elementos
vetor.append("Rocha") 
vetor.append("Medeiros")

print(vetor)
print(vetor[0]) # 0 é a primeira

nome = input("informe o seu nome")
vetor.append(nome)

print(vetor)

print(len(vetor)) #"len" retorna o numero de elementos

for nome in vetor:
    print(nome)