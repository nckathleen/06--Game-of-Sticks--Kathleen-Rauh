
def player_turn(turn_count):
    sticks_removed = input("Player{}: How many sticks do you take (1-3)? ".format(turn_count += 1))
    if 1 <= int(sticks_removed) <= 3:
        stick_subtract()
    else:
        print("Please enter a number between 1 and 3 ")

def stick_subtract(pile, sticks_removed):
    turn_count = 0
    if (turn_count % 2) == 0:


def game_set_up(pile):
    print("There are {} sticks on the board".format(pile))
    turn_count = 0
    if (turn_count % 2) == 0:


    game_set_up()
    return sticks_removed


def game_size():
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
    game_size():
    game_set_up(pile):
    game_loop():
    is_game_over():





if __name__ == '__main__':
    main()
