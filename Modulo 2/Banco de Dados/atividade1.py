import sqlite3 as funcionarios

banco = funcionarios.connect('banco.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (nome TEXT, idade INTEGER, email TEXT, sala_de_aula TEXT, escola TEXT)")

cursor.execute("INSERT INTO pessoas VALUES ('Taylor', 19, 'taylor@gmail.com', 'laranja', 'Ruth de Azevedo Silva Rodriguês')")

banco.commit()

cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())
