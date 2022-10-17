def hello(name="Márton"):
    print("Hello")

    def greet():
        return "Greet() inside hello" 

    def welcome():
        return "\t this is welcome() inside hello!"
    
    if name == "Márton":
        return greet
    else:
        return welcome


# my_new_func = hello()
# print(my_new_func())

# greet = hello() # functions are objects that can be passed into other objects

def new_decorator(original_function):

    def wrap_func():
        print("Some extra code, before the original function")

        original_function()

        print("Some extra code, after original function")

    return wrap_func

def func_needs_decorator():
    print("I want to be decorated")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()

print("\n")

@new_decorator
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator()

