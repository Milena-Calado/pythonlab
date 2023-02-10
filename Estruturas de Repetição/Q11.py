#Calcular o menor de uma serie de numeros inteiros lidos. A leitura dos numeros deve parar
#quando o numero zero for lido
soma = 0
qtd = 0
n1 = int(input('Informe um numero: '))
while n1 == 0:
    n1 = int(input('Infome outro numero:')) 
while n1!= 0:
    
    n1 = int(input('Infome outro numero:')) 
    
menor = 9999999999999999999
for i in range(1, n1+1):
    
    if n1 < menor and n1 != 0:
        menor = n1
 
print('O menor número é:', menor)

