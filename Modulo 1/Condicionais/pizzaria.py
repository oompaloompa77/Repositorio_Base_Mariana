# para desenvolver. Será um programa para a pizzaria, no local receberá: nome do cliente, endereço, opções (mussarela, calabresa, portuguesa, marguerita), deverá imprimir o nome do cliente,endereço o sabor escolhido

#Passo 1.nome do cliente
nome_do_cliente = input('Seja bem vindo! Qual o seu nome, por favor?')

#Passo 2. endereço
endereco = input('Endereço de entrega:')

#Passo 3. receber o pedido
pedido = input('Digite qual o sabor para sua pizza: \n'
'(Mussarela | Calabresa | Portuguesa | Marguerita) :')

print(f'Sr. {nome_do_cliente}, seu pedido será entregue no{endereco}, o sabor escolhido é {pedido}')

#Passo 4. opções (elief tradução para pt-br senão então)
if pedido == "Mussarela":
    print(f'Sr(a){nome_do_cliente}, o seu pedido será entregue no {endereco}, sabor escolhido é:{pedido}')
elif pedido == "Calabresa":
    print(f'Muito obrigado pelo seu pedido, {nome_do_cliente}. Nosso motoboy ja esta a caminho do {endereco}, com a sua pizza de {pedido}')
elif pedido == "Portuguesa":
print(f'Excelente escolha {nome_do_cliente}, a nossa pizza {pedido} chegara em breve na {endereco})
      else:
print(f'Oba! A pizza {pedido}, chegara quentinha na sua casa {endereco}, agradecemos pelo pedido {nome_do_cliente}')