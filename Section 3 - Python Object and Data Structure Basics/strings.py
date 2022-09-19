'''
- str: ordered sequence of characters: "hello", "szia", "200"
    It means that we can use indexing and slicing to grab sub-sections of strings
    Indexing starts at 0
    Last letter is at -1 index
    Escape sequences: \n \t
    string object cannot support item assignment
'''

print('Hello')
print("Hello")
print("Piros \nfű")

print("A string hossza: ", len("He "))

# indexing and slicing
    # slicing: [start:stop:step]

mystring = "Hello World"
print(mystring)
print("First character: ", mystring[0])
print("Last character: ", mystring[-1])
print(mystring[6::])
print(mystring[:4:])
print(mystring[2:9:2])
print(mystring[::2])
print(mystring[::-1])
print(mystring[8])

# string object cannot support item assignment

name = "Márton"
# name[0] = "K" -> ez így nem fasza

last_letters = name[1::]
new_name = "K" + last_letters
print(new_name)

letter = "z"

print(letter * 10)

# print('2' + 3) -> ez így szintén nem fasza

x = "Hello World"
print(x.upper())
print(x.split())

mondat = "Ezt a mondatot fel szeretném osztani"
print(mondat.split('a'))

# string interpolation
print("Hello, this string is {}".format("INSERTED"))
print("The {2} {0} {1}".format("brown", "fox", "big"))