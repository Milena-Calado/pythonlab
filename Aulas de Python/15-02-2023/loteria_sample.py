from random import sample

def numeros_loteria():
    return sorted(sample(range(1, 60), 6))

print(numeros_loteria())