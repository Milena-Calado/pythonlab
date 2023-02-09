#Calcular o valor de S com N termos, onde N é informado pelo usuário e: S = 1 + 3/2 + 5/3 + 7/4...
#usando for 

num = 1
den = 1
soma = 0.0
n = int(input('Num de termos: '))
while n < 1 or n > 50:
    n = int(input('Invalido, digite o Num de termos positivos:'))

for i in range(1, n+1):
    soma = soma + num / den
    den = den + 1
    if i % 2 == 1:
        num = num + 2
    else:
        num = 1
    
print('Resultado:', soma)