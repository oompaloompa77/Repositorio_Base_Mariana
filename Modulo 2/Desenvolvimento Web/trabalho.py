import json
ARQUIVO = 'dados.json'

with open(ARQUIVO, "a+") as arquivo:
    arquivo.seek(0)
    try:
        json.load(arquivo)
    except:
        arquivo.write("[]")

def carregar():
    with open(ARQUIVO, "r") as arquivo:
        return json.load(arquivo)
    
def salvar(dados):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(dados, arquivo)

def criar():
    nome = input("Nome: ")
    idade = input("Idade: ")
    tamanho = input("Tamanho: ")
    modelo = input("Modelo: ")

    dados = carregar()
    dados.append({"nome": nome, "idade": idade, "tamanho": tamanho, "modelo": modelo})
    salvar(dados)
    print("Salvo!")

def menu():
    while opcao !=5:
        opcao = int(input("Selecione uma opção: \n 1- Criar \n  2- Listar \n 3- Atualizar \n 4- Deletar"))
        if opcao == 1:
                criar()
        elif opcao == 2:
                listar()
        elif opcao == 3:
                atualizar()
        elif opcao == 4:
                deletar()
        elif opcao == 5:
                break











nome = input('Por favor, digite seu nome: ')
idade = int(input('Por favor, digite sua idade: '))
tamanho = input('Digite o tamanho da jaqueta: ')
modelo = input('Digite o modelo da jaqueta que você gostaria: ')