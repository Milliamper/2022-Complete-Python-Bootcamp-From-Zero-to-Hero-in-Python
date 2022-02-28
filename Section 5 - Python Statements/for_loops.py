mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numbers in mylist:
    # print(numbers)
    # print("Hello")

    # Check for even
    if numbers % 2 == 0:
        print(numbers)
    else:
        print(f"Odd number : {numbers}")

########################

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print("A számok összege : ", list_sum)

########################
# Iterate through list
mystring = "Hello World"

for letter in mystring:
    print(letter)

########################

my_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
print("A lista hossza : ", len(my_list))

# for item in my_list:
# print(item)

# tuple unpacking
for (a, b) in my_list:
    print(a)

# iterate through dictionary
d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(key,value)