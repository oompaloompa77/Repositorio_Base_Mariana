#Colocar os dados necessários para formação do programa de pizzaria
#Infomar ao usuário quais as opções dos sabores de pizzas disponíveis
#Usuário escolher o sabor e digitar o código da opção escolhida
#Usar match-case para mostrar a opção dos sabores
#Imprimir resultado

print("Código de sabores disponíveis para pizza")
print("714 - Calabresa acebolada")
print("147 - Frango com catupiry")
print("1421 - Camarão gratinado com cogumelos")
print("2821 - Marguerita")
print("3528 - Quatro queijos")
print("4235 - Rúcula com tomate")
print("000 - Quero montar minha pizza. Monte sua pizza por 70,00. Fique a vontade para adicionar tudo que quiser, segue a lista de ingredientes que temos (molho de tomate, calabresa, bacon, lombo suíno, frango desfiado, azeitonas, brócolis, rúcula, tomate, alho frito, cebola em rodelas.)")
print("707 - O sabor desejado não foi encontado!")

código = int(input("Digite o código para o sabor escolhido: "))

match código:
    case 714:
        print("CALABRESA ACEBOLADA - DISPONÍVEL APARTIR DE - R$45,00")
    case 8:
        print("CEBOLA RETIRADA de sua pizza, fique tranquilo!")
    case 147:
        print("FRANGO COM CATUPIRY - DISPONÍVEL APARTIR DE - R$55,00 ")
    case 13:
        print("ADICIONAIS DE BACON - DISPONÍVEL APARTIR DE - R$5,00")
    case 1421:
        print("PIZZA DE CAMARÃO - DISPONÍVEL APARTIR DE - R$74,00")
    case 9:
        print("CAMARÃO EXTRA ADICIONADO - DISPONÍVEL APARTIR DE - R$7,00")
    case 2821:
        print("MARGUERITA - DISPONÍVEL APARTIR DE - R$60,00")
    case 3528:
        print("QUATRO QUEIJOS - DISPONÍVEL APARTIR DE - R$50,00")
    case 4235:
        print("RÚCULA COM TOMATE - DISPONÍVEL APARTIR DE - R$55,00")
    case 707:
        print("Desculpe não conseguir te ajudar, talvez em outro momento!")
    case 000 :
        pizza= input("Digite os ingredientes: ")
        print(f"Aproveite e tenha uma ótima pizza, {pizza}")
    case _:
        exit() #Encerrar o programa se for 707
        print("Desculpe não conseguir te ajudar, talvez em outro momento!")