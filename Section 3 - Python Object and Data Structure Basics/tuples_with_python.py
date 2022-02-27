# olyan mint a lista csak immutable - vagyis ha egyszer be lett állítva az értéke, nem lehet felülírni

my_tuple = (1, 2, 3)
my_list = [1, 2, 3]

print(type(my_tuple))

my_tuple = ("one", 2, "three", 2)
print(my_tuple)

print("Kettesek szama : " ,my_tuple.count(2))

