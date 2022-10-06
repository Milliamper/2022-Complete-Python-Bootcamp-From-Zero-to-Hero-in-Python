# immutables - vagyis nem módosíthatóak az elemei, nem írhatóak felül

t = (1,2,3)
t2 = (1, "kettő", 3.14)
mylist = [1,2,3]

print(type(t))

t3 = ('a', 'a', 'b')
print("Az 'a' karakter előfordulása a tuple-ben: ", t3.count('a'))
print("A 'b' előfordulása a {} index helyen".format(t3.index('b')))