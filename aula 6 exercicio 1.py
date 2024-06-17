"""1) Faça um programa que fará a leitura de indeterminados números e esses números serão armazenados em um vetor.
Quando o usuário digitar 0, o programa interromperá a leitura e irá imprimir o somatório dos números e a quantidade de elementos.
"""

vetor = []

while True:
    numero = int(input("digite um numero "))
    vetor.append(numero)
    if numero == 0: 
        break

soma = 0
for n in vetor: 
    soma += n 

quantidade = len(numero)

print(f"soma nos elementos é {soma}")
print(f"a quantidade de elementos: ")
