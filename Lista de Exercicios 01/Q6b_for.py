num = 2
den = 500
soma = 0.0
n = int(input('Num de termos: '))
while n < 1 or n > 50:
    n = int(input('Invalido, digite o Num de termos positivos:'))

for i in range(1, n+1):
    soma = soma + num / den
    den = den - 10
    if i % 2 == 1:
        num = -5
    else:
        num = 2
    
print('Resultado:', soma)