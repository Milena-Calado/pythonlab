#Ler 2 strings e dizer quantas vezes o primeiro aparece no segundo

procura = str(input('procura:'))
texto = str(input('Texto:'))
cont = 0
pos = texto.find(procura)
while pos != -1:
    cont = cont + 1
    pos = texto.find(procura, pos + 1)
print(cont)
#print(texto.count(procura)) forma errada pq nao conta tudo

