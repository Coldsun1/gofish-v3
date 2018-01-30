import pytest
from gofish import cards

def test_take_cards():
    player1 = cards.Player('player1')
    player2 = cards.Player('player2')

    player1.hand.append('2')
    assert player1.hand == ['2']

    cards.take_cards(player2, player1, '2')

    assert player1.hand == []
    assert player2.hand == ['2']


def test_create_deck():

    deck = cards.create_deck()

    assert len(deck) == 52

def test_basic():
    player1 = cards.Player('player1')
    player2 = cards.Player('player2')

    deck = cards.create_deck()

    assert len(deck) == 52

    for _ in range(7):
        cards.take_cards(player1, deck)
        cards.take_cards(player2, deck)

    assert len(player1.hand) == 7
    assert len(player2.hand) == 7
    assert len(deck) == 38


def test_check_sets():
    player1 = cards.Player('player1')

    player1.hand = ['2', '2', '2', '2', 'ace']
    assert player1.hand == ['2', '2', '2', '2', 'ace']

    cards.check_sets(player1)
    assert player1.hand == ['ace']
    assert player1.sets == ['2']

# skip
def te_st_check_win():

    player1 = cards.Player('player1')
    player2 = cards.Player('player2')

    players = [player1, player2]

    deck = []

    assert len(deck) == 0
    assert len(player1.hand) == 0
    assert len(player2.hand) == 0

    player1.sets = ['ace', 'king']
    player2.sets = ['ace', 'jester', 'queen']

    assert len(player1.sets) == 2
    assert len(player2.sets) == 3

    assert cards.check_win(players, deck) == player2.name
