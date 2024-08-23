import flet as ft
import random

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
        x1 = str(random.randint(0,9))
        x2 = str(random.randint(0,9))
        x3 = str(random.randint(0,9))
        x4 = str(random.randint(0,9))
        x5 = str(random.randint(0,9))
        x6 = str(random.randint(0,9))
        x7 = str(random.randint(0,9))
        x8 = str(random.randint(0,9))
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8)
#tive que usar o RETURN para puxar o numero randomico 

    def salvar_dados(e):
        nip.value = gerar_nip()
        dados = f"Nome {nome.value}, idade {idade.value}, om {om.value}, patente {patente.value}, NIP: {nip.value}"
        #usei o value para poder capturar os valores 
        print(dados)
        
        retorno_salvar = ft.AlertDialog(      #ft.AlertDialog cria janelas pop=up
            title=ft.Text("Dados Salvos com sucesso"),
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

