from colorsys import TWO_THIRD
from curses.ascii import isdigit


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choice():

    # VARIABLES
    num = ''
    acceptable_range = range(1,11)
    within_range = False

    # CONDITIONS TO CHECK
    # DIGIT OR WITHIN_RANGE = FALSE
    while num.isdigit() == False or within_range == False:
        num = input("Give a number between 1 and 9: ")

        # DIGIT CHECK
        if num.isdigit() == False:
            print("You must add a number between 1 and 9!\n")

        # RANGE CHECK
        if num.isdigit():
            if int(num) in acceptable_range:
                within_range = True
            else:
                print("You are out of acceptable 1 to 9 range!")
                within_range = False

    return int(num)


row1 = [' ', 'X', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', '']

display(row1, row2, row3)

print("The given number is: ", user_choice())
