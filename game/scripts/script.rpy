# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define day = 1

# The game starts here.

label start:

    jump pre_game_opening

    # if day == 1:
    #     jump day_1
    # elif day == 2:
    #     jump day_2

    # This ends the game.

    return
