class Dog():

    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A  CLASS

    species = "mammal"

    def __init__(self, breed, name, spots):

        # Attributes
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # Expect boolean
        self.spots = spots
    
    # OPERATIONS / ACTIONS ---> METHODS
    def bark(self, number):
        print(f"Woof! My name is {self.name} and the number is {number}")


my_dog = Dog(breed="Lab", name="Sammy", spots=True)  # osztály egy példánya

#print(type(my_dog))
#print(my_dog.breed)
#print(my_dog.name)
#print(my_dog.spots)
#print(my_dog.species)
#my_dog.bark(18)

class Circle():
    
    # CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2
    
my_circle = Circle(20)
print("Radius: ", my_circle.radius)
print("Area: ", my_circle.area)
print("Circumference: ", my_circle.get_circumference())
        


