init 10 python:
    #dr
    dr.set_opinion(borgia, 45)
    dr.set_opinion(sforza, 50)
    
    dr.set_opinion(riario, 80)
    dr.set_opinion(piccolomini, 60)
    dr.set_opinion(riario, 20)
    dr.set_opinion(colonna, 60)

    dr.set_opinion(cesare, 30)
    dr.set_opinion(caterina, 70)

    #BORGIA
    borgia.set_opinion(dr, 40)
    borgia.set_opinion(sforza, 55)
    
    borgia.set_opinion(riario, 40)
    borgia.set_opinion(piccolomini, 60)
    borgia.set_opinion(riario, 65)
    borgia.set_opinion(colonna, 55)

    borgia.set_opinion(cesare, 85)
    borgia.set_opinion(caterina, 40)

    #SFORZA
    sforza.set_opinion(dr, 40)
    sforza.set_opinion(borgia, 40)
    
    sforza.set_opinion(riario, 50)
    sforza.set_opinion(piccolomini, 60)
    sforza.set_opinion(riario, 75)
    sforza.set_opinion(colonna, 70)

    sforza.set_opinion(cesare, 40)
    sforza.set_opinion(caterina, 85)

    #MEDICI
    medici.set_opinion(dr, 25)
    medici.set_opinion(borgia, 45)
    medici.set_opinion(sforza, 70)
    
    medici.set_opinion(riario, 30)
    medici.set_opinion(piccolomini, 65)
    medici.set_opinion(colonna, 50)

    medici.set_opinion(cesare, 80)
    medici.set_opinion(caterina, 70)

    #RIARIO
    riario.set_opinion(dr, 90)
    riario.set_opinion(borgia, 35)
    riario.set_opinion(sforza, 65)
    
    riario.set_opinion(medici, 30)
    riario.set_opinion(piccolomini, 65)
    riario.set_opinion(colonna, 65)

    riario.set_opinion(cesare, 30)
    riario.set_opinion(caterina, 70)

    #COLONNA
    colonna.set_opinion(dr, 65)
    colonna.set_opinion(borgia, 55)
    colonna.set_opinion(sforza, 70)
    
    colonna.set_opinion(riario, 60)
    colonna.set_opinion(piccolomini, 70)
    colonna.set_opinion(medici, 50)

    colonna.set_opinion(cesare, 45)
    colonna.set_opinion(caterina, 70)

    #PICCOLOMINI
    piccolomini.set_opinion(dr, 50)
    piccolomini.set_opinion(borgia, 50)
    piccolomini.set_opinion(sforza, 60)
    
    piccolomini.set_opinion(riario, 65)
    piccolomini.set_opinion(caterina, 65)
    piccolomini.set_opinion(colonna, 50)

    piccolomini.set_opinion(cesare, 50)
    piccolomini.set_opinion(caterina, 60)

    #CATERINA
    caterina.set_opinion(dr, 65)
    caterina.set_opinion(borgia, 50)
    caterina.set_opinion(sforza, 85)
    
    caterina.set_opinion(riario, 70)
    caterina.set_opinion(piccolomini, 65)
    caterina.set_opinion(colonna, 60)
    caterina.set_opinion(medici, 65)

    caterina.set_opinion(cesare, 40)

    #CESARE
    cesare.set_opinion(dr, 35)
    cesare.set_opinion(borgia, 90)
    cesare.set_opinion(sforza, 40)
    
    cesare.set_opinion(riario, 30)
    cesare.set_opinion(piccolomini, 60)
    cesare.set_opinion(colonna, 60)
    cesare.set_opinion(medici, 80)

    cesare.set_opinion(caterina, 55)

    for npc in npcs.values():
        for candidate in voters:
            npc.set_papal_op(candidate, 40)

        j_promise = papabile.generate_promise(dr, npc)
        j_promise.make()
        b_promise = papabile.generate_promise(borgia, npc)
        b_promise.make()
        s_promise = papabile.generate_promise(sforza, npc)
        s_promise.make()