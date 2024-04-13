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
