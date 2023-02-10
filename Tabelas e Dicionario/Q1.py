n = int(input('Digite o tamanho da tabela de profissões: '))

tab = {}

for i in range (n):
    codP = int(input('Digite o código de uma profissão:'))
while codP < 1:
    codP = int(input('Inválido, Digite o código de uma profissão:'))

for i in range (n):
    nomeP = str(input('Digite o nome da profissão:' ))
    centroP = int(input('Digite o centro o qual a profissão pertence:'))

tab[codP] = (nomeP, centroP)  

print('Tabela com %d profissões foi lida corretamente.' % (n))
print('Tabela ->', tab)

codP = int(input('Digite um código de profissão para busca (<=0 para parar):'))

while codP > 0:
    if codP in tab:
        nomeP, centroP = tab[codP]
        print('Profissão %d é %s e seu centro é %d' % (codP, nomeP, centroP))
    else:
        print('Profissão %d nao existe na tabela' % (codP))
    
    codP = int(input('Digite outro código que deseja buscar (<=0 para parar):'))
print('Fim do Programa')







                               
