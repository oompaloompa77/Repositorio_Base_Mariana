print('Adição - 1')
print('Subtração - 2')
print('Múltiplicação - 3')
print('Divisão - 4')

escolha = int(input('Digite o código desejado para a utilização da calculadora: '))
opções = int(input("Digite o número: "))
segundo_valor = int(input("Digite o número: "))

match escolha:
        case 1:
            try:
                print(f'{opções} + {segundo_valor} = {opções + segundo_valor}')
            except:
                print(f'Não é possível realizar esse cálculo, por favor tente novamente')

        case 2:
            try:
                print(f'{opções} - {segundo_valor} = {opções - segundo_valor}')
            except:
                print(f'Não é possível realizar esse cálculo, por favor tente novamente')

        case 3:
            try:
                print(f'{opções} x {segundo_valor} = {opções * segundo_valor}')
            except:
                print(f'Não é possível realizar esse cálculo, por favor tente novamente')

        case _:
            try:
                print(f'{opções} / {segundo_valor} = {opções / segundo_valor}')
            except:
                print(f'Não é possível realizar esse cálculo, por favor tente novamente')