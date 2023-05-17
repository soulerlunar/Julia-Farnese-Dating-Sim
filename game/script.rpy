# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Julius")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    default x = 8

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show julius:
        zoom 0.5

    # These display lines of dialogue.

    j "You've created a new Ren'Py game."

    j "Once you add a story, pictures, and music, you can release it to the world!"

    if x > 10:
        jump day_1

    # This ends the game.

    return
