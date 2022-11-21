"""
Contains the entities & macros used in the game
"""

import random
from typing import Iterable

SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
NUM_VALUES = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
            'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    """
    Card that'll be used in the game

    Atributes
    suit: str
        Suit of the card
    rank: str
        Rank of the card
    """

    def __init__(self, suit: str, rank: str) -> None:
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"


def compare(first: Card, second: Card) -> int:
    """
    Returns
    - A positive number, if the first card is the greater
    - A negative number, if the first card is the least
    - Zero, if the first card is equal to the second card
    """

    return NUM_VALUES[first.rank] - NUM_VALUES[second.rank]


class FullDeck:
    """
    Deck holding all 56 cards, shuffled
    """

    def __init__(self) -> None:
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append( Card(suit, rank) )
        self.shuffle()

    def shuffle(self) -> None:
        """
        Shuffles the cards in the deck
        """

        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        """
        Removes one card from the deck

        Returns
        The card removed
        """

        return self.cards.pop()


class Player:
    """
    Player of the game and their deck
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.deck = []

    def __str__(self) -> str:
        return f"{self.name}: {len(self.deck)} cards"

    def add_cards(self, card: Card|Iterable[Card]) -> None:
        """
        Adds one or multiple cards to the bottom of the player's deck

        Parameters
        card: card to be added
        """

        ## single card
        if type(card) == type( Card("", "") ):
            self.deck.append(card)

        ## iterable of cards
        else:
            self.deck.extend(card)

    def remove_card(self) -> Card:
        """
        Removes one card from the top of the player's deck

        Returns
            The card removed
        """

        return self.deck.pop(0)
