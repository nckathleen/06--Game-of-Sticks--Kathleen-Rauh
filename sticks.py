
def player_turn(pile, turn_count):
    if turn_count % 2 = 0:
        player = 1
    else:
        player = 2
    print("There are {} sticks on the board".format(pile))
    sticks_removed = input("Player{}: How many sticks do you take (1-3)? ".format(player))
    if 1 <= int(sticks_removed) <= 3:
        stick_subtract(pile,sticks_removed)
    else:
        print("Please enter a number between 1 and 3 ")
        player_turn()
    return sticks_removed


def stick_subtract(pile, sticks_removed):
    #total number of sticks (set_game_size)
    #player's chosen number to remove (sticks_removed)
    pile = pile - sticks_removed
    turn_count = turn_count += 1
    player_turn()
    return turn_count(pile, turn_count)


def game_set_up():
# Begins the game by asking user for the number of sticks in the game.  Passed test.
    print("Welcome to the Game of Sticks!")
    pile = input("How many sticks are there on the table initially (10-100)? ")
    if 10 <= int(pile) <= 100:
        turn_count = 1
        player_turn(pile, turn_count)
    else:
        print("Please choose a number between 10 and 100. ")
        set_game_size()
    return pile


def game_loop():
    stick_subtract(pile,sticks_removed):   # Player1 and Player2


def main():
    set_game_size()
    game_loop():
    is_game_over():



if __name__ == '__main__':
    main()
