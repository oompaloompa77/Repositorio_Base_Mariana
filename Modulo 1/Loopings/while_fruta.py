fruta = input("Charada: Qual é a fruta que é vermelha e que tem sementes?")

while fruta != 'morango':
    fruta = input('Qual é a fruta?')
    if fruta == 'morango':
        print('Você acertou!')
    else:
        print('Tente novamnete!')