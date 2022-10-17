from random import shuffle

example = [1, 2, 3, 4, 5, 6, 7]


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


print(shuffle_list(example))

####### THE GAME #############################################

def player_guess():

    guess = ""

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number 0, 1 or 2: ")

    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!", mylist)
    else:
        print("Wrong guess!", mylist)

mylist = ['', 'O', '']

mixed_list = shuffle_list(mylist)

guess = player_guess()

check_guess(mixed_list, guess)




