mystring = "Hello"
mylist = []

for letter in mystring:
    break
    mylist.append(letter)
# print(mylist)

# ugyanez 1 sorban:
mylist = [letter for letter in mystring]
print(mylist)

#######################

mylist2 = [num**2 for num in range(0, 11)]  # négyzetre emelés
print(mylist2)

#######################

mylist3 = [num for num in range(0, 11) if num % 2 == 0]
print(mylist3)

#######################

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp+32) for temp in celcius]
print(fahrenheit)

# ugyanez for ciklussal
fahrenheit = []

for temp in celcius:
    fahrenheit.append((9/5)*temp+32)
print(fahrenheit)

# if else inside list comprehension
results = [x if x % 2 == 0 else 'ODD' for x in range(0,11)]
print(results)

# nested loops in list comprehension
mylist = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist)