import pytest
from gofish import logic, cards


def test_str_to_obj():
    player1 = cards.Player('player1')
    player2 = cards.Player('player2')

    players = [player1, player2]

    assert logic.str_to_obj('player1', players) == player1
    assert logic.str_to_obj('player2', players) == player2

    assert logic.str_to_obj('playe2', players) == 'Invalid Player'


def test_take_logic():
    player1 = cards.Player('player1')
    player2 = cards.Player('player2')

    players = [player1, player2]

    player1.hand = ['ace', '2', '3', '4', '5', '6', '7']
    player2.hand = ['8', '9', '10', 'jester', 'queen', 'king']
    deck

    # take single card



    # take multiple cards

    # take from the center deck

    assert len(player1.hand) == 7
    assert len(player2.hand) == 8
