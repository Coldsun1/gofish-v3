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

    assert len(player1.hand) == 7
    assert len(player2.hand) == 6

    meow = logic.take_logic(player1, players, 'take 9 from player2')

    assert len(player1.hand) == 8
    assert len(player2.hand) == 5

    player1.hand.append('2')
    player1.hand.append('2')

    meow = logic.take_logic(player2, players, 'take 2 from player1')

    assert len(player1.hand) == 7
    assert len(player2.hand) == 8

def test_win():
    player1 = cards.Player('player1')
    player2 = cards.Player('player2')

    
