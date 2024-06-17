a = float(input("Informe o valor da hora aula: "))
b = int(input("informe o numero de horas: "))
d = float(input("informe o total de descontos"))

sl = (a + b) - d 
print(f"o salario liquido é: {sl: .2f}")