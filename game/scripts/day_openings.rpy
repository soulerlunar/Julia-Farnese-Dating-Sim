# The first day starts here

label day_1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show julius:
        zoom 0.5

    # These display lines of dialogue.

    j "This is day 1."

    j "Alessandro is waiting for you!"

    # This ends the game.

    return

label day_2:

    scene bg room

    show julius:
        zoom 0.5
    
    j "This is day 2"

    j "Get out of my chapel"
