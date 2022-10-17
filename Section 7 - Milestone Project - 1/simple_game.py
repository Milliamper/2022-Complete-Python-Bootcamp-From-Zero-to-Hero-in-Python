game_list = [0,1,2]
game_on = True

def display_game(game_list):
    print("Here is the current list: ", game_list)

def position_choice():
    choice = ''

    while choice not in ['0','1','2']:
        choice = input("Pick a position, 0, 1 or 2: ")

        if choice not in ['0','1','2']:
            print("Invalid choice")
    
    return int(choice)

def replacement_choice(game_list, position):

    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement

    print(game_list)
    return game_list

def gameon_choice():
    choice = ''

    while choice not in ['Y', 'N']:
        choice = input("Keep playing? (Y or N): ")

        if choice not in ['Y', 'N']:
            print("Invalid input!")
    
    if choice == 'Y':
        return True
    else:
        return False


while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()