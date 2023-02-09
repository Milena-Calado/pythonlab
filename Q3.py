#Ler 3 numeros e imprmir o menor deles. Sua solução é facilmente escalável para uma grande quantidade
#de números?

#n1 = int(input('Number 1:'))
#n2 = int(input('Number 2:'))
#n3 = int(input('Number 3:'))

#condição tb possível
# n1 = int(input('num'))
# menor = n1

menor = 9999999999999999999
for i in range (3):
    n = int(input('Number:'))
    if n < menor:
         menor = n

print('O menor número é:', menor)
    
