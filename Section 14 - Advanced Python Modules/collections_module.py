from collections import Counter, defaultdict, namedtuple

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 'a', 'a']

# count each unique item in list
print(Counter(mylist))

sentence = "How many times does each word show up in this sentence"
print(Counter(sentence.lower().split()))

#####################
letters = "aaaaabbbccdddeeffffff"
c = Counter(letters)

print("Most common words in letters variable: ", c.most_common())
#####################

d = {'a': 10}
print(d['a'])

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print("This should return zero because we set the default key to 0!: ", d['WRONG KEY!'])
print(d)

#####################

mytuple = (10,20,30)
print(mytuple[0])

Dog = namedtuple('Dog', ["age", "breed", "name"])

Fifi = Dog(5,"Husky", "Fifi")
print(type(Fifi))
print(f"Fifi is {Fifi.age} years old")
