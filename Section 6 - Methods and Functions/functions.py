from sqlalchemy import true


def say_hello():
    print("hello")
# say_hello()

def say_hello(name="Default Value"):
    print(f"Hello {name}")
# say_hello("Márton") # ha üresen hagyom akkor a default value fog megjelenni

def add_num(num1, num2):
    return num1+num2

result = add_num(5,6)
# print(result)

#########################################

def even_checker(number):
    return number % 2 == 0
# print(even_checker(21))

#########################################
# return true if any number is even inside a list

def chech_even_list(mylist):
    # return all the even numbers in a list

    even_numbers = []

    for num in mylist:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            # return False (ez nem jó, mert csak az első számot nézi meg így)
            pass

    return even_numbers

mylist = [1,3,5,7,2,4]
print(chech_even_list(mylist))