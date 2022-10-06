import pwd


myfile = open("test.txt")
print(myfile.read()) # egyetlen string-ként visszadja a txt tartalmát
myfile.seek(0) # kurzor így kerül vissza újra a file elejére (mac-en kell, windows-on "nem kéri")
print(myfile.readlines())

myfile.close()


print("________")

with open("test.txt") as teszt_adat:
    contents = teszt_adat.read()

print(contents)

with open("test.txt", mode = 'r') as my_file: # r: read only, w: write only, a: append, r+: read and write, w+: writing and reading
    contents = my_file.read()

print(contents)

with open("uj_fajl.txt", mode='w+') as f:
    f.write("Első sor")

with open("uj_fajl.txt") as f:
    print(f.read())