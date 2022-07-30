import os
from tkinter import Y

from player import Player


'''
This is my game of Black Jack. I am doing this for my coding course capstone project. My goal is to create a fully flushed out and 
interactive game of Black Jack - but I will start with the basics and add functionality as I continue.

The code will be brutish and not very clean. I am still learning python and will continue to get better - this is my first attempt!

Feel free to add onto the code and make the game unique and your own. I did the best I could to make the code easy and readable!

I hope you enjoy my game of Black Jack!  
'''

'''
EXPLANING VARIABLES: 
card: variable that is used to create an instance of the Card class. Laster used to create 'deck_list' and 'deck_dict'. 
deck_list: Created using the object card (variable above). Creates a list with 52 cards in it. 
deck_dict: Created using the object card (variable above). Creates a dict with 52 cards in it.
house_hand_value: Int value. Shows the current value of the houses hand
player_hand_value: Int value. Shows the current value of the players hand
house_hand = Dictionary value. Stores the cards name and card value of the cards in the houses hand
player_hand = Dictionary value. Stores the cards name and card value of the cards in the players hand
continue_var = boolean value. Used to prompt the user to weather or not they would like to play
house_player = Instance of the House class
house_init_tuple = Has the initial two cards that the house gets. Returns their value.
clear = clears the console
new_dict = dictionary with just the values for the houses hand (card name and the value of the card)
temp_list = list that contains the name of card split up into just the words minus the underscore
suite = the suite of the card. It uses the list temp_list (as seen above)
card_1 = variable that is used to create an instance of the Card class. Laster used to create 'deck_list' and 'deck_dict'. Exact same as "card"
you_player = The object of the player that is used for the user
you_init_tuple = The initial hand that the player has. Stored in a tuple
new_dict = dictionary with just the values for the houses hand (card name and the value of the card) (same as the 'name_dict' variable above - just used for the player)
temp_list = list that contains the name of card split up into just the words minus the underscore (same as the 'temp_list' variable above - just used for the player)
suite = the suite of the card. It uses the list temp_list (as seen above) (same as the 'suite' variable above - just used for the player)
game_stopper = variable used to close out enclosing for loop if the player wants to stop getting cards
hit_or_not = 
'''



# This function is used to give the rules of Black Jack. It will be used every time the player chooses to see the rules of black jack again
from configparser import MAX_INTERPOLATION_DEPTH
from sre_constants import CATEGORY_DIGIT

from card import Card
from house import House


def rules_of_black_jack():
    print("The rules of Black Jack are as follows:\n")
    print("1) You will be give 2 cards facing up. The value of the cards are as follows:")
    print("    1.1) Any numbered card will be worth the cards value")
    print("    1.2) Any face card will be worth 10")
    print("    1.3) The Ace will be worth either 11 or 1 depending on your choice!")
    print("2) The dealer will one card face up and one card face down")
    print("3) You can choose to recieve cards (called 'Hit me') or stay (called 'Stay') based on the goal of 21")
    print("4) The goal of Black Jack is to get cards toatalling in value 21. If you go over you bust. Whoever is closer to 21 (but not bust) winst the game \n")

'''
Introduction of the game
'''

print("Welcome to the Milind Casino \n")
rules_of_black_jack()

'''
Start of the game
'''

# THIS IS THE MAIN PART OF THE GAME. 
while True:
    house_bust = False
    player_bust = False
    # CREATING THE DECK OF CARDS. THERE IS BOTH A LIST REPRESENTATION AND DICTIONARY REPRESENTATION OF THE DECK. THEY WILL BE NAMED ACCORDINGLY
    card = Card()
    deck_list = card.create_deck_list() # DECK IN LIST FORM
    deck_dict = card.create_deck_dict(deck_list) # DECK IN DICTIONARY FORM

    house_hand_value = 0 # CURRENT VALUE OF HOUSES HAND
    player_hand_value = 0 # CURRENT VALUE OF PLAYERS HAND

    house_hand = {} # CURRENT CARDS IN HOUSES HAND
    player_hand = {} # CURRENT CARDS IN PLAYERS HAND 

    # CHECKING IF THE USER WANTS TO PLAY THE GAME
    continue_var = input("\nWould you like to play? Enter yes [Y] or no [N]: ").strip().lower()
    if (continue_var == "n"):
        break
    else:

        # THIS IS GETTING THE TWO INITIAL CARDS FOR THE HOUSE
        house_player = House()
        house_init_tuple = house_player.house_initial(deck_dict)
        

        # THIS IS USED TO CLEAR THE CONSOLE FOR A MORE CLEAN LOOKING GAME 
        clear = lambda: os.system('clear')
        clear()

        # FETCHING AND SHOWING THE CURRENT CARDS OF THE HOUSE
        print("HOUSES CARDS: ")
        for card_ in house_init_tuple:
            house_hand[card_] = deck_dict[card_]
            new_dict = {card_ : deck_dict[card_]}
            temp_list = card_.split("_")
            suite = temp_list[2]
            card.card_representation(deck_dict[card_], suite[0], deck_dict[card_])
            house_hand_value += deck_dict[card_]

        # DELETING THE CARDS THE HOUSE GOT FROM THE DICTIONARY
        for card in house_init_tuple:
            del deck_dict[card]



        print()
        print()

        card_1 = Card() # THERE WAS SOME WEIRD GLITCH WHERE THE VARIABLE card WAS NOT WORKING FOR LINE 98 SO I HAD TO CREATE card_1 <-- COME BACK TO FIX THIS GLITCH
        # CREATING THE PLAYERS HAND
        you_player = Player() # THE PLAYER OBJECT
        you_init_tuple = you_player.player_initial(deck_dict)

        # FETCHING AND SHOWING THE CURRENT CARDS OF YOU, THE PLAYER
        print("YOUR CARDS: ")
        for card_ in you_init_tuple:
            player_hand[card_] = deck_dict[card_]
            new_dict = {card_ : deck_dict[card_]}
            temp_list = card_.split("_")
            suite = temp_list[2]
            card_1.card_representation(deck_dict[card_], suite[0], deck_dict[card_]) # LINE 98 AS REFERENCED ABOVE. THIS SHOWS A GRAPHICAL REPRESENATION OF THE CARDS THE PLAYER HAS
            player_hand_value += deck_dict[card_] # ADDS THE VALUE OF THE CARDS IN THE PLAYERS HANDS TO THE RUNNING TOTAL
            

        # DELETING THE CARDS YOU GOT FROM THE DICTIONARY
        for card in you_init_tuple:
            del deck_dict[card]



        print()
        print()
        clear()

        #GIVING THE PLAYER THE OPTION TO GET HIT OR NOT (Sorry, I do not know the nomenclature for Black Jack)
        while True:
            
            game_stopper = False # THIS IS USED TO STOP THE WHILE LOOP IF THE PLAYER NO LONGER WANTS TO PLAY
            print("Your current total is {}".format(player_hand_value))

            player_choice_dict = you_player.hit_or_pass(deck_dict) # RETURNS A DICTIONARY OF {CARD_NAME : CARD VALUE} FOR THE PLAYERS NEW CARDS

            just_values = list(player_choice_dict.values()) # RETURNS A LIST OF THE VALUE OF THE NEW CARD DRAWN
            just_keys_temp = str(list(player_choice_dict.keys())).replace('[', '').replace(']', '') # RETURNS JUST THE KEY OF THE CARD (THE NAME OF THE CARD) WITH THE QUOTATION MARKS AROUND IT
            just_keys_len = len(just_keys_temp) # RETURNS THE LENGTH OF THE KEY
            just_keys = just_keys_temp[1:(just_keys_len - 1)] # RETURNS THE KEY WITHOUT THE QUOTATION MARKS

            # IF THE PLAYER CHOOSES TO STAY, THIS BREAKS OUT OF THE LOOP
            if just_values[0] == 0:
                game_stopper = True
            # ELSE, IF THE PLAYER CHOSE TO RECIEVE A CARD
            else:
                # ADDS THE VALUE OF THE PLAYERS NEW CARD TO THEIR CURRENT HAND
                player_hand_value += just_values[0]

                player_hand[just_keys] = just_values[0]

                del deck_dict[just_keys] # DELETES THE NEW CARD DRAWN FROM THE DECK (deck_dict)
            if game_stopper == True:
                break
        
        print()
        print()
        print()
        print("You're current hand: ")

        # THE BELOW CODE IS SO THAT I CAN DO A CARD REPRESENATION OF ALL OF THE CARDS. THE REASON I HAVE TO CREATE A NEW DECK_DICT IS BECAUSE THE OTHER CARD VALUES HAD BEEN REMOVED FROM THE OTHER DICTIONARY
        card_2 = Card()
        deck_list_2 = card_2.create_deck_list() # DECK IN LIST FORM
        deck_dict_2 = card_2.create_deck_dict(deck_list) # DECK IN DICTIONARY FORM

        # THIS SHOWS A GRAPHICAL REPRESEATNION OF THE CARDS IN THE PLAYERS HAND
        for i,j in enumerate(player_hand): # i = TRACKING VALUES, j = KEYS
            print(j)
            just_values = deck_dict_2[j]
            just_keys = j
            temp_list = just_keys.split("_")
            temp_string = temp_list[2]
            suite = temp_string[0]
            card_1.card_representation(just_values, suite, just_values)

        # THIS FUNCTION LETS THE PLAYER CHOOSE IF THEY WANT THEIR ACE TO HAVE THE VALUE OF 1 OR 11
        player_card_name_list = list(player_hand.keys())
        for card_name in player_card_name_list:
            temp_name_list = card_name.split("_")
            if temp_name_list[0] == "ACE":
                player_choice = int(input("Would you like your ace to have the value of 1 or 11? Enter 1 or 11: "))
                if player_choice == 11:
                    player_hand_value += 10
                    print(player_hand_value)
        if player_hand_value > 21:
            player_bust = True

        # THE CODE BELOW IS THE CODE THAT PLAYS FOR THE HOUSE. THE HOUSE DOES THE FOLLOWING:
        # 1. IF THE VALUE OF THEIR CARDS IS BELOW 17 THEY DRAW A CARD
        # 2. IF THE VALUE OF THEIR CARDS IS ABOVE 17 THEY STAY

        print()
        print()
        print("The houses current hand value is {}".format(house_hand_value))

        while house_hand_value < 17:
            new_house_card = list(house_player.hit_or_pass(house_hand_value, deck_dict))
            house_hand_value += deck_dict_2[new_house_card[0]]
            temp_string = new_house_card[0]
            suite = temp_string[2]
            card_1.card_representation(deck_dict_2[new_house_card[0]], suite, deck_dict_2[new_house_card[0]])
            del deck_dict[new_house_card[0]]

        if house_hand_value > 21:
            house_bust = True
        print()
        print("The houses current hand value is {}".format(house_hand_value))

        cont = input("Type in 'c' to continue: ")

        clear()
        if cont == 'c':
            if player_bust == False and player_hand_value > house_hand_value:
                print("THE PLAYER HAS WON")
            elif player_bust == True and house_bust == False:
                print("THE HOUSE HAS WON")
            elif player_bust == False and house_bust == True:
                print("THE PLAYER HAS WON")
            elif (player_bust == False and house_bust == False) and (player_hand_value < house_hand_value):
                print("THE HOUES HAS WON")
