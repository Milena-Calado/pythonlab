#Calcular a media aritmetica de varios numeros reais fornecidos pelo usuário. 
#A leitura dos numeros deve parar quando um numero negativo for lido.
soma = 0.0
qtd = 0
num = float(input('Infome um numero:'))
while num < 0:
    num = int(input('Invalido, Infome outro numero:'))
while num >= 0:
    soma = soma + num
    qtd = qtd + 1
    num = int(input('Infome outro numero real:'))

#outra resolução do problema de inserir um negativo primeiro
# if qtd > 0:
#     soma = soma / qtd
#     print('Resultado:', soma)
# else: 
#     print('Dados informados não sao validos')



