''' CARD'''
'''SUIT, RANK, VALUE'''

import random
suits = ("Hearts ♥", "Diamonds ♦", "Spades ♠", "Clubs ♣")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
dictionary_of_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
                        "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = dictionary_of_values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                
                # CREATE THE CARD OBJECT
                created_card = Card(suit, rank)

                self.all_cards.append(created_card)

    def shuffle_the_deck(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        # remove one card from the top of the deck
        return self.all_cards.pop(0)

    def adding_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # for a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"


'''GAME SETUP'''
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_the_deck()

# splitting the deck in half
for x in range(26):
    player_one.adding_cards(new_deck.deal_one_card())
    player_two.adding_cards(new_deck.deal_one_card())

print("Number of cards at player_two's hand: ", len(player_two.all_cards))
print("First card of player two: ", player_two.all_cards[0])

''' WHILE GAME_ON'''

round_num = 0
game_on = True

while game_on:

    round_num += 1
    print("Round ", round_num)

    if len(player_one.all_cards) == 0:
        print("Player one is out of cards! Playar two wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player two is out of cards! Playar one wins!")
        game_on = False
        break

    # START A NEW ROUND
    player_one_cards_in_play = []
    player_two_cards_in_play = []

    # dealing one card to the table to compare
    player_one_cards_in_play.append(player_one.remove_one())
    player_two_cards_in_play.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_cards_in_play[-1].value > player_two_cards_in_play[-1].value:
            player_one.adding_cards(player_one_cards_in_play)
            player_one.adding_cards(player_two_cards_in_play)
            at_war = False

        elif player_one_cards_in_play[-1].value < player_two_cards_in_play[-1].value:
            player_two.adding_cards(player_one_cards_in_play)
            player_two.adding_cards(player_two_cards_in_play)
            at_war = False

        else:
            print("WAR!")
            # vagyis már nincs elég kártyája, hogy csatázzon mégegyet
            if len(player_one.all_cards) < 5:
                print("Player one unable to declare a war")
                print("PLAYER TWO WINS")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player two unable to declare a war")
                print("PLAYER ONE WINS")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards_in_play.append(player_one.remove_one())
                    player_two_cards_in_play.append(player_two.remove_one())


'''
two_hearts = Card("hearts", "Two")
three_of_clubs = Card("Clubs", "Three")

new_deck = Deck()
print(len(new_deck.all_cards))

new_deck.shuffle_the_deck()

for card_object in new_deck.all_cards:
    print(card_object)

my_card = new_deck.deal_one_card()
print("My card is: ", my_card)
 
print("Here is your card: ", my_card)
print(len(new_deck.all_cards))

new_player = Player("Márton")
print(new_player)
new_player.adding_cards(my_card)
new_player.adding_cards([my_card, my_card, my_card])

print(new_player)
print(new_player.all_cards[0])

new_player.remove_one()
print(new_player)

'''
