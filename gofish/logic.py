# i want this file to contain all the logic
from gofish import cards, lexicon, extras
#import cards, lexicon, extras
import os

def main_loop(player, players, deck):
    os.system('cls')
    print(f"{player.name} Is Up!")
    input("Press ENTER To Continue!")
    os.system('cls')

    taken = 0

    while True:
        player.hand = sorted(player.hand, key=extras.types.index)
        print('- ' * 15)
        print(f'Player: {player.name}')
        print(f'Cards: {player.hand}')
        print('- ' * 15)

        input_sentence = input('> ')
        # pattern for asking for a card: take card other_player
        # order is not important

        if 'exit' in input_sentence:
            break

        elif 'take' in input_sentence and taken == 0:
            took = take_logic(player, players, input_sentence)

            if took == False:
                cards.take_cards(player, deck)
                print(f"Picked up a {player.hand[-1]}")

            print(f'\n{player.name} Your Turn Is Finished!')
            input("Press Enter to Continue!")
            break

        elif 'show other players' in input_sentence:
            print('Players: ')
            add = 1
            for i in players:

                print(f'{add}: {i.name}')
                add += 1
            input('')

        else:
            print('I don\'t know what to do with that\n')

def take_logic(player, players, input_sentence):
    results = lexicon.scan(players, input_sentence)

    for i in results:
        if i[0] == 'player':
            other_player = str_to_obj(i[1], players)
        elif i[0] == 'card':
            card = i[1]

    if card in other_player.hand:
        cards.take_cards(player, other_player, card)
        return True

    else:
        print(f"{other_player.name} did not have a {card}.")
        print("Picking up a card from the center deck instead.\n")
        return False


# takes a string and converts it to a player object
def str_to_obj(player_str, players):
    for pl in players:
        if player_str == pl.name:
            return pl

    return 'Invalid Player'
