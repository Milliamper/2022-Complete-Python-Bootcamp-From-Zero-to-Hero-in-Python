import random

def negyzetre_emel(n):
    for x in range(n):
        yield x**2
    
    return x


def random_number (low, high, n):
    for x in range(n):
        yield random.randint(low,high)
    
    return x

print(list(random_number(1,10,5)))