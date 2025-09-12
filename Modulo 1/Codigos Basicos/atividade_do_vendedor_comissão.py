#Pedindo o nome do vendedor
print(input('Digitar o nome do vendedor: '))
print('-------------------------------------------')

#Pedindo o salario fixo do vendedor
salario = float(input('Digitar o salario fixo do vendedor: '))
print('----------------------------------------------')

#Pedindo o total de vendas efetuadas no mês em dinheiro
total_vendas = float(input('Digite o total de vendas'))
print('-----------------------------------------------')

#Calcular as vendas em comparação a comissao que é de 15%
comissao = total_vendas * 0.15
print('----------------------------------------------------------')

#imprimir o valor final que o vendedor ganha no mês
valor_final = total_vendas + comissao
print('Valor final',valor_final)