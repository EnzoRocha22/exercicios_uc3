a = float(input("Informe o valor total da compra "))
b = int(input("Informe o numero de parcelas "))

parcela = a / b

print(f"Voce deverá pagar: {parcela: .2f} durante {b} meses")