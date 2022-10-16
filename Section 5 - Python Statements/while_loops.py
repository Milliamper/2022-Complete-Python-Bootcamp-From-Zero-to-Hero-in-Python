x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print("x is not less than 5")

# break, continue, pass

y = [1,2,3]
for num in y:
    pass
print("Enf of my script")

mystring = "Márton"
for letter in mystring:
    if(letter == 'o'):
        continue
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
