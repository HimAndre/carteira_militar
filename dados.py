class Militar:
    def __init__(self, nome, idade, om, patente):
        self.nome = nome
        self.idade = idade
        self.om = om
        self.patente = patente


def Cadastro():
    nome = input('Qual e o nome do militar:')
    idade = input('Qual e a idade:')
    om = input('OM do mil:')
    patente = input('Qual a patente do MIL:')
    return Militar(nome, idade, om, patente)


cadastro = input('Deseja cadastrar o militar?:').lower()

if cadastro == "sim": 
    militar_cadastrado = Cadastro()
    
descricao = input('''Deseja visualizar o cadastro do MIL?
[S] ou [N]''').upper()

if descricao == "S":
    print('Nome=',militar_cadastrado.nome)
    print('Nome=',militar_cadastrado.idade)
    print('Nome=',militar_cadastrado.om)
    print('Nome=',militar_cadastrado.patente)

nip = input("Deseja atribuir um nip ao militar?")
if nip == 'sim':
        
    import random

    x1 = str(random.randint(0,9))
    x2 = str(random.randint(0,9))
    x3 = str(random.randint(0,9))
    x4 = str(random.randint(0,9))
    x5 = str(random.randint(0,9))
    x6 = str(random.randint(0,9))
    x7 = str(random.randint(0,9))
    x8 = str(random.randint(0,9))

    nip = (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8)

    print(nip)
