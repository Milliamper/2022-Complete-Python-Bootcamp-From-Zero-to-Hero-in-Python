mystring = "Hello World"
print(mystring)

print("A string első karaktere : ", mystring[0])

print("A string utolsó karaktere : ", mystring[-1])

# slicing: egy rész kiragadása
# [start:stop:step]
print("Slicing : ", mystring[6:])
print("Slicing : ", mystring[0:5])
print("Slicing : ", mystring[::])
print("Slicing : ", mystring[::2])
print("Reversing : ", mystring[::-1])