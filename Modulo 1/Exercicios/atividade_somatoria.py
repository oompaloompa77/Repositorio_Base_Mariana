#1. Criar um programa para monitorar sua saúde com base no cálculo do IMC (Índice de Massa Corporal).
#2. Receber a variável do peso (kg).
#3. Receber a variável de altura (m).
#4. Fazer o cálculo de IMC com base nos valores apresentados.
#5. Imprimir o valor do IMC.


nome = str(input('Por Favor, digite seu nome: '))
peso = float(input('Insira o peso: '))
print(peso)
print('------------------------------------')
altura = float(input('Insira sua altura: '))
print(altura)
print('------------------------------------')
imc = peso / (altura**2)
print(imc)
print('----------------------------------')
if imc < 18.5 : 
    print('Você está abaixo do peso!')

elif 18.5 <= imc <= 24.9: 
    print(f'Sr(a) {nome} com base nas informções coletadas... Parabéns seu peso está normal!!')

elif 25 <= imc <= 29.9 : 
    print(f'Sr(a) {nome} com base nas informções coletadas... Infelizmente você está com sobrepeso!')

elif 30 <= imc <= 34.9 : 
    print(f'Sr(a) {nome} com base nas informções coletadas... Infelizmente você está com obesidade grau 1!')

elif 35 <= imc <= 39.9 :
    print(f'Sr(a) {nome} com base nas informções coletadas... Sinto muito, você está com obesidade grau 2!!')

else:
    print(f'Sr(a) {nome} com base nas informções coletadas... Sinto muito, você está com obesidade grau 3!!!')
