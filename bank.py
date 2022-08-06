'''
This will be the class for the Bank account. The main functions of this class will be to... 
1. wager (determine how much the house should bet on the current game)
2. Store how much money the player currently has (the house has infinite money)
3. Add money / subtract money: Add or remove money from the players bank account
4. Insurance: Insures teh current game for the player to a certain extent (won't be a get out of jail for free card though)
'''


from xmlrpc.client import boolean

class Bank():
    def __init__(self) -> None:
        bank_account = 10000 # THE PLAYER WILL START OUT WITH 10,000 DOLLARS TO GAMBLE WITH


    def wager(self, is_lucky: boolean, random_draw: int, card_hand_value : int) -> tuple: # is_lucky = IS THE PLAYER FEELING LUCKY. IF SO, THE HOUSE WAGERS LESS. random_draw = AROUND EVERY 1/5 OF THE TIME THE CASINO DOUBLES THE BET.
        initial_bet = 0
        if(card_hand_value <= 5):
            initial_bet = 250
        elif(card_hand_value <= 10):
            initial_bet = 300
        elif(card_hand_value <= 17):
            initial_bet = 150
        elif(card_hand_value <= 21):
            initial_bet = 300
        if(is_lucky and (random_draw == 5)):
            return (initial_bet * 1.5)
        elif(not(is_lucky) and (random_draw) == 5):
            return (initial_bet * 2)
        elif(is_lucky and not(random_draw == 5)):
            return (initial_bet * .5)
        elif(not(type(is_lucky) == boolean) or not(type(random_draw) == int)):
            raise TypeError("ENTER A BOOLEAN FOR is_lucky AND AN INT FOR random_draw")