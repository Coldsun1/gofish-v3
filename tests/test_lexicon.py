import pytest
from gofish import lexicon, cards

def test_scan():
    player1 = cards.Player('player1')
    player2 = cards.Player('player2')

    players = [player1, player2]

    one = lexicon.scan(players, 'take a ACE from player2')
    assert one == [('card', 'ace'), ('player', 'player2')]

    two = lexicon.scan(players, '2 player1')
    assert two == [('card', '2'), ('player', 'player1')]

    three = lexicon.scan(players, 'something everything king player2')
    assert three == [('card', 'king'), ('player', 'player2')]
