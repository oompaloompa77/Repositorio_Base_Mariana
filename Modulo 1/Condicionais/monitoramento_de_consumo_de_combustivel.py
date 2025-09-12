#Criar um programa que faça o monitoramento de combustivel
#Perguntar a pessoa a distância percorrida (em km)
#Quantidade de combustivel gasto (em litros)
#O programa deve calcular o consumo_medio:
#< 8 = Alto consumo
#8 – 12 = Consumo moderado
#> 12 = Econômico
#Dizer o resultado final com: alto consumo, cxonsumo moderado, econômico


distância = input("Digite a distância percorrida (em km):" )
print('---------------------------------------------------------')
litros = input("Digite a quantidade de combustivel gasto (em litros):")
print("------------------------------------------------------------")
consumo_medio = (distância / litros)

if consumo_medio < 8  :
    print('Auto consumo')

elif consumo_medio <=12 :
    print('Consumo moderado')

else:
    print('Econômico')

