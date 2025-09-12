#falando de acumuladores
soma = 0 #acumulador precisa sempre ser iniciado com 0
x = 0
while x <10:
    x = int(input(f'Digite {x} um número: '))
    soma = soma + x
print(f"A soma dos números de 1 a 10 é {soma}")