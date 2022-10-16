from itertools import tee
from random import shuffle, randint

print("Print numbers from 0 to 10: ")
for num in range(10):
    print(num)

print("Print numbers from 3 to 13: ")
for num in range(3, 10):
    print(num)

print("Print numbers from 0 to 10 by 2 steps: ")
for num in range(0, 11, 2):
    print(num)

print("List of numbers by range generator: ", list(range(0, 11, 2)))


#######################


print("Enumeration: ")
index_count = 0
for letter in "abcde":
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1

index_count = 0
word = "Márton"
for letter in word:
    print(word[index_count])
    index_count += 1

print("index count automatically in tuples")
for index, letter in enumerate(word):
    print(index, letter)


#######################

print("zip")
mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
mylist2 = ['a', 'b', 'c', 'd', 'e']

for item in zip(mylist1, mylist2): # a rövidebb listáig fűz össze csak
    print(item)

print(list(zip(mylist1, mylist2)))


#######################

print('x' in ['y', 'z', 'x'])

d={"mykey": 123}
print(123 in d.values())

#######################


mylist = [-1, 30, 40, 2]
print("Lowest number in list: ", min(mylist))
print("Highest number in list: ", max(mylist))


#######################


mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)



#######################

print(randint(1,100))

#######################

# stringként tárol!
# castolni kell ha integerként akarom tárolni
name = int(input("Add meg a neved: "))
print("A neved: ", name)
