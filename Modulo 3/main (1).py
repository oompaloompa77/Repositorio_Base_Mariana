import os
import flet as ft #ft é apelido de flet

def main(page: ft.Page):
    page.title = "Paçoca" #nome do título
    page.theme_mode = "dark" #modelo/tema
    
    # Função para criar pastas
    def criar_pasta(e):
        texto = texto_recebido.value
        try:
            os.mkdir(texto)
            informativo.value = f"Pasta criada: '{texto}'"
        except FileExistsError:
            informativo.value = f"A pasta '{texto}' já existe."
        page.update()

    # Função de listar arquivos
    def listararquivos(e):
        arquivos = os.listdir()
        for item in arquivos:
            informativo.value =f"7     {arquivos}"
            page.update()

    # Função para criar arquivos
    def criar_arquivo(e):
        global texto
        texto = texto_recebido.value
        try:
            open(texto, "w").close()
            informativo.value = f"Arquivo criado: '{texto}'"
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

     # Função para renomear arquivos
    def renomear_arquivo(e):
        texto
        texto_novo = texto_recebido.value 
        try:
            os.rename(texto, texto_novo)
            informativo.value = f"Arquivo '{texto}' renomeado para '{texto_novo}'"
        except Exception as erro:
            informativo.value = f"Erro: {erro}"
        page.update()

    # Função para apagar arquivos
    def apagar_arquivo(e):
        texto = texto_recebido.value
        if os.path.exists(f'{texto}'):
            os.rmdir(texto)
        print("Arquivo apagado")
        page.update()

    # Campos e botões
    texto_recebido = ft.TextField(label="Escreva o nome do arquivo/pasta...")
    botao_pasta = ft.ElevatedButton("CRIAR PASTA", bgcolor="PURPLE", color="BLACK", width=200, on_click=criar_pasta)
    botao_arquivo = ft.ElevatedButton("CRIAR ARQUIVO", bgcolor="CYAN", color="BLACK", width=200, on_click=criar_arquivo)
    botao_listararquivos = ft.ElevatedButton("LISTAR ARQUIVO", bgcolor="WHITE", color="BLACK", width=200, on_click=listararquivos)
    botao_renomear = ft.ElevatedButton("RENOMEAR ARQUIVO", bgcolor="ORANGE", color="BLACK", width=200, on_click=renomear_arquivo)
    botao_apagar = ft.ElevatedButton("APAGAR ARQUIVO", bgcolor="BLUE", color="BLACK", width=200, on_click=apagar_arquivo)


    informativo = ft.Text("", size=20, color="white")

    # Layout
    #APAREÇA NO CÓDIGO
    page.add(
        ft.Row([texto_recebido], alignment="center"),
        ft.Row([botao_pasta, botao_arquivo, botao_listararquivos, botao_renomear, botao_apagar], alignment="center"),
        ft.Row([informativo], alignment="center")
    )

ft.app(target=main)