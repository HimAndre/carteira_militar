import flet as ft
from random import randint
import sqlite3

def main(pagina: ft.Page):
    pagina.title = "Cadastro Pessoal"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    #entra aqui os campos de input
    nome = ft.TextField(label="Nome", width=300)
    idade = ft.TextField(label="Idade", width=300)
    om = ft.TextField(label="Om", width=300)
    patente = ft.TextField(label="Patente", width=300)
    nip= ft.TextField(label="Nip",width=300, read_only=True)

    
    def gerar_nip():
        cpf = ''.join(str(randint(0,9)) for x in range(9))
        return cpf        
        
        
    def salvar_dados(e):
        nip.value = gerar_nip()
        dados = f"Nome {nome.value}, idade {idade.value}, om {om.value}, patente {patente.value}, NIP: {nip.value}"
        #usei o value para poder capturar os valores 
        print(dados)
        
        # atraves desse conjunto de codigos abaixo consigo pegar os inputs do usuario e colocar em um BD
        banco = sqlite3.connect("banco_militares")
        cursor = banco.cursor()
        
        cursor.execute("CREATE TABLE IF NOT EXISTS militares (nome TEXT,idade INTERGER,om TEXT, patente TEXT,nip INTEGER)")
        cursor.execute("INSERT INTO militares (nome,idade,om,patente,nip) VALUES (?,?,?,?,?)",(nome.value, str(idade.value), om.value, patente.value,str(nip.value)))
        
        banco.commit()
                      
                      
        retorno_salvar = ft.AlertDialog(      #ft.AlertDialog cria janelas pop=up
            title=ft.Text("Dados salvos com sucesso"),
            content=ft.Text(dados),
        )
        # em tentativa e erro consegui exibir mensagem ao salvar os dados
        # retorno_salvar precisou ser criado dentro da funçao salvar 
        pagina.dialog = retorno_salvar # associa o pop-up com à página 
        retorno_salvar.open=True #força abertura do pop-up
        pagina.update()
        
    botao_salvar = ft.ElevatedButton(text="Salvar", on_click=salvar_dados)
    
    pagina.add(
        ft.Column(
            [nome, idade, om, patente,nip, botao_salvar],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
# de forma basica este é o caminho para receber as informaçoes     

ft.app(target=main)

