import math
n1 = int(input('Numero: '))
raiz = int(math.sqrt(n1))
div = 2

while div <= raiz and n1 % div != 0:
    div = div + 1
if div > raiz:
    print(n1, 'é um numero primo e foi testado até', div)
else:
    print(n1, 'não é um número primo e', div, 'é um divisor')
