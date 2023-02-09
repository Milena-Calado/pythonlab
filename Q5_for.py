#Calcular o fatorial de um numero inteiro lido
#Usando for

num = int(input('Digite o numero que deseja o fatorial:'))

resultado=1
for n in range(1, num+1):
    resultado = resultado * n

print('O fatorial de',num, 'é:',resultado)