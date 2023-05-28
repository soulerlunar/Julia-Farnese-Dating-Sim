

label julius_d1:

    scene bg sistine
    
    j_int "According to everything I’ve heard from Alessandro and rumors in Rome, Giuliano della Rovere is a formidable man."
    
    j_int "The other vote counters seem divided between being scared of him and hating him (though maybe that has more to do with his nephew than the man himself),"
    
    j_int "but I haven’t spoken with him enough to have a grasp on what he’s really like."

    j_int "I mean, he’s certainly competent. And power-hungry, so he’s definitely going to be a frontrunner for the papacy."
    
    j_int "And from what I’ve heard of him (and his daughter), he’s not the pious type of cardinal who would refuse a woman’s companionship."

    j_int "At the very least I should try to approach him. Perhaps I’ll get a better understanding of the man by speaking with him."

    show julius

    j_int "Well. At least he’s not terrible-looking. And even in those Franciscan robes, he seems… strong."

    dr.c "Dioneo Farnese, greetings! My nephew tells me you’re new to the Vatican. How have you found it so far?"

    julia "It is…hard but gratifying work, Your Eminence. And it is an honor to be in the presence of such great men."

    narrator "Julius laughs."

    dr.c "Well, some of us may be that, yes, but fret not, young man. You are just as important, perhaps even more so than the cardinals here."
    
    dr.c "A job as a vote-counter is a crucial one, after all. This whole endeavor would all fall apart without your honest efforts."

    j_int "Is Cardinal della Rovere being…nice? Either someone is lying about him, or he has a very good poker face."

    julia "Thank you, Your Eminence. If I may…"

    menu:
        "[[show him the portrait of Julia Farnese]":
            jump.c1
        "I know you have much sway with Cardinal Nanni…":
            jump .c2
        "I must return to my duties.":
            jump.conclusion


    label .c1:

        julia "This is my cousin, Julia Farnese. Forgive me if this is presumptuous, but if a man in your position (and soon to be in a much loftier position) should ever find himself in need of…"

        julia "companionship,"

        julia "Julia is a most beautiful young woman and very capable of discretion."

        dr.c "Yes…she is very lovely. Though I have heard that she is married to one Orsino Orsini, is she not? Would he prove himself to be a problem in this regard?"

        julia "Far from it, Your Eminence. Orsino Orsini is a weak-willed man, and would not object to anything Julia asks of him."

        dr.c "I see…"

        dr.c "…"

        dr.c "Well I shall think on the matter, and write to you. But know that I am…very intrigued by this suggestion, Dioneo, and I am {i}very{/i} amenable to the idea of it."

        $dr.add_opinion(julia_name, 15)

        julia "Of course, Your Eminence."

        j_int "Cardinal or no, it seems no man can resist the temptation of beauty, and certainly not that of the most beautiful woman in Italy."

        j_int "Even if I decide not to support della Rovere, it’s good to have planted the seed in his mind."

        j_int "Though if I want to be his mistress and papal hostess, I’ll have to do much more than this to win him over…"

        jump .conclusion

    label .c2:

        dr.c "Oh?"

        julia "I wouldn’t want to suggest anything dishonest of course, but I could provide you with the vote tallies after they take place, Your Eminence."

        dr.c "It would be very useful to know the vote counts, if only so that I can confirm that I can trust those who claim to be voting with me."

        j_int "Should I offer to switch votes for della Rovere? It would make him more likely to help with our debts, but if I decided to support someone else,"
        
        j_int "he might accuse me of cheating and have me thrown out of my position. My secret could be revealed…"

        j_int "No, it’s too risky. But that doesn’t mean I can’t switch votes for him anyway. And giving him the vote counts will prove my loyalty in the meantime, while not making me tied to him."

        julia "I would be more than happy to provide you with the vote tallies, Your Eminence."
        
        julia "But please keep in mind my family’s troubles. The Farneses are still a noble family of Rome, and could prove a useful ally to any future pope."

        dr.c "Of course. I shall not forget my friends when I sit upon the papal throne, and you can trust that I will bear your support in mind."

        $ dr.add_opinion(julia_name, 5)

        jump.conclusion

    label .conclusion:
        
        dr.c "Well I shan’t keep you any longer, then. And here, a tip for your troubles."

        narrator "[[He gives you a single florin. An obscene amount of money for most other functionaries, but to you merely a drop in the bucket of your family’s debts.]"

        julia "Thank you, Your Eminence."

        hide julius

        narrator "[[Julius walks off, and immediately pulls Cardinal Riario away to discuss something. This could be a good sign, but Riario seems suspicious of you, and it could spell disaster if they get too close to discovering your real identity.]"

        j_int "…Well."

        j_int "Della Rovere is certainly confident (though arrogant might be a better word)."
        
        j_int "If his confidence is actually as well-founded as he seems to believe, I could be in a very good position by sticking to his side."

        j_int "His association with the French does make him a hard sell."
        
        j_int "Maybe if I switched some votes in his favor or swayed the other cardinals to his side, I might be able to help him along. He is still Italian after all (at least more than Borgia anyway)."

        j_int "And there’s a cold fire in his eyes, an ambition just barely hidden behind his veneer of gentility. I have little doubt that such a man seeks power, power that he could share with me if I were at his side…"

        return