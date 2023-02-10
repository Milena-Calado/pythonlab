#Ler uma lista de N numeros (N é informado pelo usuario antes), e depois criar duas outras listas com os 
#numeros pares e impares separados. No final imprimir as 3 listas 

n = int(input('Tamanho:'))
while n < 1:
    n = int(input('Inválido, tamanho:'))

v1 = [0]*n
par = [0]*n
imp = [0]*n
qtd_par = qtd_imp = 0

for i in range(n):
    v1[i] = int(input('V1 elemento' +str(i) + ': '))
    if v1[i] % 2 == 0:
        par[qtd_par] = v1[i]
        qtd_par = qtd_imp + 1
    else:
        imp[qtd_imp] = v1[i]
        qtd_imp = qtd_imp + 1

par = par[:qtd_par]
imp = imp[:qtd_imp]

print('Lidos =', v1)
print('Pares =', par)
print('Impares =', imp)

