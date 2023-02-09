#Calcular o fatorial de um numero inteiro lido
#Usando While

num = int(input('Digite o numero que deseja o fatorial:'))

resultado = 1
count = 1

while count <= num:
    resultado *= count
    count += 1

print('O fatorial de',num, 'é:',resultado)