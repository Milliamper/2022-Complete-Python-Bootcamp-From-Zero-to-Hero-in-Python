def myfunc(a, b):
    # returns 5% of the sum a and b

    return sum((a, b)) * 0.05

# print(myfunc(40,60))

#############################################

# bármennyi paraméter megadható így
# tuple-ként szerepel a függvényben


def myfunc(*args):
    return sum(args) * 0.05, args


print(myfunc(40, 60, 50, 50, 30, 70))

#############################################

# key word arguments
# dictionary-vel tér vissza


def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print("My fruit choice is {}".format(kwargs["fruit"]), kwargs)
    else:
        print("No fruit")


print(myfunc(fruit="Apple"))

#############################################


def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0], kwargs["food"]))


print(myfunc(10, 20, 30, fruit="orange", food="eggs", animal="dog"))
