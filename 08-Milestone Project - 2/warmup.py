#!/usr/bin/env python3
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9,
'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single Card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


if __name__ == "__main__":
    # Game setup
    player_one = Player('One')
    player_two = Player('Two')
    game_on = True
    round_number = 0
    cards_at_war = 5
    
    new_deck = Deck()
    new_deck.shuffle()
    
    # 52 cards split between two players
    for x in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    while game_on:

        round_number += 1
        print(f'Round {round_number}')

        if len(player_one.all_cards) == 0:
            print('Player One out of cards! Player Two Wins!')
            game_on = False
            break

        if len(player_two.all_cards) == 0:
            print('Player Two out of cards! Player One Wins!')
            game_on = False
            break

        # Start a new round
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
        
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True

        while at_war:
            # [-1] to always compare last card from the stack
            if player_one_cards[-1].value > player_two_cards[-1].value:

                # print(f'{player_one_cards[-1]} > {player_two_cards[-1]}')

                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                at_war = False
            
            elif player_one_cards[-1].value < player_two_cards[-1].value:

                # print(f'{player_one_cards[-1]} < {player_two_cards[-1]}')

                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)

                at_war = False

            else:

                print('WAR!')
                # print(f'{player_one_cards[-1]} = {player_two_cards[-1]}')

                if len(player_one.all_cards) < cards_at_war:
                    print('Player One unable to declare war')
                    print('Player Two Wins!')
                    game_on = False
                    break
                
                elif len(player_two.all_cards) < cards_at_war:
                    print('Player Two unable to declare war')
                    print('Player One Wins!')
                    game_on = False
                    break

                else:

                    for num in range(cards_at_war):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())