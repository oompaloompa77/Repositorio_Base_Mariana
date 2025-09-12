nome = ['Joaquim', 'Maria', 'Ana', 'José']

print(nome[0]) # Joaquim
print(nome[1]) # Maria
print(nome[2]) # Ana

nome [0] = "João" # estava Joaquim
nome [1] = "Lucas" # estava Maria
nome [2] = "Patrícia" # estava Ana

print(nome[0]) # alterado para João
print(nome[1]) # alterado para Lucas
print(nome[2]) # alterado para Patrícia

nome.append("Andressa")
nome.append("Jorge")

print(nome[0]) 
print(nome[1])
print(nome[2])
print(nome[3])
print(nome[4])
print(nome[5])

nome.insert(1, "Fernanda") #Insere "Fernanda na posição 1"
print("Após insert: ", nome)

#Modificando elementos 
nome[2] = "Paulo" #Modifica o elemento na índice 2
print("Ápos modificação: ", nome)

#Removendo elementos
del nome[3] #Remove o elemento no índice 3
print("Àpos del: ", nome)

nome.remove("João") #Remove a primeira ocorrência de "Maria"
print("Àpos remove: ", nome)

removido = nome.pop(2) #Remove e reorna o elemento no índice 2
print(f"Após pop (removido '{removido}'):", nome)

nome.clear() #Esvazia a lista
print("Após clear:", nome)