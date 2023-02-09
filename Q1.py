#Ler 3 números do tipo float, calcular a sua média aritmetica, e imprmir os numeros juntamente com 
# o resultado. E se os números forem inteiros?

n1 = float(input('Number 1:'))
n2 = float(input('Number 2:'))
n3 = float(input('Number 3:'))

media = float((n1+n2+n3)/3)

print(n1, n2, n3, f'Média:', media)