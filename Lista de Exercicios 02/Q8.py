# Ler uma sequencia de numeros inteiros positivos(ou zero). A leitura deve parar com uma digitação 
# de um numero negativo. Seu programa deve imprimir os números lidos cujos valores tem dois digitos 
# significativos, mas na ordem inversa em que forem lidos - o ultimo lido deve ser o primeiro a ser impresso.

numeros = []

n = int(input('Insira um Numero, se for negativo pára: '))

while n >= 0:
    if n > 9 and n < 100:
        numeros.append(n) #também poderia usar insert para já entrar na posição zero.
    n = int(input('Insira um Numero, se for negativo pára: '))

#for i in range(len(numeros -1, -1, -1)) - outra forma de resolver para inverter a ordem
#   print (numeros[i], '', end='')
numeros.reverse() #inverte para que o ultimo digitado seja o primeiro da lista

print(numeros)






