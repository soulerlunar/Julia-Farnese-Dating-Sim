label borgia_d1:
    scene bg sistine

    j_int "Though he’s maybe not as charismatic as some of the other cardinals, Rodrigo Borgia is definitely one of the frontrunners for the papacy."

    j_int "He’s always treated Alessandro well, like the noble Roman that he is, which is more than I can say for della Rovere’s lapdog, Riario."

    j_int "He hasn’t recognized me as Julia, though, which has been amusing."

    julia "Vice chancellor!"

    show borgia

    borgia.c "Dioneo Farnese."

    julia "I wanted to thank you, Your Eminence, for hiring me as an assistant clerk. I am honored to be here among such great men, and amidst history being made."

    borgia.c "It was no trouble. Your cousin, Alessandro, spoke highly of you, and I am sure you will perform your duties well."

    julia "Of course. If you aren’t too busy, Your Eminence, I was hoping to have a word with you."

    borgia.c "Go ahead."

    j_int "I can’t tell if this is Borgia being friendly or if I’ve already somehow managed to make myself disfavored, but I guess it’s too late to back out now."

    narrator "[[show him the portrait of Julia Farnese]"

    julia "This is my cousin, Julia Farnese."

    hide borgia

    show borgia happy

    borgia.c "Julia Farnese…Yes, I have heard she is one of the most beautiful women in Rome, and this portrait exemplifies that to be sure."

    julia "Forgive me if this is presumptuous, Your Eminence,  but as you have seen, Julia is a very beautiful young woman much beloved by Rome."
    
    julia "She would be a great boon to you if you were to choose her as your papal hostess."

    borgia.c "Hm…I am not yet decided on a hostess, though I have heard that Julia is married to an Orsini, is she not?"

    j_int "It seems the subject of a mistress is already on his mind, if he’s already asking me about my husband."

    julia "Yes, though that should be no trouble to you, Your Eminence. Orsino Orsini is a very weak-willed man, and could not refuse Julia from anything she decided upon."
    
    julia "Nor could he refuse the man on the highest throne in all of Europe."

    menu:
        borgia.c "And do you believe that I will be that man?"

        "Of course...":
            jump .c1
        "I'm not sure...":
            jump .c2

    label .c1:

        julia "And I would be willing to help ensure it, Your Eminence."

        $ borgia.add_opinion(julia_name, 10)

        borgia.c "In what manner?"

        julia "My family is well-connected in Rome and beloved by the Mob. I’m sure if our influence was behind you, we could sway our fellow Romans to support you as well."
        
        julia "We are kin with the Orsini through Julia’s marriage, after all."

        borgia.c "That is useful indeed. The enmity that much of Italy has towards my family for our Spanish roots will likely cause trouble."
        
        borgia.c "Swaying the Mob would be very helpful for the safekeeping of my family."

        julia "And with Julia Farnese’s incomparable beauty by your side as your papal hostess, the city of Rome would certainly fall at your feet and welcome your papacy with open arms."

        borgia.c "..."

        j_int "How easily men fall silent in the face of a woman’s charms, even when they think she is not present!"

        julia "I would be most willing to help Your Eminence in any tasks you require, though of course, the Farneses’ influence will only be more powerful the stronger our family is."
        
        julia "It is no secret that we have fallen on hard times, but if that were to be rectified…"

        borgia.c "Yes, I believe your cousin, Alessandro, owes me 5,000 florins. And of course, as the pope with his beautiful sister at my side, the rest of your family’s debts would be a trifle."

        julia " Then I am sure Julia would be pleased to be your household, and she’s given me her assurances that she wishes to be beside you as pope."

        borgia.c "That is good to hear. I have much more work to be done, so I must go, but you are free to speak with me whenever you like."

        borgia.c "Keep me abreast of what goes on with the functionaries, and let me know if anyone gives you any troubles."

        return

    label .c2:

        hide borgia happy

        show borgia upset

        $ borgia.add_opinion(julia_name, -10)

        borgia.c "Well the election is not a time for neutrality, Dioneo, and if your cousin wants me to make her my papal hostess, I will need the papacy in order to do so."

        julia "Of course. I will think on the matter and return to my duties."

        hide borgia

        j_int "The truth is, I’m not yet sure Borgia can win. And a Spaniard on the throne of St. Peter? It’s nearly unthinkable!"

        j_int "But if I don’t support Borgia and he does win, then I’ll have lost my chance to gain anything."
        
        j_int "And Borgia is more than competent and knows Alessandro well…this could be our chance for a cardinalship or an even greater benefice someday."

        return