import math
import random

value = 4.35

print(math.floor(value))
print(math.ceil(value))
print(round(4.5))
print(round(5.5))
# ez azért ilyen mert ha mindig fel vagy lefele kerekítene, vagyis csak egy irányba, akkor fals adatokat kapnánk egy idő után
# ezért aszerint a szabály szerint kerekít, hogy melyik irányba kap páros számot

print(math.pi)
# numpy library more advanced than math lib

print(math.log(math.e))
print(math.log(100, 10))
print(math.sin(10))
print(math.degrees(math.pi/2))

'''Random module'''
print(random.randint(0, 100))

random.seed(42)  # this way we can always get the same random integers
print(random.randint(0, 100))  # setting a sequence for random numbers

mylist = list(range(0, 20))
print(mylist)
print("Get random item from the list: ", random.choice(mylist))

# sample with replacement
# ismétlődhetnek a számok
print("Get multiple random numbers from the list: ",
      random.choices(population=mylist, k=10))

# sample without replacement
# NEM ismétlődhetnek a számok
print("Get multiple random numbers from the list: ",
      random.sample(population=mylist, k=10))

random.shuffle(mylist)
print("Shuffled list: ", mylist)

print("Pick a random number between 0 and 100 with floating points too: ",
      random.uniform(a=0, b=100))
print(random.gauss(mu=0, sigma=1))
