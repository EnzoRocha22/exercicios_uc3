from conexao import conectar


def cadastrar():
    
    while True:
        veiculo = {}
        veiculo["nome"] = input("informe o nome do veiculo: ")
        veiculo["ano"] = int(input("informe o ano do veiculo: "))
        veiculo["valor"] = float(input("informe o valor do veiculo: "))
        veiculo['descricao'] = input("Descrição do veículo: ")
        veiculo["tipo"] = input("seu veiculo é usado ou 0km? ")
        
        
    
        #frota.append(veiculo)
        con = conectar()
        cursor = con.cursor()

        sql = "insert into veiculo (nome, valor, descricao, tipo) values (%s, %s, %s, %s)"
        cursor.execute(sql,(veiculo["nome"], veiculo['valor'], veiculo ["descricao"], veiculo ["tipo"]))
        con.commit()
        r = input("deseja continuar? (s/n)").lower()
        if r == "n":
            break


def listar(frota):
    for c in frota:
        for k, v in c.item():
            print (f"{k}: {v}")
            print("_"*50)

def marca():
    while True:
        nome = input("informe a marca: ")
        
        con = conectar()
        cursor = con.cursor()

        sql = "insert into marca (nome) values (%s)"
        cursor.execute(sql, (nome,) )
        con.commit()

        r = input("deseja continuar? (s/n) ").lower()
        if r == "n":
            break

def listarveiculos():
    con = conectar()
    cursor = con.cursor()

    sql = 'select * from veiculo order by nome desc'
    cursor.execute(sql)

    resultado = cursor.fetchall()
    for v in resultado:
        print(v)

def listarmarca():
    con = conectar()
    cursor = con.cursor()

    sql = "select * from marca order by nome"
    cursor.execute(sql)

    resultado = cursor.fetchall()
    for v in resultado:
        print(v)