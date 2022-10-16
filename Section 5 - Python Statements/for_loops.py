mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print('num')

print("Only even numbers: ")
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd number: {num}")

list_sum = 0
for num in mylist:
    list_sum += num
print("Számok összege 1-től 10-ig: ", list_sum)


for letter in "Hello World":
    print(letter)

tup = (1, 2, 3)
for item in tup:
    print(item)

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for item in mylist:
    print(item)

print("tuple unpacking: ")
for (a,b) in mylist:
    print(a)

dictionary = {'k1':1, 'k2':2, 'k3':3}
for item in dictionary:
    print(item)

for key,value in dictionary.items():
    print(key, value)