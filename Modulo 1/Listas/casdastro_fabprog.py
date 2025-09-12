#Fazer um programa que imprima o nome da pessoa com o seu cadastro.
#Exixbir todos os nomes de pessoas cadastradas na lista.
#Modificar um nome apresentado na lista.
#Solicitar o nome da pessoa que será exclída da lista, excluir.
#Encerrar o programa.

nomes = ["Helena", "Letícia", "Rebecca", "Rodrigo", "Samuel", "Matheus"]

print('')
print('Menu')
print('1 - Cadastro')
print('2 - Lista de contatos')
print('3 - Excluir contatos')
print('4 - Sair do programa')

removendo = int(input("Digite o código: "))

match removendo:
    case 1:
        nome = input('Digite um nome: ')
        nome.append (nome)
        print('Salvo: ')
        print('Nova lista', nomes)
    case 2:
        print(nomes)
    case 3:
        print("Helena", "Letícia", "Rebecca", "Rodrigo", "Samuel", "Matheus")
        nome_remove = input("Digite o nome que você deseja excluir: ")
        if nome_remove in nomes:
            nomes.remove(nome_remove)
            print(f'{nome_remove}, foi removido com sucesso!')
            print("Nova lista: ", nomes)
        else:
            print("ERRO...Nome não encontrado!")
        
    case _:
        print("Encerrando programa...")