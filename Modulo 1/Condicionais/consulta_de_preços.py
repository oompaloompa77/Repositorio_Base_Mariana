#Exibe os códigos disponíveis

print("Códigos de produtos: ")
print("1 - Café")
print("2 - Chá")
print("3 - Suco")
print("4- Refrigerante")
print("5- Àgua")
print("0 - Sair")

#Solcita o código do produto ao usuário
código = int(input("Digite o código do produto: "))

#Usa math-case para mostrar o preço com base no código
match código:
    case 1:
        print("Produto: Café - Preço: R$ 4,50")
    case 2:
        print("Produto: Chá - Preço: R$ 3,00")
    case 3:
        print("Produto: Suco - Preço: R$ 5,00")
    case 4:
        print("Produto: Refrigerante - Preço: R$ 6,00")
    case 5:
        print("Produto: Àgua - Preço: R$ 2,00")
    case 0:
        print("Saindo do programa...")
        exit() #Encerra o programa se o código for 0
    case _:
        print("Código inválido. Por favor, tente novamnete.")