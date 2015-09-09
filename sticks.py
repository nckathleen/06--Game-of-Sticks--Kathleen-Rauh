
def player_turns(pile, turn_count):
    if (turn_count % 2) == 0:
        print("player2")
        player = 2
    else:
        print("player1")
        player = 1
    print("There are {} sticks on the board".format(pile))
    sticks_removed = int(input("Player{}: How many sticks do you take (1-3)? ".format(player)))
    if 1 <= sticks_removed <= 3:
        turn_count += 1
        print("In player_turns turn_count is: " + str(turn_count))
        stick_subtract(pile,sticks_removed, player, turn_count)
    else:
        print("Please enter a number between 1 and 3 ")
        player_turns(pile, turn_count)
    return (sticks_removed, turn_count)


def stick_subtract(pile, sticks_removed, player, turn_count):
    print("Turn Count is: " + str(turn_count))
    pile = pile - sticks_removed
    if pile > 2:
        player_turns(pile, sticks_removed)
    else:
        end_game(pile, player)
    return pile


def end_game(pile, player):
    print("There are {} sticks on the board".format(pile))
    if pile == 2:
        sticks_removed = int(input("Player{}: How many sticks do you take (1-2)? ".format(player)))
        stick_subtract(pile, sticks_removed, player)
    else:
        print("Player{}: You lose. You took the last stick.".format(player))


def game_set_up():
# Begins the game by asking user for the number of sticks in the game.  Passed test.
    print("Welcome to the Game of Sticks!")
    pile = int(input("How many sticks are there on the table initially (10-100)? "))
    if 10 <= pile <= 100:
        turn_count = 1
        print("Im here in game_loop")
        game_loop(pile, turn_count)
    else:
        print("Please choose a number between 10 and 100. ")
        game_set_up()
    return pile


def game_loop(pile, turn_count):
    player_turns(pile, turn_count)
    return turn_count


def main():
    game_set_up()
    play_again = input("Would you like to play again? (Y)es or (N)o: ")
    if play_again[0] not in ('Y', 'y'):
        print("Hope you enjoyed the game.")
    else:
        game_set_up()



if __name__ == '__main__':
    main()
