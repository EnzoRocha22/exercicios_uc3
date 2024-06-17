agenda = []



while True:
    pessoa = {}
    pessoa["nome"] = input("informe nome: ")
    pessoa["idade"] = int(input("informe a idade: "))
    pessoa["e-mail"] = input("informe o e-mail: ")
    pessoa["endereço"] = input("informe o endereço: ")
    pessoa["telefone"] = input("informe o telefone")

    agenda.append(pessoa)
    r = input("deseja continuar? (s/n) ")
    if r == "n":
        break

for contato in agenda:
    print (contato["nome"])