# def create_cubes(n):
#    result = []
#
#    for x in range(n):
#        result.append(x**3) 
#    
#    return result

def create_cubes(n):
    for x in range(n):
        yield x**3 # így többet spórol a memóriával

print(create_cubes(10)) # the creating list of result is kept in memory

print(list(create_cubes(100)))