class Int_set(object):
    """Um Int_set é um conjunto de inteiros"""
      #Valor de um conjunto é representado por uma lista de inteiros, self._vals.
      #Cada inteiro em um set aparece em self._vals apenas uma vez.

    def __init__(self):
        """Cria conjunto vazio de inteiros"""
        self._vals = []

    def insert(self, e):
        """Assume que e tem um valor inteiro e insere e em self"""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """Assume que e tem um valor inteiro
           Retorna True se está em self, e False do contrário"""
        return e in self._vals

    def remove(self, e):
        """Assume que e tem um valor inteiro e remove e de self
           Lança ValueError se e não está em self"""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def get_members(self):
        """Retorna uma lista com os elementos de self._vals
           Nada pode ser assumido sobre a ordem dos elementos"""
        return self._vals[:]
    
    def union(self, other:type):
        """other é um objeto Int_set
           altera o estado de self de forma a conter exatamente 
           os elementos atuais mais os elementos de other."""
        for elem in other:
            self.insert(elem)
    
    def __iter__(self):
        yield from self._vals
        # for e in self._vals:
        #     yield e

    def __add__(self, other):
        new_set = Int_set()
        new_set._vals = other.get_members()
        new_set.union(self._vals)
        return new_set
    
    def __len__(self):
        return self.size()
    
    def __tamanho__(self):
        return self.size()

    def __eq__(self,y):
        #assuma que x e y são Int_set
        # x == y (x é o self, y é o other)
        # x == y <==> Int_set.__eq__(x,y)
        return sorted(self._vals) == sorted(y._vals)
    
    def size(self):
        return len(self._vals)

    def __str__(self):
        """Retorna uma representação em string de self"""
        if self._vals == []:
            return '{}'
        # self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'

# +: __add__
# -: __sub__
# **: __pow__
# <<: __lshift__
# *: __mul__ 
# /: __truediv__ 
# //: __floordiv__ 
# %: __mod__
# |: __or__ 
# <: __lt__
# ∧: __xor__ 
# >: __gt__
# >>: __rshsift__ 
# ==: __eq__ 
# <=: __le__ 
# &: __and__ 
# !=: __ne__ 
# >=: __ge__ 


if __name__=='__main__':
    s = Int_set()
    s.insert(3)
    s.insert(4)
    print(str(s))
    print('O valor de s é', s)
    t = Int_set()
    t.insert(4)
    t.insert(5)
    t.insert(6)
    print('O valor de t é', t)
    print('O tamanho de s agora é', len(s))
    print('O tamanho de t agora é', len(t))
    s.union(t)
    print('O valor de s agora é', s)#{3,4,5,6}
    print('O valor de t agora é', t)#{4,5,6}
    print('O tamanho de s agora é', s.size())
    # print('O tamanho de t agora é', tamanho(t))
    x = s + t
    print('O valor de x é', x)
    print('O tamanho de x agora é', len(x))
    print('s e x são iguais? ', s == x)
    x.insert(12)
    print('O valor de x é', x)
    print('O tamanho de x agora é', len(x))
    print('O valor de s é', s)
    print('O tamanho de s agora é', len(s))
    print('s e x são iguais? ', s == x)
    # print(1 == x)
    # x = s
    # print('s e x são iguais? ', s == x)