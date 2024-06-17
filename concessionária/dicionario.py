from funcoes import cadastrar, listar, marca, listarveiculos, listarmarca
import os 

frota = []



while True:
    os.system("cls" if os.name == 'nt' else 'clear')
    print("concessionária")
    print("1 - Cadastrar Veiculos")
    print("2 - Listar veiculos")
    print("3 - Cadastrar Marca")
    print("4 - Listar Marca")
    print("0 - Sair")
    try:
        opcao = input("digite a opção: ")
        match(opcao):
            case '1':
                cadastrar()
            case '2':
                listarveiculos()
            case "3":
                marca()
            case "4":
                listarmarca()
            case '0':
                print("até a proxima.")
                break
            case _:
                print("opção inválida.")
    except:
        print("Erro na seleção da opção.")
        