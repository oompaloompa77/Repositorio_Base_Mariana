#1. pedir o numero de qual tabuada faremos
#2. Digitar da onde a tabuada deve começar
#3. Digitar da onde a tabuada deve encerrar
#4. Imprimir o resultado final da tabuada

numero = int(input('Digite a tabuada que iremos fazer:' ))

i = int(input('Onde deseja começar a tabuada que iremos fazer?: '))

termino = int(input('Onde deve encerrar a tabuada que iremos fazer?: '))

while i <= termino:
    print(f' {i} x {numero} = {i * numero}')
    i += 1

