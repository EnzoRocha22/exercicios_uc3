print("Lojas Tabajara")

while True:
    total = 0
    contador = 1
    preco = float(input(f"Produto {contador} (digite 0 para finalizar): R$ "))
    
    
    while preco != 0:
        total += preco
        contador += 1
        preco = float(input(f"Produto {contador} (digite 0 para finalizar): R$ "))
    
    print(f"Total: R$ {total:.2f}")
    
    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total
    
    print(f"Troco: R$ {troco:.2f}\n")