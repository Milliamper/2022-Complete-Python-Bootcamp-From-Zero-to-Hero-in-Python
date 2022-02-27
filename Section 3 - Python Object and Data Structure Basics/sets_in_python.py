# unordered collections of unique elements
# egy dologból csak egy lehet benne

myset = set()

myset.add(1)
myset.add(2)
myset.add(2)

print(myset)

mylist = [1,1,1,1,2,2,2,3,3]
print(set(mylist))