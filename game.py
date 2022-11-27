from typing import Iterable, Tuple
import entities


DIV = "-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-\|/-"


def deal_cards(cards: entities.FullDeck, player1: entities.Player, player2: entities.Player) -> bool:
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

    try:
        while len(cards) > 0:
            for player in (player1, player2):
                card = cards.deal_card()
                player.add_cards(card)
    except IndexError:
        return False
    else:
        return True


def print_players(player1: entities.Player, player2: entities.Player) -> None:
    """
    Prints the players given

    Parameters
    player1: entities.Player, player2: entities.Player
        Players to be printed
    """

    for player in (player1, player2):
        print(player)


def gather_cards(cards: Iterable[entities.Card], player1: entities.Player, player2:entities.Player) -> Tuple[entities.Card]:
    """
    Gathers all the cards to be given to the war round winner

    Parameters
    cards: Iterable[entities.Card]
        Cards already gathered
    player1: entities.Player, player2:entities.Player
        Players of the game

    Returns
        All the cards gathered
    """

    cards = list(cards)
    for player in (player1, player2):
        try:
            for _ in range(0, 3):
                cards.append( player.remove_card() )
        except IndexError:
            pass
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

def print_result(player1: entities.Player, player2: entities.Player) -> None:
    print_players(player1, player2)
    if len(player1) <= 0:
        print(f"{player2.name} has won the game!")
    else:
        print(f"{player1.name} has won the game!")


def main():
    print(r":::       :::     :::     :::::::::  ")
    print(r":+:       :+:   :+: :+:   :+:    :+: ")
    print(r"+:+       +:+  +:+   +:+  +:+    +:+ ")
    print(r"+#+  +:+  +#+ +#++:++#++: +#++:++#:  ")
    print(r"+#+ +#+#+ +#+ +#+     +#+ +#+    +#+ ")
    print(r" #+#+# #+#+#  #+#     #+# #+#    #+# ")
    print(r"  ###   ###   ###     ### ###    ### ")
    print()

    player1 = entities.Player("Player 1")
    player2 = entities.Player("Player 2")
    full_deck = entities.FullDeck()
    print("The game has begun!")

    full_deck.shuffle()
    print("The deck with 56 cards has been shuffled")

    deal_cards(full_deck, player1, player2)
    print("Each player has received 28 cards")

    cards_in_table = []

    print()
    print(DIV)
    print()

    while True:
        print_players(player1, player2)

        card1 = player1.remove_card()
        cards_in_table.append(card1)
        print(f"Player 1 showed {card1}")

        card2 = player2.remove_card()
        cards_in_table.append(card2)
        print(f"Player 2 showed {card2}")

        if entities.compare(card1, card2) > 0:
            print("Player 1 won the round")
            player1.add_cards(cards_in_table)
        elif entities.compare(card1, card2) < 0:
            print("Player 2 won the round")
            player2.add_cards(cards_in_table)
        else:
            print("IT'S WAR!")
            cards_in_table = gather_cards(cards_in_table, player1, player2)
            continue

        if loser(player1, player2) != None:
            break
        else:
            cards_in_table.clear()
            print()
            print(DIV)
            print()

    print_result(player1, player2)


if __name__ == "__main__":
    main()
