#Ler 2 vetores de tamanho N, com N informado pelo usuário antes, somar os 2 vetores, imprimir os 2 vetores
# e depois o vetor resultado

n = int(input('Tamanho:'))
while n < 1:
    n = int(input('Inválido, tamanho:'))

v1 = [0]*n
v2 = [0]*n
vres = [0]*n

for i in range(n):
    v1[i] = int(input('V1 elemento' +str(i) + ': '))
for i in range(n):
    v2[i] = int(input('V2 elemento' +str(i) + ': '))
    vres[i] = v1[i] + v2[i]

print('V1 =', v1)
print('V2 =', v2)
print('Soma =', vres)