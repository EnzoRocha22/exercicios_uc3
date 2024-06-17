vetornome=[]
vetorIdade=[]
vetorEmail=[]
vetorTelefone=[]
vetorAgenda=[]
agenda = []

quantidade = 0
total_idade = 0


resp = ''
while True:
    nome= input("informe o nome ")
    idade = int(input("informe sua idade "))
    email = input("infomre o seu email ")
    endereco = input("digite se endereço ")
    telefone = int(input(ValueError("insira seu telefone ")))
    total_idade = total_idade + idade
    quantidade += 1 

    agenda.append((nome, idade, email, endereco, telefone))

    resp = input("deseja continuar (s/n)").lower()
    if resp == "n":
        break

for n in vetornome:
    if nome < 18:
        print("menor de idade ")


media_idade = total_idade / quantidade
print(f'menor de idade {nome} e a quantidade é {quantidade}')

