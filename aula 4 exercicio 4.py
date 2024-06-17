"""""
def funcao():
    pass
resp = ""
while True:
    print("entrei")
    if resp == "s":
        pass
    print("outro comando")

print("fim") 
""""" 


resp = ''
ts = 0
tf = 0
quantidade = 0
while True:
    salario = float(input("informe o salario "))
    filhos = int(input("informe o numero de filhos "))
    ts = ts + salario 
    tf = tf + filhos
    quantidade += 1 
    resp = input("deseja continuar (s/n) ").lower()
    if resp == 'n':
        break

ms = ts / quantidade
mediafilhos = tf / quantidade
print(f"q média de salários a {ms:.2f}")
print(f"a média de filhos é {mediafilhos:.2f}")
print("fim")