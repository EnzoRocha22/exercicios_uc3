peso = float(input("informe o seu peso"))
altura = float(input("Informe a sua altura"))
sexo = input("qual seu sexo: ")
if sexo.upper() == "M":
    peso_ideal = (72.7*altura)-58
    print(f"seu peso ideal é {peso_ideal}")
elif sexo.upper() == "F":
    peso_ideal = (67.1*altura)-44.7
    print(f"Seu peso ideal é {peso_ideal}")
else:
    print("Sexo não identificado.")