import random

from card import Card

'''
This is the player class for my Black Jack project.

The purpose of this class is much the same of the house class, except it is meant to be used by the player. The two purposes for this class are:
1. Give the player an option to draw another card or stay
2. If the player goes above 21 return that they are bust
'''

class Player():

    def __init__(self) -> None:
        pass

    # RETURNS THE INITIAL HAND OF THE PLAYER BASED ON THE AVAIBLE CARDS PASSED IN
    def player_initial(self, deck) -> tuple:

        # THIS MAKES SURE THAT THE VALUE PASSED TO THIS METHOD IS A DICTIONARY. IF IT IS NOT THE CODE WILL NOT WORK
        if not(type(deck) == dict):
            raise Exception("INPUT MUST BE A DICTIONARY")

        # PICKS A CARD AT RANDOM FROM THE PROVIDED DECK. IT WILL ALSO RETURN THE CARDS SO THAT THEY CAN BE REMOVED FROM THE DECK ONCE THEY ARE ADDED TO THE PLAYERS HAND 
        card_one = random.choice(list(deck))
        card_two = random.choice(list(deck))
        while card_two == card_one:
            card_two = random.choice(list(deck))
        return card_one, card_two

    
    def hit_or_pass(self, deck: dict) -> dict: # "*ARGS" STANDS FOR THE CARDS THE PLAYER CURRENTLY HAS. SHOULD BE OF CLASS 'Card'
        '''
        def ret_tuple(*args) -> tuple: # RETURNS ALL OF THE CARDS THE PLAYER CURRENTLY HAS AS A TUPLE SO THAT WE CAN WORK WITH THAT DATA
            mylist = []
            for i in args: 
                mylist.append(i)
            return tuple(mylist)
        '''
        hit_or_pass = input("Would you like to Hit [H] or Stay [S]: ").strip().lower() # TAKES IN WETHER OR NOT THE PLAYER WANTS AN EXTRA CARD

        if hit_or_pass[0] == "h": # IF THE PLAYER CHOOSES TO RECIEVE A CARD
            card, value = random.choice(list(deck.items()))
            return {card : value}
        elif hit_or_pass == "s": # IF THE PLAYER CHOOSES TO NOT RECIEVE A CARD 
            return {"STAY" : 0}
        else: # IF THE PLAYER DOESN'T INPUT EITHER AN "H" OR "S" THEN THIS ERROR WILL BE RAISED
            raise Exception("MUST ENTER EITHER 'H' OR 'S'")
    
    # IMPLIMENTATION PENDING
    def player_hand(self, *args, deck):
        player_hand_dict = {}