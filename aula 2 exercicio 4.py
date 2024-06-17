codigo = input("informe o seu codigo de funcionário: ")
salario = float(input("Informe o seu salario: "))
cargo = input("informe o seu cargo: ")

if cargo.capitalize() == "Gerente" and codigo == 101:
    salario_novo = salario+(salario*0.10)
elif cargo.capitalize() == "Engenheiro" and codigo == 102:
    salario_novo = salario+(salario*0.20)
elif cargo.capitalize() == "Tecnico" and codigo == 103:
    salario_novo = salario+(salario*0.30)
else:
    salario_novo = salario+(salario*0.40)
print(f"seu novo sálario é: {salario_novo} e o antigo é de {salario}")