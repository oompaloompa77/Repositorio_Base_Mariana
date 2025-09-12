def mostrar_linha():
   '''
   Mostrar uma linha de separação
   '''

   print('-' * 50)

#Exemplo de uso da função mostrar_linha
mostrar_linha()

print("Aluguel de carros com a maior frata do Brasil | Localiza")

mostrar_linha()

nome = input("Digite seu nome: ")

mostrar_linha()

print(f"Olá, {nome} ! Estamos felizes em tê-lo conosco.")

mostrar_linha()

print("Selecione o carro que deseja alugar: ")

mostrar_linha()

print('1 - BMW')
print('2 - MUSTANG')
print('3 - HB20')
print('4 - FUSCA')
print('5 - CIVIC')
print('0 - SAIR')

selecionar = int(input("Selecione o carro que você deseja alugar: "))

match selecionar:
   case 1:
      print('A BMW (Bayerische Motoren Werke), uma empresa alemã, é conhecida por fabricar automóveis e motocicletas de luxo, sendo uma das marcas mais respeitadas no mundo.')

   case 2:
      print('O Ford Mustang é um automóvel desportivo icónico, conhecido por sua história e popularidade.')

   case 3:
      print('O Hyundai HB20 é um carro subcompacto lançado em 2012, desenvolvido e produzido exclusivamente para o mercado brasileiro.')

   case 4:
      print('O Volkswagen Fusca, também conhecido como "Carocha" em Portugal, é um icónico automóvel da Volkswagen, produzido desde 1938 até 2003.')

   case 5:
      print('O Honda Civic é um sedan compacto, conhecido pela sua confiabilidade, bom desempenho e conforto, sendo um dos modelos mais populares da Honda.')

   case _:
      exit() #Encerrar o programa se for 0
      print('Ok, saindo do programa!')