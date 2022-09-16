def myfunc(a, b):
    # Return 5% of the sum of a and b
    return sum((a, b)) * 0.05


# ezek positional argumentek
# azaz a 40 - > a , 60 - > b
print(myfunc(40, 60))

#######################################################
# így tuple-ként vannak kezelve a számok, bármennyit hozzá lehet adni


def myfunc(*args):
    return sum(args) * 0.05


print(myfunc(40, 60, 100))

#######################################################

# **kwargs -> key word arguments


def myfunc(**kwargs):
    print("It's a dictionary: ", kwargs)
    if "fruit" in kwargs:
        print("My fruit of choise is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")


myfunc(fruit="apple", veggie="lettuce")

#######################################################


def myfunc(*args, **kwargs):
    print("args : ", args)
    print("kwargs : ", kwargs)
    print("I would like {} {}".format(args[0], kwargs["food"]))


myfunc(10, 20, 30, fruit="orange", food="eggs", animal="lion")
