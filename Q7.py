#Somar os inteiros impares entre dois valores inteiros informados pelo usuário
#usando for 
soma = 0  
n1 = int(input('Numero 1:'))
n2 = int(input('Numero 2:'))

if n2 < n1:
    n1, n2 = n2, n1
if n1 % 2 == 0:
    aux = n1 + 1
else: 
    aux = n1 

for i in range(aux, n2 + 1, 2):
    soma = soma + i

print('Resultado da soma é:',soma, 'para intervalo entre', n1, 'e', n2)

#usando while




