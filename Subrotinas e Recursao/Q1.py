def separa(n):
    lis = []
    while n > 0:
        lis.insert(0, n % 10) 
        n = n // 10 
        #print(n, lis)  
    return lis

def ocorrencia(n, d):
    l = separa(n)
    qtd = 0
    for i in l:
        if i == d:
            qtd = qtd + 1
    return qtd

num = int(input('Numero: '))
while  num < 1 or num > 99999:
    num = int(input('Invalido. Numero: '))

while  num > 0:
    q = ocorrencia(num, 9)
    print(num, 'tem', q, 'digitos 9')
    num = int(input('Numero: '))
    while num > 99999:
        num = int(input('Invalido. Numero:'))