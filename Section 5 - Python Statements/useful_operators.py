from random import randint, shuffle
mylist = [1, 2, 3]

# range operator (start, stop, step), azaz generator
for num in range(3, 10, 2):
    break
    print(num)

# enumerators
# v1
index_count = 0

for letter in 'abcde':
    break
    print(f"At index {index_count} the letter is {letter}")
    index_count += 1

# v2
index = 0
word = "abcde"

for letter in word:
    break
    print(f"At index {index} the letter is {word[index]}")
    index += 1

# enumerate
for index, letter in enumerate(word):
    break
    print(index, letter)

# zip
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2, mylist3):
    break
    print(item)

print(list(zip(mylist1, mylist2, mylist3)))

# in operator (check something if something in a list, dictionary, string)

print('x' in [1, 2, 3, 'x'])
print('a' in 'a world')
print("mykey" in {'mykey': 345})

#min, max

my_list = [1, 2, 3, 4, 10]
print("Highest number in my list : ", max(my_list))
print("Lowest number in my list : ", min(my_list))

# random, shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist)
print(mylist)

print("Random number between 1 and 100 : ", randint(1, 100))

mynum = randint(1,1000)
print(mynum)

# input from user

result = input('Enter your name : ')
print("Your name is : ", result)
print(type(result)) # stringként tárol (a számokat is)

# cast string to int
num = int(input('Enter your favourite number : '))
print("Your number is : ", num)
print(type(num))