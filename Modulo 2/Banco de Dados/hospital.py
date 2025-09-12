# import sqlite3

# banco = sqlite3.connect('hospital.db')
# cursor = banco.cursor()

# cursor.execute("SELECT nome, cidade FROM pacientes WHERE cidade = 'São Paulo'")

# resultado = cursor.fetchall()

# for linha in resultado:
#     print(linha)

# banco.close()

# import sqlite3

# banco = sqlite3.connect('hospital.db')
# cursor = banco.cursor()

# cursor.execute("SELECT nome, diagnostico FROM pacientes WHERE idade > 40")

# resultado = cursor.fetchall()

# for linha in resultado:
#     print(linha)

# banco.close()

# import sqlite3

# banco = sqlite3.connect('hospital.db')
# cursor = banco.cursor()

# cursor.execute("SELECT nome, plano_saude FROM pacientes WHERE plano_saude = 'Unimed'")

# resultado = cursor.fetchall()

# for linha in resultado:
#     print(linha)

# banco.close()

# import sqlite3

# banco = sqlite3.connect('hospital.db')
# cursor = banco.cursor()

# cursor.execute("SELECT nome, data_internacao FROM pacientes ORDER BY data_internacao ASC")

# resultado = cursor.fetchall()

# for linha in resultado:
#     print(linha)

# banco.close()

# import sqlite3

# banco = sqlite3.connect('hospital.db')
# cursor = banco.cursor()

# cursor.execute("SELECT nome, DIAGNOSTICO FROM pacientes WHERE diagnostico = 'Fratura'")

# resultado = cursor.fetchall()

# for linha in resultado:
#     print(linha)

# banco.close()

import sqlite3

banco = sqlite3.connect('hospital.db')
cursor = banco.cursor()

cursor.execute("SELECT nome, medico_responsavel FROM pacientes WHERE medico_responsavel = 'Dr. João'")

resultado = cursor.fetchall()

for linha in resultado:
    print(linha)

banco.close()