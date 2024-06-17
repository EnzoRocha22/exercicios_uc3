n = int(input("informe um numero "))
n2 = int(input("informe outro numero "))
op = (input("informe um operador "))

r = 0
match op:
    case "+":
        r = n + n2
        (print(f"{n} + {n2} = {r}"))
    case "-":
        r = n - n2
        print(f"{n} - {n2} = {r}")
    case "*":
        r = n * n2
        print(f"{n} *  {n2} = {r}")
    case "/":
        if n2 != 0:
            r = n / n2
        print(f"{n} / {n2} = {r}")
    case _:
        print("operador inválido")
        