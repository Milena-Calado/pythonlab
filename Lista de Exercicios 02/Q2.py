#Ler o nome do usuário e imprimi-lo em formato de escala, ou seja, só a primeira letra na primeira linha 
#as duas primeiras letras na segunda linha e assim por diante.

nome = str(input("Digite seu nome: "))

for i in range(len(nome)):
    print(nome[:i+1])


#outra resolução
# for i in range(len(nome)):
#     for j in range (i+1):
#         print(nome[j], end='')
#     print()





