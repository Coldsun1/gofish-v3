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
