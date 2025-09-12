#Média com while
# 'nota_total' é o acumulador de notas
nota_total = 0
bimestre = 0

while bimestre < 4:
    nota = float(input('Digite a nota do aluno: '))
    nota_total += nota #Acumulado a nota total
    bimestre += 1
    print(f'A {nota} digitada do aluno foi armazenada com sucesso!')

média = nota_total / 4 #Calcular a média ápos sair do loop
print(f'A média do aluno é {média}')