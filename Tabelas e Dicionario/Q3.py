# Ler uma tabela de alunos onde:
# - cada aluno tem um cpf (tipo long), um nome (string) e uma idade (inteiro).
# - a leitura da tabela pára com um cpf que não seja positivo.
# - Sabe-se que o usuário digitará no máximo 200 alunos.
# - Depois o usuário informará um inteiro positivo N, seguido por uma sério de N intervalos de idade (idades mínima e máxima).
# - O programa deve imprimir, para cada intervalo digitado pelo usuário, os dados dos alunos que se enquadram no intervalo seguidos pelo numero de alunos do intervalo.
# - Caso a idade minima de algum intervalo não seja menor do que a idade máxima, o programa deve imprimir uma mensagem de erro e continuar

tab = {}
n = idMax = idMin = qtd = 0

cpf = int(input('CPF: '))
while cpf <= 0:
    cpf = int(input('Digite um CPF válido: '))

while cpf > 0 and qtd < 200:
    nome = input('Nome:')
    idade = int(input("Idade: "))
    while idade < 0:
        idade = int(input('Invalida, digite e idade: '))
    tab[cpf] = (nome, idade)
    qtd = qtd + 1
    cpf = int(input('CPF: '))
print(tab)

if cpf > 0 :
    print('Leitura interrompida, ultimo CPF desprezado.')

n = int(input('Quantidade de intervalos: '))
while n <= 0:
    n = int(input('Invalido, quantidade de intervalos: '))

for i in range(n):
    idMin = int(input('Idade mínima: '))
    while idMin < 0:
        idMin = int(input('Invalida. Idade mínima: '))
    idMax = int(input('Idade maxima: '))
    if idMax >= idMin:
        qtd2 = 0
        for ch in tab:
            if tab[ch][1] >= idMin and tab[ch][1] <= idMax:
                print(ch, tab[ch][0], tab[ch][1])
                qtd2 = qtd2 + 1
        print('Quantidade de alunos =', qtd2)
    else:
        print('Intervalo invalido, desprezado.')



