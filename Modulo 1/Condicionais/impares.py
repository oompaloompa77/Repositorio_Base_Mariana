#Gerar números ímpares de acordo com o número digitado pelo usuário 
x = 1
contador = 0

x = 1
contador = 0
quantidade_ímpares = int(input("Digite a quantidade de números ímpares que deseja gerar:"))
while contador < quantidade_ímpares:
    print(x)
    x += 2
    contador += 1 