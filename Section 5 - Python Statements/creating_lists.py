mylist = []
mystring = "Hello"
for letter in mystring:
    mylist.append(letter)
print(mylist)

###############################################

mylist = [letter for letter in mystring]
print(mylist)

###############################################

mylist = [x for x in range(0,11)]
print(mylist)

###############################################

print("A számok négyzete 0-tól 10-ig:")
mylist = [num**2 for num in range(0,11)]
print(mylist)

###############################################

mylist = [x for x in range (0,11) if x % 2 == 0]
print("Lista feltöltése páros számokkal egy sorban:", mylist)

###############################################

celsius = [0, 23, 42, 100]

fahrenheit = [ (9/5) * temp + 32 for temp in celsius]
print(fahrenheit)

###############################################

mylist = []
for x in [1,3,5]:
    for y in [200, 400, 600]:
        mylist.append(x*y)
print("nested loop: ", mylist)