'''
This is the card class for my Black Jack project. 

The goal of this class is to:
1. Create all the different cards and assign them all values
2. Create a method that populates a list with all the cards that we will use (this will be our Deck)


NOTES FOR LATER IMPROVEMENT:
- PERHAPS I CAN COMBINE THE LIST AND DICTIONARY INTO ONE METHOD -
- CREATE AN IMPLEMENTATION OF THE CARDS SUCH THAT THEY APPEAR SIDE TO SIDE FOR BOTH THE HOUSE AND THE PLAYER - 
- I COULD CREATE A PARENT PLAYER CALSS AND THEN HAVE THE HOUSE AND CURRENT PLAYER CLASS INHERIT FROM THAT CLASS -
'''

class Card():

    # Methods



    def __init__(self) -> None:
        pass

    # This method is designed to create a deck with all 52 cards and returned a non shuffeled version
    def create_deck_list(self) -> list:
        return_list = []
        counter_list_one = list(range(1,14))
        counter_list_two = list(range(1, 5))
        name = "EMPTY_NAME"
        for num_1 in counter_list_one:
            if num_1 == 1:
                name = "ACE"
            elif num_1 == 2:
                name = "TWO"
            elif num_1 == 3:
                name = "THREE"
            elif num_1 == 4:
                name = "FOUR"
            elif num_1 == 5:
                name = "FIVE"
            elif num_1 == 6:
                name = "SIX"
            elif num_1 == 7:
                name = "SEVEN"
            elif num_1 == 8:
                name = "EIGHT"
            elif num_1 == 9:
                name = "NINE"
            elif num_1 == 10:
                name = "TEN"
            elif num_1 == 11:
                name = "JACK"
            elif num_1 == 12:
                name = "QUEEN"
            elif num_1 == 13:
                name = "KING"
            for num_2 in counter_list_two:
                if (num_2 == 1):
                    return_list.append(name + "_OF_SPADES")
                elif (num_2 == 2):
                    return_list.append(name + "_OF_HEARTS")
                elif (num_2 == 3):
                    return_list.append(name + "_OF_CLUBS")
                elif (num_2 == 4):
                    return_list.append(name + "_OF_DIAMONDS")
        return return_list
    
    # This method is designed to give each of the cards a numerical value (such as 1 for ACE and so on)
    def create_deck_dict(self, ca_list) -> dict:
        return_dict = {}
        for card in ca_list:
            temp_list = card.split("_")
            if temp_list[0] == "ACE":
                return_dict[card] = 1
            elif temp_list[0] == "TWO":
                return_dict[card] = 2
            elif temp_list[0] == "THREE":
                return_dict[card] = 3
            elif temp_list[0] == "FOUR":
                return_dict[card] = 4
            elif temp_list[0] == "FIVE":
                return_dict[card] = 5
            elif temp_list[0] == "SIX":
                return_dict[card] = 6
            elif temp_list[0] == "SEVEN":
                return_dict[card] = 7
            elif temp_list[0] == "EIGHT":
                return_dict[card] = 8   
            elif temp_list[0] == "NINE":
                return_dict[card] = 9
            elif temp_list[0] == "TEN":
                return_dict[card] = 10
            elif temp_list[0] == "JACK":
                return_dict[card] = 10
            elif temp_list[0] == "QUEEN":
                return_dict[card] = 10
            elif temp_list[0] == "KING":
                return_dict[card] = 10
        return return_dict

    # This method will print out a quasi graphical representation of what the card looks like. In the bottom right corner we see the numerical value of the card as well
    def card_representation(self, value: int, suite: str, num: int) -> None:
        card_list_one = ["----"]
        card_list_two = ["-{v}{s}-".format(v = value, s = suite)]
        card_list_three = ["----    Value = {}".format(num)]

        print(card_list_one)
        print(card_list_two)
        print(card_list_three)
        print()
    
    def card_representation_dealer_init(self) -> None: # THIS IS TO HIDE THE SECOND INITIAL CARD OF THE DEALER
        card_list_one = ["----"]
        card_list_two = ["-??-"]
        card_list_three = ["----    Value = Who knows..."] 

        print(card_list_one)
        print(card_list_two)
        print(card_list_three)
        print()
