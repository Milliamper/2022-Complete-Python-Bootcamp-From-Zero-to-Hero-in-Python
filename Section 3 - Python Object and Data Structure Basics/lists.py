# unordered sequences with multiple object types
# supports indexing, slicing, nesting

mylist = [1,2,3]
mylist = ["Szöveg", 2, 200.1]
another_list = [6,7,8]

print("A lista hossza: ", len(mylist))
print("A lista első eleme: ", mylist[0])
print("A lista első elemétől az elemei: ", mylist[1::])
print("Concat two list : ", mylist + another_list)

mylist[0] = "SZÖVEG" #mutable
print("Concat two list : ", mylist + another_list)

mylist.append(4)
print("Új elem hozzáfűzése a lista végére", mylist)

another_list.pop()
print("Utolsó elem kiszórása a listából")
print("Concat two list : ", mylist + another_list)

elso_elem_kuka = mylist.pop(0)
print("Concat two list : ", mylist + another_list)

abc_list = ['f', 'c', 'b', 'y', 'q', 'a']
num_list = [4,7,1,2,3,9,48,22]


abc_list.sort()
num_list.sort()
print(f"Listák sorba rendezve: \n{abc_list}\n{num_list}")

abc_list.reverse()
num_list.reverse()
print(f"Listák megfordítva: \n{abc_list}\n{num_list}")