
def player_turn(turn_count):
    sticks_removed = input("Player{}: How many sticks do you take (1-3)? ".format(turn_count += 1))
    if 1 <= int(sticks_removed) <= 3:
        stick_subtract()
    else:
        print("Please enter a number between 1 and 3 ")
        player_turn()
    return sticks_removed


def stick_subtract(pile, sticks_removed):
    #total number of sticks (game_size)
    #player's chosen number to remove (sticks_removed)
    pile = pile - sticks_removed

    return pile


def game_set_up():
# Begin to count turns in order to keep track of which player's turn it is.
    game_size()
    print("There are {} sticks on the board".format(pile))
    turn_count = 1
    if (turn_count % 2) == 0:
        player = '1'
    else:
        player = '2'
    player_turn(turn_count)
    game_set_up()
    return turn_count


def game_size():
# Begins the game by asking user for the number of sticks in the game.  Passed test.
    print("Welcome to the Game of Sticks!")
    pile = input("How many sticks are there on the table initially (10-100)? ")
    if 10 <= int(pile) <= 100:
        game_set_up(pile)
    else:
        print("Please choose a number between 10 and 100. ")
        game_size()
    return pile


def game_loop():
    stick_subtract(pile,sticks_removed):   # Player1 and Player2
    take_turns():


def main():
    game_set_up()
    game_loop():
    is_game_over():





if __name__ == '__main__':
    main()
