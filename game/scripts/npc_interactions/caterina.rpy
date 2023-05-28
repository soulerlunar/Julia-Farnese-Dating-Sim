label caterina_d1:
    scene bg sistine

    j_int "I know Caterina Sforza. I watched her in her days as Papal Hostess, and she ran Pope Sixtus’ home with a cool efficiency."

    j_int "She’s not meant to be in here, just as, at the last election, she was not “meant” to point a cannon at the Sistine, but such are her ways, I suppose."
    
    j_int "I admire her—a woman with power in her own right, something quite rare in this world."

    j_int "She’s vicious. Her uncle, Cardinal Ascanio Sforza, is here as a voter, and she’s likely here to support him in whatever he does."
    
    j_int "She’d be a valuable ally and, perhaps more importantly, she could be a way of getting to Cardinal Sforza, that headstrong man."

    j_int "I’m not quite sure what she wants out of this election. I’d better go ahead and ask."

    julia "Lady Sforza! A moment, if you will."

    show caterina_happy

    caterina.c "Ah, Father Dioneo Farnese, am I correct?"

    julia "Yes! You may not know me well, but I am Father Alessandro Farnese’s cousin–I am a newcomer to Rome."

    caterina.c "Interesting! I’d never heard of Father Farnese having a cousin Dioneo before, let alone one in the church…"

    j_int "Oh no, is she on to me?!"

    caterina.c "…But I suppose some relations simply do not come up in conversation! Now, what brings you to the Sistine today?"
    
    caterina.c "I just received a letter from your cousin Julia—a quite glowing letter, of which I am much appreciative."
    
    caterina.c "She mentioned some debts your family has accrued?"

    menu:
        "Yes, actually. I know that you have much sway in Rome, and…":
            jump .c1
        "Actually, I was first wondering what you find yourself up to in the Sistine?":
            jump .c2
        "I should return to vote counting.":
            jump .conclusion
    
    label .c1:
        
        julia "My family is, indeed, greatly in debt. Anything you or your family could do to help relieve those debts would be greatly appreciated."

        caterina.c "Well, I could certainly talk to my uncle Ascanio about it."
        
        caterina.c "Julia Farnese wrote to me and told me all about your family’s noble history, and I would certainly like to help you all. We would, of course, require something in return."

        menu:

            "[[show her the portrait of Julia Farnese]]":
                jump .c3
            "My position as a vote counter could be quite useful...":
                jump .c4
       
        label .c3:
            julia "Would your uncle be in want of any sort of...companionship?"

            caterina.c "Oh, well, I suppose I could ask, I’m not sure if he’ll be interested in a female companion…"
            
            caterina.c "Come to think of it, does he swing in that…? Never mind. I’ll bring it up with him. She does look quite lovely."

            julia "A good word with him would be much appreciated!"

            caterina.c "One thing, is Julia Farnese not married?"

            julia "Ah, yes. Well, she’s married in quite the same way as you were married to Girolamo Riario."

            caterina.c "Oh, I understand completely. I weep for him nightly. God rest his soul."

            julia "God rest his soul."

            j_int "I suppress a smile, and it looks like Caterina does too."

            caterina.c "Well, I’ll discuss it with my uncle."

            julia "You have my gratitude."

            $caterina.add_opinion(julia_name, 10)
            $sforza.add_opinion(julia_name, 10)

            hide caterina_happy

            show caterina_concerned

            jump .conclusion

        label .c4:

            caterina.c "Is that so? Would you mind elaborating?"

            julia "Nothing untoward, my Lady. I could simply let you know how Cardinals are voting, such that you and your family may keep an accurate record of your allies and defectors."

            caterina.c "That would, indeed, be interesting."

            j_int "I could go so far as to offer to forge votes for Sforza, or for whoever the Cardinal chooses to support… No, not yet."
            
            j_int "That is an offer I could make another day. Telling them the votes is more than enough of a benefit for my alliance as of right now."

            julia "I’d be happy to provide vote tallies, as long as you and Cardinal Sforza keep in mind my family’s recent troubles. We are a noble family with much influence in Rome, and your help would not go unrewarded."

            caterina.c "Of course. If we are able to secure the papal throne, we will not forget this gesture of goodwill."
            
            hide caterina_happy

            show caterina_concerned

            jump .conclusion

    label .c2:

        narrator "Her voice gets low."

        hide caterina_happy

        show caterina_concerned

        $ caterina.add_opinion(julia_name, 10)

        caterina.c "Well, perhaps I shouldn’t share so many details, but King Charles has his eyes on Milan."
        
        caterina.c "Milan, of course, must remain under Sforza—and, by extension, Italian—control. My uncle Ascanio and I are here to ensure that."

        julia "Ah, yes, naturally. Well, I suppose, then, that you are advocating for yourselves on the papal throne, or perhaps Borgia?"

        caterina.c "Yes, well, Cardinal della Rovere is family by marriage, but he seems reluctant to renounce French support."
        
        caterina.c "I respect him greatly, but we must watch out for our own interests, just as I’m sure you will watch out for your own."

        j_int "It’ll be hard to play both sides between Sforza-Borgia and della Rovere for long… Something to keep in mind."

        jump .conclusion
    
    label .conclusion:

        caterina.c "I will let you return to your duties. Here, let me tip you for your fine work—"

        sforza.c "CATERINA! Come here and help me convince these Milanese cardinals to do the right thing, won’t you? That French rat della Rovere has everyone in his pocket."

        caterina.c "Oh, um, yes! I’ll be right there!"

        caterina.c "He’s, well, he can be quite brash. I’m sure you understand he’s under a lot of pressure right now. We will speak again soon."

        narrator "She drops a florin in your hand and hurries off."

        stop music
        return