from unicodedata import name


def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

# apply the function to every simple number in the list
for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))

##################################################
names = ["Amy", "Eve", "Sally", "Dave"]


def splicer(string):
    if len(string) % 2 == 0:
        return "EVEN"
    else:
        return string[0]


print(list(map(splicer, names)))

##################################################


def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]

# only grab the even numbers:
print(list(filter(check_even, mynums)))

##################################################
# lambda expression (anonymous function, only using 1 time):

square = lambda num: num**2
print(square(3))

# using map with lambda
print(list(map(lambda num:num**2, mynums)))

# using map with filter
print(list(filter(lambda num: num % 2 == 0,mynums)))

print(list(map(lambda name:name[::-1],names)))