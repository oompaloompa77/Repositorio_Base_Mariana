import sqlite3 as funcionarios

banco = funcionarios.connect('empresa.db')

cursor = banco.cursor()

cursor.execute("SELECT nome, salario FROM funcionarios")
for nome, salario in cursor.fetchall():
    print(f'Nome: {nome}, Salário: {salario}')

cursor.execute("SELECT * FROM funcionarios WHERE nome = 'Carla'")
dados = cursor.fetchall()
if dados:
    for linha in dados:
        print(linha)
else:
    print("Funcionária Carla não encontrada.")

cursor.execute("SELECT nome, cargo FROM funcionarios WHERE DEPARTAMENTO = 'TI")
for nome, cargo in cursor.fetchall():
    print(f"Nome: {nome}, Crgo: {cargo}")

banco.close()