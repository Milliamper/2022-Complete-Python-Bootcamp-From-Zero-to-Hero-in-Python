# Handle the exceptions!
# 1

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("You cannot multiply str with int")

# 2
x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("You cannot divide by zero!")
finally:
    print("All done!")

# 3

def ask():
    while True:
        try:
            num = int(input("Please add a number to square it: "))
        except:
            print("That's not a number")
            continue
        else:
            print("The result is:", num**2)
            break

ask()