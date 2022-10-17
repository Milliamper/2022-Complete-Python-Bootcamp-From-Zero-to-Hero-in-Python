class Animal():

    def __init__(self):
        print("Animal created!")
    
    def who_am_i(self):
        print("I'm an animal")
    
    def eat(self):
        print("I'm eating")

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")
    
    def who_am_i(self):
        print("I'm a dog")

myanimal = Animal()
myanimal.eat()
myanimal.who_am_i()

mydog = Dog()
mydog.eat()
mydog.who_am_i()

#######################
print("\nPOLYMORPHISM")
#######################

class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
         return self.name + " says Woof!"

class Cat():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
         return self.name + " says Meow!"

niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)

#######################
print("\nABSTRACT CLASS")
#######################

class Animal():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstact method")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"

pepe = Cat("Pepe")
picur = Dog("Picur")

print(pepe.speak()) 