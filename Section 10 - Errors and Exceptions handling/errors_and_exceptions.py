def add(n1, n2):
    return n1 + n2

n1 = 10
n2 = input("Please add the second number: ")

try:
    result = n1 + int(n2)
    print(result)
except:
    print("Hey it looks like aren't adding correctly")


#################################################################

