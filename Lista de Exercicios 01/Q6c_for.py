#Calcular o valor de S com N termos, onde N é informado pelo usuário e: S = 37*38/1 + 36*37/2 + 35*36/3...
#usando for


num = 37
numerador = 38
den = 1
soma = 0.0
n = int(input('Num de termos: '))
while n < 1 or n > 50:
    n = int(input('Invalido, digite o Num de termos positivos:'))

for i in range(1, n+1):
    soma = soma + num * numerador / den
    numerador = numerador - 1
    num = num - 1
    den = den + 1
    # if i % 2 == 1:
    #     num = num + 1
    # else:
    #     num = 1
    
print('Resultado:', soma)


