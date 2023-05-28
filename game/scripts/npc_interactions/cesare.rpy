label cesare_d1:
    scene bg sistine

    j_int "I haven’t spoken much with Cesare Borgia since my arrival at the Sistine. He’s one of my brother’s closest friends, and he knows me as Julia well enough to probably recognize me."

    j_int "But I’ve been keeping my head down as Dioneo and hoping that he’ll be too busy courting votes for his father to notice that I’m here."

    j_int "Not that I’m terribly worried about it, but the fewer people that have leverage over me the safer–"

    show cesare

    cesare.c "Dioneo. I’d like to have a word."
    play music royal

    j_int "Oh, shit."

    narrator "Cesare Borgia drags you over to a darkened alcove and pushes you against the wall, eyes lit up in fury and something else…Oh. He’s worried."

    cesare.c "What are you doing here, Julia? Are you insane? You’re lucky my father’s memory isn’t as sharp as mine, or you’d have been thrown out of the Sistine in disgrace!"

    julia "Don’t say my name out loud! And it’s not like I want to be here, but the Farnese family needs me! And someone needs to keep an eye on Alessandro."

    menu:
        cesare.c "You don’t trust me to do it? He’s one of my dearest friends, you know that I’d never let anything happen to him."

        "It's not that I don't trust you...":
            jump .c1

        "The election is too important to leave in just Alessandro’s hands…":
            jump .c2

        "This is an opportunity I couldn’t afford to waste…":
            jump.c3


    label .c1:

        julia "But you’re a busy man, and you’re about to become even busier if your father is elected."
        
        julia "How could I ask you to risk your precious time for the sake of one man, when all of Italy hangs in the balance?"

        cesare.c "This election is important, yes, but look around Julia. This is a den of snakes, men who will do anything for power."

        cesare.c "To have friends with me is a great comfort, one I cannot afford to lose."

        julia "Then you will continue to watch after him?"
        
        julia "This is a great opportunity for us to elevate our family, but it is also an opportunity for others to try and take advantage of our current losses."

        cesare.c "I will do everything in my power to protect your brother and you, Julia, and I will see that my father does the same."

        j_int "What a relief. A part of me has worried that maybe Cesare would blackmail me or my brother if he knew that I was here, but it is good to know that he is as true as ever."

        j_int "Power drives people to do strange things (case in point right here), but if Cesare remains steadfast, that’s one less enemy to worry about."

        julia "Thank you, Cesare. If I can help you in any way, I will do my very best."

        cesare.c "While I think the wisest course of action for you would be to keep your head down during this whole thing and stay out of trouble, your position as a vote counter is invaluable."

        cesare.c "No other cardinal, except maybe Piccolomini or della Porta, will be trying to win this election by fair and honest means."

        cesare.c "My father must do whatever it takes in order to win, and if you could lend your position to our cause, I could do more than just protect you in the Sistine."

        cesare.c "We both want to see your family raised back to its noble status, and it would be so much easier to accomplish from the right hand of the pope."

        menu:
            "Of course I will support your father as pope…":

                $ cesare.add_opinion(julia_name, 10)
                
                cesare.c "Thank you, Julia. Or, Dioneo I should say."

                julia "Of course, Cesare. It is good to know that I have another friend here."

                j_int "It is too bad that Cesare is young and only an archbishop, he has far more strength and wit than his station would allow."
                
                j_int "But if there is to be a Borgia pope, it will not be Cesare but his father, and that is who I need to really endear myself to."

                j_int "Helping Cesare will help us both in our goals, and he is a friend I’d rather not lose…"

                jump .conclusion

            "I will have to think about it…":

                cesare "I see. Keep what I say in mind, and be warned: neutrality can only get one so far."

                j_int "Hm. True, but Cesare is biased towards his father, and until it’s clear where the chips will fall, I’m better off not declaring my support just yet."

                jump .conclusion

    label .c2:

        julia "I couldn’t sit back and do nothing while the fate of Italy hangs in the balance, and though the Farneses aren’t as powerful as we once were, I had to ensure our influence is wielded for the right candidate."

        cesare.c "My father, of course. I’ve been doing all I can for him, but there are so many people to talk to it sometimes sets my mind spinning."

        julia "Perhaps I can help. I have overheard many of the cardinals’ conversations, and because I know which way they are voting, I can offer you some insight as to who would be best to pull to your father’s side."

        cesare.c "Who should I speak to, then?"

        menu .who_to_influence:
            "Guelphs":

                $ promise = drive_out_colonna.generate_promise(borgia, orsini)
                $ promise.make()

                cesare.c "I’ll take your advice into account. Thank you Jul- I mean Dioneo, and be safe."

                jump .conclusion

            "Dominicans":

                $ promise = sacred_palace.generate_promise(borgia, carafa)
                $ promise.make()

                cesare.c "I’ll take your advice into account. Thank you Jul- I mean Dioneo, and be safe."

                jump .conclusion

            "Genoans":

                $ promise = independent_genoa.generate_promise(borgia, gentili)
                $ promise.make()

                cesare.c "Hm…both of them have far more reason to listen to Sforza or della Rovere, but I’ll consider it."

                jump .conclusion

            "Leo":
                $ promise = vice_chancellor.generate_promise(borgia, medici)
                $ promise.make()

                cesare.c "Hm... Getting him on my side early could be very good. I'll think about it."

                jump .conclusion

    label .c3:

        julia "My father was a foolish man and left Alessandro and I saddled with his debts."
        
        julia "Dangerous though it may be, the election may be the best chance we have to make the connections we need to get out of this hole."

        cesare.c "I suppose that’s true enough."
        
        cesare.c "All my efforts are so completely bent towards my father’s papacy that I forget there are other boons that can come from this gathering of cardinals."

        julia "It’s a worthy goal, and will do far more for your family than anything else. I admire your loyalty to them."

        cesare.c "Yes well, if only my father felt as you do. Perhaps then he would see where my true usefulness lies:"
        
        cesare.c "not here, stifled in the robes of a priest, but in my brother’s place on the battlefield."

        j_int "I too know how it feels to be stifled. I could be descended from the most noble family in Rome, and yet the cardinals here would see me as little more than a card to be exchanged."
        
        j_int "But it is also better that way. Better for them to think me nothing more than a beautiful prize to be won than to grasp my true desire, while I slowly ensure that I have wrung promises and power from each of them."

        julia "I’m sure your father will see you as I do in time. And if he does not…well. Once you help him secure your family’s power, I’m sure you will be able to wield it to your advantage. There is a great deal of power in being overlooked."

        cesare.c "You’re right. You Farneses all have a knack for good advice, it seems."

        $ cesare.add_opinion(julia_name, 15)

        julia "So long as you don’t forget us when you’ve risen to the top of the Vatican."

        cesare.c "Never! You and Alessandro shall be taken care of so long as I have the strength to grasp a sword."

        julia "A long time, I expect. Well, I shouldn’t keep you any longer, and if we spend any longer hidden away, people might talk."

        cesare.c "Farewell then, and be safe. If anyone causes you trouble, do not hesitate to speak to me about it."

        j_int "A valuable friend, who will undoubtedly be more valuable if his father becomes pope. He probably won’t like the part of my plan that involves seducing his father, but I hope he will understand."
        
        j_int "I don’t want to hurt him, but my family’s fortunes must come first…"

        stop music

        return


    cesare.c "I'm going to be making a promise to Leo, to see if I can win him over. Should I?"

    julia "Do it."

    $ c_promise = vice_chancellor.generate_promise(borgia, medici)
    $ c_promise.make()

    label .conclusion:

        cesare.c "Well, regardless, good luck Ju— I mean, Dineo. And be safe."

        julia "Thank you. And you as well."
        stop music

        return