# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define day = 1

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sistine

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    julia "This is my first day in the Sistine. I suppose I should go and find Alessandro."

    show alessandro

    # These display lines of dialogue.

    alessandro.c "Good morning, dear sister. Or should I say Dioneo."

    alessandro.c "I'm glad we've made it this far, but let's best be careful."

    alessandro.c "If anyone figures out who you are, we're in big trouble."

    if day == 1:
        jump day_1
    elif day == 2:
        jump day_2

    # This ends the game.

    return
