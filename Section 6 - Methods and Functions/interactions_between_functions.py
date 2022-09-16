from random import shuffle

example = [1,2,3,4,5,6,7]
shuffle(example) # ez nem tér vissza semmivel...
# print(example)

####################################################

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist # ...de így már igen

def player_guess():

    guess = ""

    while guess not in ["1","2","3"]:
        guess = input("Pick a number : 1, 2, or 3 : ")
    
    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess-1] == "O":
        print("Correct")
        print(mylist)
    else:
        print("Wrong guess!")
        print(mylist)

# Initial list
mylist = [" ", "O", " "]

# Shuffle list
mixed_list = shuffle_list(mylist)

# User guess
guess = player_guess()

# Check guess
check_guess(mixed_list, guess)