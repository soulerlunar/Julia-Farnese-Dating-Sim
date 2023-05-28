# The first day starts here

label pre_game_opening:

    scene bg vatican
    play music choral

    j_int "It’s the first day of the papal election, and my first day as Dioneo Farnese."
    
    j_int "With Pope Innocent dead, cardinals from all corners of Italy (and even some beyond) are coming to Rome to politick and scheme, vying for one of them to become the next Vicar of Christ."

    j_int "My brother, Alessandro, is still only a priest, but he knows papal politics well, and managed to get me a job as his cousin “Dioneo Farnese” as an assistant clerk during the election." 
    
    j_int "I’ll have to actually work during the election, but hopefully I’ll also have enough time to speak to some of the cardinals…"

    j_int "My foolish father left our family in a lot of debt before he died, saddling Alessandro and I with the task of paying it off."
    
    j_int "At this point, the best way for us to move forward is to try to get the debt forgiven, as the sum is too high and our income too small."

    scene bg sistine
    
    j_int "Hence why I’m here. The Farnese family is old and noble, and if we want to see our family returned to power in Rome, this is the best opportunity for it."
    
    j_int "I intend to ingratiate myself to the man who will become the new pope, and win a place for myself at his side as his mistress and papal hostess."

    j_int "But I’ll have to pretend to be Dioneo in order to do it, which I hope won’t cause any problems."
    
    j_int "There are people here who know me, who might recognize my face even in disguise."
    
    j_int "And while part of being a vote counter means that I’ll be able to help someone by cheating, it will put me in a very dangerous position."

    j_int "No matter what, I can’t be caught."

    alessandro.c "Hey, Julia, come here."

    j_int "My brother is calling me. I assume that means we’re about to begin."

    show alessandro
    play music dance

    julia "Shouldn’t you start getting in the habit of calling me Dioneo, not Julia? It would be bad for both of us if you slipped up at the wrong time."

    alessandro.c "Alright then, Dioneo. This way, I found a place for us to talk."

    scene bg farnesement

    show alessandro

    alessandro.c "Are you ready for today?"

    julia "I think so. I’m trying not to think too hard about the possibility of this going wrong."

    alessandro.c "It won’t go wrong! So long as we’re careful and we play our cards right, this election could be the greatest thing that’s ever happened for our family."
    
    alessandro.c "Have you given any thought to who we’re going to choose?"

    julia "I’ve thought about it, but I think I’ll need to talk to the candidates more before I can choose."

    alessandro.c "Obviously we’ll need to go with whoever seems most set to win, but we don’t have many friends here, and I’d like to keep the two we have."
    
    alessandro.c "Cesare will certainly be supporting his father, Cardinal Borgia, and though I don’t know who Giovanni will be supporting, it seems pretty clear he won’t be supporting della Rovere."

    j_int "Cesare and Giovanni... Alessandro's closest friends from school. He cares a lot about them."

    julia "Hm… Making sure we keep our connections is important, though we’ll need more than just them as allies if we’re going to succeed."

    alessandro.c "Yes. You should plan to talk to the papabile cardinals and figure out which candidate is going to be the most successful and the most amenable to taking you as a lover if they become pope."
    
    alessandro.c "We can also do our own share of lobbying and influencing voters, but it might be more worth our time to help others do it for us."

    julia "More importantly, we’ll have access to the vote counting, and can switch votes if necessary."
    
    julia "Our family will be the kingmakers of this election, and our reward will be the restoration of our power and influence."

    alessandro.c "So long as we’re not caught."

    julia "Right. So long as we’re not caught."

    alessandro.c "Then we should get going before the conclave begins. It would be a bad look for us to be late."

    julia "Be careful, brother."

    alessandro.c "You as well. Come find me if there’s anything we should speak about, and I’ll meet you here again when the day is over."

    hide alessandro

    j_int "It seems the time has come to see if all our plans will be able to bear fruit."
    
    j_int "The front runners of this election, Cardinals Sforza, Borgia, and della Rovere, will be working furiously to win the majority of votes, and I’ll need to do what I can to help one of them succeed."

    j_int "Borgia, Alessandro’s boss, and mine too. A workaholic Spaniard who came to this election well prepared to do whatever it takes to win…"

    j_int "Della Rovere, an ambitious man who recently made a deal with the French. One not to be underestimated, but it seems public opinion is against him. For now, at least…"

    j_int "Sforza, Milanese and young. He wants the papacy to defend his home against French invasion. But he’s the only Italian here not on the payroll of foreign powers. Maybe he has a shot?"

    j_int "I should choose my candidate wisely."

    j_int "Once the election is over and I’m named the Vatican hostess, I will have the favor of the most powerful man in Europe, and our debts will be all but meaningless…"

    j_int "But for now, I should head up and get to work. These men aren’t going to seduce themselves."

    jump day_1


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

    $ d1_talkable = [dr, borgia, cesare, riario, caterina]

    call interact_menu(d1_talkable, "d1")

    call vote_counting

    # This ends the game.

    return

label day_2:

    scene bg room

    show julius:
        zoom 0.5
    
    dr.c "This is day 2"

    dr.c "Get out of my chapel"
