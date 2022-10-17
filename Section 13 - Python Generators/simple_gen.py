def simple_gen():
    for x in range(3):
        yield x

for x in simple_gen():
    print(x)

print("")

g = simple_gen()
print(next(g))
print(next(g))
print(next(g))

#######################

s = "hello"
for letter in s:
    print(letter)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))