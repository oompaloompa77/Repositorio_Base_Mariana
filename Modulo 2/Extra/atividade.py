import os
# os.mkdir('PROJETOS!')
# print('Pasta Criada')
open("Projetos!/TESTE/MATEMATICA.txt", "w").close()
open("Projetos!/PORTUGUES.txt", "w").close()
open("Projetos!/CIENCIAS.txt", "w").close()

arquivos = os.listdir()
for item in arquivos:
    print(item)

