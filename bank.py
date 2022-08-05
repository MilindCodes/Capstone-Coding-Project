'''
This will be the class for the Bank account. The main functions of this class will be to... 
1. wager (determine how much the house should bet on the current game)
2. Store how much money the player currently has (the house has infinite money)
3. Add money / subtract money: Add or remove money from the players bank account
4. Insurance: Insures teh current game for the player to a certain extent (won't be a get out of jail for free card though)
'''


def __init__(self) -> None:
    bank_account = 10000 # THE PLAYER WILL START OUT WITH 10,000 DOLLARS TO GAMBLE WITH


def wager(self, is_lucky, random_draw) -> int: # is_lucky = IS THE PLAYER FEELING LUCKY. IF SO, THE HOUSE WAGERS LESS. random_draw = AROUND EVERY 1/5 OF THE TIME THE CASINO DOUBLES THE BET.
    pass