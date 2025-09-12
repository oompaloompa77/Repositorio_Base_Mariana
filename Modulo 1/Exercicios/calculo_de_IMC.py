nome_do_cliente = input('Ola!Seja bem vido!Gostaria de monitorar o seu IMC? \n Se sim, me diga o seu nome por favor.')


peso = float(input('Me diga o seu peso:'))
#print(peso)

altura = float(input('Agora a sua altura:'))
#print(altura)

imc = peso / (altura **2)
print(imc)

#exibir:
#o valorcalculado
print(f'Segundo as informaçoes obtidas {nome_do_cliente}, seu IMC é de {imc}')

#exibir:
##uma mensagem de orientaçao com base no resultado

if imc < 18.5 :
    print(f'Segundo as dados fornecidos, {nome_do_cliente}, seu IMC está abaixo do peso')

elif  18.5 <= imc <= 24.9 :
    print(f'Segundo as dados fornecidos, {nome_do_cliente}, seu IMC está normal 🚀')

elif 25.0  <= imc <= 29.9:
    print(f'Segundo as dados fornecidos, {nome_do_cliente}, seu IMC está com sobrepeso')

elif 30.0 <= imc <= 34.9 :
    print(f'Segundo as dados fornecidos, {nome_do_cliente}, seu IMC está com obesidade Grau I')

elif  35.0 <= imc <= 39.9  :
    print(f'Segundo as dados fornecidos, {nome_do_cliente}, seu IMC está com obesidade Grau II ⚠️')

else:
    print(f'Segundo as dados fornecidos, {nome_do_cliente}, que seu IMC está obesidade Grau III (mórbida)')



