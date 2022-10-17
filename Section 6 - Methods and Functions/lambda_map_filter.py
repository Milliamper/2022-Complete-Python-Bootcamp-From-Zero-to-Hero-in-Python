def square(num):
    return num**2

my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))

##########################################

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return "EVEN"
    else:
        return mystring[0]

names=["Márton", "Eszter","Petra"]

print(list(map(splicer, names)))

##########################################

def check_even(num):
    return num % 2 == 0

mynums=[1,2,3,4,5,6]

# csak a páros számok kiválogatása
print(list(filter(check_even, mynums)))

##########################################

square = lambda num: num ** 2
print(square(3))

print(list(map(lambda num:num**2, mynums)))
print(list(filter(lambda num: num % 2 == 0, mynums)))


