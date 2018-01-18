import cards, logic

deck = cards.create_deck()

player1 = cards.Player('player1')
player2 = cards.Player('player2')
#player3 = cards.Player('player3')
#player4 = cards.Player('player4')

players = [player1, player2]

for _ in range(7):
    cards.take_cards(player1, deck)
    cards.take_cards(player2, deck)

while True:
    for player in players:
        logic.main_loop(player, players, deck)
