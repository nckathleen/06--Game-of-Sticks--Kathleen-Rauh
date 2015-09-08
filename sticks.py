


def game_set_up(pile):


def game_size():
    print("Welcome to the Game of Sticks!")
    pile = 10
    pile = input("How many sticks are there on the table initially (10-100)? ")
    if 10 <= pile <= 100:
        game_set_up(pile)
    else:
        print("Please choose a number between 10 and 100 ")
        game_size()
    return pile


def game_loop():
    stick_subtract():   # Player1 and Player2
    take_turns():


def main():
    game_size():
    game_set_up(pile):
    game_loop():
    is_game_over():





if __name__ == '__main__':
    main()
