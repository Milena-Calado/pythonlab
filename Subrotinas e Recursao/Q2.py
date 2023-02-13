def inverte(n):
    inverter = 0
    while n > 0:
        inverter = inverter * 10 + (n%10)
        n = n // 10 
        #print(n, inverter)  
    return inverter

num = int(input('Numero: '))
while  num < 100:
    num = int(input('Invalido. Numero: '))

for i in range(100, num + 1):
    if i == inverte(num):
        print(num, 'é palindromo')
    else: 
        print(num, 'não é palindromo')
   
    