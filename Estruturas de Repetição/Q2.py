#Ler 2 numeros inteiros e calcular o resto da divisão do primeiro pelo segundo. Se o resto for zero
#imprimir o primeiro numero, senão imprimir o quadrado do resto. Existe uma situação que pode causar 
#problemas: pense se seu programa está preparado para lidar com isso.

n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Digite outro numero inteiro:'))
while n2 == 0:
    n2 = int(input('n2 inválido, Digite um número válido:'))

div = n1 % n2

if div == 0:
    print('Resultado:', n1)
else:
    print('Resultado:', div**2)
