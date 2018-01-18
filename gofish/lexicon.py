from gofish import extras
#import extras
# ignore everything except players and card types

def scan(players, input_sentence):
    # input_sentence MUST contain a card and a player
    results = []

    words = input_sentence.lower().split()
    players_str_list = []

    for player in players:
        players_str_list.append(player.name)

    for word in words:
        if word in extras.types:
            results.append(('card', word))

        elif word in players_str_list:
            results.append(('player', word))

    return results
