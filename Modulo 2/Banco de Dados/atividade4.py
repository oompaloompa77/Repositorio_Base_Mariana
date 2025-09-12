import sqlite3


conn = sqlite3.connect('loja.db')
cursor = conn.cursor()


print("Produto e cliente de todas as vendas:")
# cursor.execute("SELECT produto, cliente FROM vendas")
for produto, cliente in cursor.fetchall():
    print(f"Produto: {produto}, Cliente: {cliente}")

print("\n")


print('Vendas realizadas pelo cliente "João":')
# cursor.execute("SELECT * FROM vendas WHERE cliente = 'João'")
vendas = cursor.fetchall()
if vendas:
    for venda in vendas:
        print(venda)
else:
    print("Nenhuma venda encontrada para o cliente João.")

print("\n")


print("Produtos com preço unitário maior que 50:")
# cursor.execute("SELECT produto FROM vendas WHERE preco_unitario > 50")
produtos = cursor.fetchall()
for (produto,) in produtos:
    print(produto)


conn.close()