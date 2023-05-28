label riario_d1:
    
    scene bg sistine

    j_int "Ah, there’s Cardinal Raffaele Riario. If I want to influence this election beyond just switching votes, he’s definitely going to be important to talk to."
    
    j_int "He’s Cardinal della Rovere’s heir and has his ear and his trust, so if I want to win della Rovere over (or screw him over), I can use Riario to do it."

    j_int "I wonder if he remembers me. The real me, that is."
    
    j_int "We used to party together before the election consumed the thoughts of everyone in Italy, and he’s always been rather fun to hang around."

    j_int "Though he gets rather morose when he’s deep enough in his cups, mumbling about some “Lorenzo.” I wonder if he means the Medici…"

    j_int "Anyway, it’s been a while since we’ve last seen each other, so hopefully he won’t recognize me, but he’s also one of my bosses now, so I’ll need to be careful."

    show riario

    riario.c "Dioneo! Shouldn’t you be collecting votes? I think I heard one of the Maffeis looking for you."

    julia "Yes, of course, Your Eminence, but I was hoping to have a word with you first, if you’re willing."

    riario.c "Fine. What is it?"

    menu:
        "[[show him the portrait of Julia Farnese]":
            jump .c1
        "I was wondering if there was anything I could do to help you and your uncle…":
            jump .c2
        "Never mind…":
            jump .c3
    
    label .c1:
       
        julia "This is my cousin, Julia Farnese."

        riario.c "…I don’t see the appeal."

        j_int "I’m the most beautiful woman in Italy! Is he blind?"

        julia "She is the most beautiful woman in Italy, Your Eminence. And your uncle will be in need of a papal hostess should he become the pope."

        riario.c "I don’t see how beauty has anything to do with it."
        
        riario.c "And my sister-in-law, Caterina Sforza, is the obvious choice for is papal hostess. She’s done it before, and is beloved by Rome."

        $ riario.add_opinion(julia_name, -5)

        julia "…Of course, Your Eminence. Though, if I may, the Farnese family is of ancient and noble Roman blood."
        
        julia "This would be a sure way to win Rome’s favor, especially given your uncle’s ties to the French."

        riario.c "Well I’ll take it into consideration then. I have many people to speak to and far too little time, so I’ll be off then."

        julia "Good day, Your Eminence."

        return

    label .c2:

        riario.c "What did you have in mind?"

        julia "Well, as a vote counter I have certain… access that others, such as yourself, do not."
        
        julia "I have overheard many of the cardinals’ conversations, and because I know which way they are voting, I can offer you some insight as to who would be best to pull to your uncle’s side."

        riario.c "Interesting…It could be a worthwhile deal, though I expect you’d want something in return."

        julia "Well my cousin, Julia Farnese, is an exceptional young woman, and I’ve heard others say she is the most beautiful woman in Italy."
        
        julia "It would be a great boon to the Farnese family and to yours if she were to be your uncle’s papal hostess."

        riario.c " I will have to bring it up with my uncle. My sister-in-law, Caterina Sforza, is already our first choice for the role, you understand."

        julia "Of course, Your Eminence."

        riario.c "But perhaps I could do something about your debt with the Franciscan bank if your information is good. Do you have any suggestions on who I should talk to in the meantime?"

        menu .who_to_influence:
            "Guelphs":

                $ promise = drive_out_colonna.generate_promise(dr, orsini)
                $ promise.make()
                $ riario.add_opinion(julia_name, -5)

                riario.c "Hm. I will take this into consideration."

                jump .after_influence

            "Dominicans":

                riario.c "My uncle is a Franciscan monk, and you think I will be able to sway the Dominicans to our side? I think my time is better spent elsewhere."

                menu:
                    "You're right, my mistake":
                        $riario.add_opinion(julia_name, -5)

                        riario.c "Indeed it was."

                    "But think of the blow it would do to Borgia":
                        $ promise = sacred_palace.generate_promise(dr, carafa)
                        $ promise.make()
                        $riario.add_opinion(julia_name, -10)

                        riario.c "Your opinion is noted."


                jump .after_influence

            "Peace Faction":

                $ promise = protect_siena.generate_promise(dr, piccolomini)
                $ promise.make()
                $ riario.add_opinion(julia_name, 5)

                cesare.c "Hm. I will take this into consideration."

                jump .after_influence

        label .after_influence:

            riario.c "Now get back to work."

            julia "Of course your Eminence. My apologies."

        return
    
    label .c3:

        riario.c "Don’t waste my time again."

        julia "Of course your Eminence. My apologies."

        return