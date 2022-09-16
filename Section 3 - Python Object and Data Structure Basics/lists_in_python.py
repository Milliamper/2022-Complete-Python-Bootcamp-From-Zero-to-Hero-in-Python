# ordered sequences - azaz indexelhető

my_list = [1, 2, 3]
my_list = ["string", 100, 23.3]

mylist = ["one", "two", "three"]
print(mylist[0])
print(mylist[1:])

# concat
another_list = ["four", "five"]
new_list = mylist + another_list
print(new_list)

new_list[0] = "Valami más"
print(new_list)

new_list.append("six")
print(new_list)

# remove and return last item at default
popped_item = new_list.pop(0)
print(popped_item)

# sort
new_list = ['a', 'e', 'x', 'b']
num_list = [4, 1, 8, 3]

new_list.sort()  # nem tér vissza semmivel
my_sorted_list = new_list.sort()

print(type(my_sorted_list))
print(new_list)

# rendezés
num_list.sort()
print(num_list)

# megfordítás
num_list.reverse()
print(num_list)
