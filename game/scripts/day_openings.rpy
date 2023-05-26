# The first day starts here

label day_1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sistine

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alessandro

    # These display lines of dialogue.

    alessandro.c "Alright, here we go. Day 1."

    alessandro.c "We've got this. Time to build up our family."

    alessandro.c "Gonna meet a lot of new people today."

    alessandro.c "You should probably decide who you want to speak to."

    hide alessandro

    call interact_menu(npcs, "d1")

    # This ends the game.

    return

label day_2:

    scene bg room

    show julius:
        zoom 0.5
    
    dr.c "This is day 2"

    dr.c "Get out of my chapel"
