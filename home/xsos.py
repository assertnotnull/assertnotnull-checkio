def checkio(game_result):
    unique_in_row = []
    for row in game_result:
        unique_in_row.append(set(row))
        if len(set(row)) == 1:
            return row[0]
    union = unique_in_row[0] & unique_in_row[1] & unique_in_row[2]
    print(union)
    if len(union) == 2:
        if crosses(game_result):
            return game_result[1][1]
    return union.pop() if len(union) == 1 else "D"


def crosses(game_result):
    for x in [0, 2]:
        if len(set(game_result[x][0] + game_result[1][1] + game_result[0][x])) == 1:
            print(set(game_result[x][0] + game_result[1][1] + game_result[x][x]))
            return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio(["OOO","XX.",".XX"]) == "O", "Fail"
    assert checkio(["OXO","XOX","OXO"]) == "O"
    assert checkio(["OXO","XXO","XOX"]) == "D"

