from typing import Iterable, Tuple
import entities


def deal_cards(cards: entities.FullDeck, player1: entities.Player, player2: entities.Player) -> None:
    """
    Deals the cards in 'cards' to the players in 'players'

    Parameters
    cards: entities.FullDeck
        Cards to be dealt
    player1: entities.Player, player2: entities.Player
        Players to receive the cards

    Returns
    If the cards were dealt equaly to the players
    """

    while len(cards) > 0:
        for player in (player1, player2):
            card = cards.remove_card()
            player.add_cards(card)


def gather_cards(cards: Iterable[entities.Card], player1: entities.Player, player2: entities.Player, amount: int) -> Tuple[entities.Card]:
    """
    Gathers all the cards to be given to the war round winner

    Parameters
    cards: Iterable[entities.Card]
        Cards already gathered
    player1: entities.Player, player2:entities.Player
        Players of the game
    amount: int
        Amount of cards to be taken from each player

    Returns
        All the cards gathered or None, if not possible
    """

    cards = list(cards)
    for player in (player1, player2):
        try:
            for _ in range(amount):
                cards.append( player.remove_card() )
        except IndexError:
            return None
    return cards


def loser(player1: entities.Player, player2: entities.Player) -> entities.Player | None:
    """
    Parameters
    player1: entities.Player, player2: entities.Player
        Players in the game

    Returns
    The loser or None, if there isn't one yet
    """

    for player in (player1, player2):
        if len(player) <= 0:
            return player

def print_result(player1: entities.Player, player2: entities.Player, rounds: int, wars: int) -> None:
    """
    Prints the result of the game

    Parameters
    player1: entities.Player, player2: entities.Player
        Players in the game
    rounds: int
        Total of rounds played
    wars: int
        Total of wars in the game
    """

    if len(player1) <= 0:
        print(f"{player2.name} has won the game!")
    else:
        print(f"{player1.name} has won the game!")
    print(f"Number of rounds: {rounds}")
    print(f"Number of wars: {wars}")
    print()
    print(player1)
    print(player2)


def main():
    print(r":::       :::     :::     :::::::::  ")
    print(r":+:       :+:   :+: :+:   :+:    :+: ")
    print(r"+:+       +:+  +:+   +:+  +:+    +:+ ")
    print(r"+#+  +:+  +#+ +#++:++#++: +#++:++#:  ")
    print(r"+#+ +#+#+ +#+ +#+     +#+ +#+    +#+ ")
    print(r" #+#+# #+#+#  #+#     #+# #+#    #+# ")
    print(r"  ###   ###   ###     ### ###    ### ")
    print()

    WAR_QT_CARDS = 3
    player1 = entities.Player("Player 1")
    player2 = entities.Player("Player 2")
    full_deck = entities.FullDeck()
    full_deck.shuffle()
    deal_cards(full_deck, player1, player2)
    cards_in_table = []
    rounds = 0
    wars = 0

    while True:
        rounds += 1

        ## moves
        card1 = player1.remove_card()
        cards_in_table.append(card1)
        card2 = player2.remove_card()
        cards_in_table.append(card2)

        ## comparing
        if entities.compare(card1, card2) > 0:
            player1.add_cards(cards_in_table)
            player1.win_round()
            cards_in_table.clear()
        elif entities.compare(card1, card2) < 0:
            player2.add_cards(cards_in_table)
            player2.win_round()
            cards_in_table.clear()
        else:
            wars += 1
            cards_in_table = gather_cards(cards_in_table, player1, player2, WAR_QT_CARDS)

        if loser(player1, player2) != None:
            break

    print_result(player1, player2, rounds, wars)


if __name__ == "__main__":
    main()
