import readline


myfile = open("test.txt")

print(myfile.read())
# ilyenkor az előző olvasásból a kurzor a szöveg végén maradt, ezért az újabb olvasás üres stringet fog visszaadni
# myfile.seek(0) megoldja
myfile.seek(0)
print(myfile.readlines())

myfile.close()

#így nem kell close() függvény
with open("test.txt") as my_new_file:
    contents = my_new_file.read()
print(contents)

# mode='w' - write only (will overwrite files or create new)
# mode='a' - append pnly (will add on to files)
# mode='r+' - reading and writing
# mode='w+' - writing and reading (overwrites existing files or creates a new file)
with open("test.txt", mode="r") as myfile:
    print(myfile.read())

#with open("test.txt", mode="a") as myfile:
#   myfile.write("\n5. sor")

with open("test2.txt", mode="w") as f:
    print(f.write("I created this file"))

with open("test2.txt", mode="r") as myfile:
    print(myfile.read())


