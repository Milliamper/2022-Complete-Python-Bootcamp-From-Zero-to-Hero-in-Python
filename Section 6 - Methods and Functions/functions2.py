# check if number is even

def is_even(a):
    return a % 2 == 0

print(is_even(9))


# check if any number is even inside the list



def check_even_list(num_list):

    even_list = []

    for number in num_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass
    # return False

mylist = [1,3,2,5,7,9,11,12]
print(check_even_list(mylist))
print("All even numbers: ", even_list)