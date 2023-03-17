# escreva uma funcão que recebe um lista L e devolve uma nova lista sem elementos duplicados

def removerDuplicados(L):
    nova_lista = []
    for elemento in L:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista
print(removerDuplicados([1,1,1,1,1,2,3,4,5,3,2,2,1]))

#Escreva uma função que recebe duas listas e retorna True caso tenha elementos em comum

def temElementosemComum(L1, L2):
    for e in L1:
        if e in L2:
            return True
    return False
print(temElementosemComum([1,2,3,4,5], [6,7,8,1,10]))

#Escreva uma função que recebe uma lista L e outra lista S e retorna True caso S seja sublista de L

def sublista(L, S):
    for i in range(len(L)):
        if L[i] == S[0]:
            equal = True
            for j in range(len(S)):
                if S[j] != L[i+j]:
                    equal = False
                    break
            if equal:
                return equal
    return False
print(sublista([1,2,3,4,5,6,7,8], [2,3]))   
print(sublista([1,2,3,4,5,6,7,8], [2,6])) 

#ESCREVA UMA FUNCAO QUE RECEBA UMA STRING S COMO ARGUMENTO E RETORNA UM DICIONÁRIO COM A FREQUENCIA DE 
#CADA LETRA NESTA STRING. POR EX FREQUENCIALETRAS('LEOPOLDO')
#RETORNA {'l': 2, 'e': 1, 'o': 3, 'p': 1, 'd':1}

def frequenciaLetras(s):
    frequencia = {}
    for letra in s:
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1
    return frequencia
print(frequenciaLetras('leopoldo'))

#Escreva uma função que receve um nome de arquivo como argumento e conta a quantidade de 
# palavaras neste arquivo

def qtd_palavras(file):
    with open (file, "r") as arquivo:
       texto = file.read()
       palavras = texto.lower().replace('.', '').replace(',', '').split()
       contar_palavras = {}
       for palavras in palavras:
           if palavras in contar_palavras:
               contar_palavras += 1
           else: 
               contar_palavras = 1
       return contar_palavras

           