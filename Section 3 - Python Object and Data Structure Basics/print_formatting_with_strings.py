# string interpolation - változó beszúrása stringbe

print("This is a string {}".format("INSERTED"))
print("The {} {} {}".format("fox", "brown", "quick"))
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))

# float formatting "{value:width.precision f}" - hány tizedes jegyig írja ki
result = 100/777
print("The result was {r:1.3f}".format(r=result))

#f string literals
name = "Márton"
age = 22
print(f"Hello, my name is {name} and I'm {age} years old")