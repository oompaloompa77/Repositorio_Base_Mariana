peso = float(input('Digite seu peso:' ))
print(peso)

altura = float(input('Digite sua altura: '))
print(altura)

try: 
    imc = peso / (altura**2)
    print(imc)

except:
    print('Desculpe, não foi possível fazer o cálculo! Tente Novamente em alguns instantes...')