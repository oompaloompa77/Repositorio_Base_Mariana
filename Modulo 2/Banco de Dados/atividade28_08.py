import sqlite3
#UPDATE
# #Aumento de 10% do salario de funcionarios de TI
# conn = sqlite3.connect('ricardaofather.db')
# cursor = conn.cursor()
# cursor.execute("UPDATE  funcionarios SET salario = 'salario * 1.10' WHERE departamento = 'TI';")
#conn.commit()

# #Atualização do telefone
# conn = sqlite3.connect('ricardaofather.db')
# cursor = conn.cursor()
# cursor.execute("UPDATE funcionarios SET telefone = '(11) 98888-7777' WHERE cpf = '15967994960';")
# conn.commit()

# #Alterando a Ana
# conn = sqlite3.connect('ricardaofather.db')
# cursor = conn.cursor()
# cursor.execute("UPDATE funcionarios SET departamento = 'RH' WHERE cpf = '06212428809';")
# conn.commit()

# #Alterações de cargo (alterei a Raiane)
# conn = sqlite3.connect('ricardaofather.db')
# cursor = conn.cursor()
# cursor.execute("UPDATE funcionarios SET cargo = 'Analista' WHERE telefone = '(11) 98888-7777';")
# conn.commit()


# #DELETE
# conn = sqlite3.connect('ricardaofather.db')
# cursor = conn.cursor()
# cursor.execute("DELETE FROM funcionarios WHERE idade <=19;")
# conn.commit()

# conn = sqlite3.connect('ricardaofather.db')
# cursor = conn.cursor()
# cursor.execute("DELETE FROM funcionarios WHERE pnome = 'Victor' ;")
# conn.commit()

# conn = sqlite3.connect('ricardaofather.db')
# cursor = conn.cursor()
# cursor.execute("DELETE FROM funcionarios WHERE departamento = 'Marketing' ;")
# conn.commit()