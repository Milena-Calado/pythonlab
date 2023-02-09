#Somar os inteiros pares entre 50 e 100 (inclusive)

#Usando for

soma = 0
for i in range(50, 102, 2):
    soma = soma + i
    print(soma)

print(f'A soma dos números pares é:',soma)

