x = 0

while x < 5:
    print(f"The current value of x is {x}")
    x += 1
else:
    print("x is no longer less than 5")

# pass (does nothing)

y = [1,2,3]

for item in y:
    pass

# continue (goes to the top of the closest enclosing loop)

mystring = "Márton"

for letter in mystring:
    if letter == 'á':
        #continue
        break
    print(letter)

# break (breaks out of the current closest enclosing loop)