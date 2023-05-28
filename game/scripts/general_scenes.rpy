label vote_counting:

    scene bg sistine

    $ votes = get_votes(voters)
    $ vote_count = count_votes(votes)
    $ winner = get_winner(vote_count)

    if not winner is None:
        jump .no_pope

label .habemus_papam:
    mario.c "Habemus papum!"
    
    mario.c "We have a pope!"

label .no_pope:

    mario.c "We have finished the vote counting! The votes are as follows:"

    python:
        dr.set_opinion(riario, 80)

        count_list = sorted(vote_count.items(), key=lambda item: item[1])

        for candidate in count_list:
            msg = str(npcs[candidate[0]].c.name) + " with " + str(candidate[1]) + " vote"
            if candidate[1] != 1:
                msg += "s"
            msg += "."
            renpy.say(mario.c, msg)

    mario.c "This means we have no pope at this time. The conclave shall continue."

    j_int "No pope yet. That means I have to keep working."
        
