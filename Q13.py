num1 = int(input('Numero 1:'))
num2 = int(input('Numero 2:'))

if num1 < num2 :
    mdc = num1
else: 
    mdc = num2

while num1 % mdc != 0 or num2 % mdc != 0:
    mdc = mdc -1
print('Resultado:', mdc)


