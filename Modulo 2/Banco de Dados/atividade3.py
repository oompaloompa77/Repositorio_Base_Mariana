import sqlite3


conn = sqlite3.connect('escola.db')
cursor = conn.cursor()


print("Nome e nota de todos os alunos:")
# cursor.execute("SELECT nome, nota FROM alunos")
for nome, nota in cursor.fetchall():
    print(f"Nome: {nome}, Nota: {nota}")

print("\n")

print("Dados do aluno com id = 3:")
# cursor.execute("SELECT * FROM alunos WHERE id = 3")
aluno = cursor.fetchone()
if aluno:
    print(aluno)
else:
    print("Aluno com id = 3 não encontrado.")

print("\n")


print("Alunos da turma 'B' com nota maior ou igual a 7:")
# cursor.execute("SELECT * FROM alunos WHERE turma = 'B' AND nota >= 7")
for aluno in cursor.fetchall():
    print(aluno)


conn.close()