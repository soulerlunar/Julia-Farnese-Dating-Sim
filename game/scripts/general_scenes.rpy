label vote_counting:

    scene bg sistine

    $ votes = get_votes(voters)
    $ vote_count = count_votes(votes)
    $ winner = get_winner(vote_count)
    $ print(votes)

    python:
        pope = False
        if winner is None:
            renpy.jump("vote_counting.no_pope")
        else:
            pope = True
            renpy.jump("vote_counting.habemus_papam")

label .habemus_papam:
    play music choral
    
    mario.c "Habemus papum!"
    
    mario.c "We have a pope!"

label .no_pope:

    mario.c "We have finished the vote counting! The votes are as follows:"

    python:
        count_list = sorted(vote_count.items(), key=lambda item: item[1])

        for candidate in count_list:
            msg = str(npcs[candidate[0]].c.name) + " with " + str(candidate[1]) + " vote"
            if candidate[1] != 1:
                msg += "s"
            msg += "."
            renpy.say(mario.c, msg)

    if not pope:
        mario.c "This means we have no pope at this time. The conclave shall continue."

        j_int "No pope yet. That means I have to keep working."

        j_int "I might as well take a look at the votes, though..."

        j_int "hm..."

        python:
            for v in votes.items():
                msg = str(npcs[v[0]].c.name) + " voted for " + str(npcs[v[1]].c.name) + "."
                renpy.say(j_int, msg)
        
        j_int "Interesting info, I'll have to use this carefully."
    else:
        j_int "So quickly?!"

        j_int "Damn it. We haven't cleared our debt, or gotten me locked as hostess, or anything..."

        j_int "I guess this is game over for the Farneses..."

        narrator "The end"