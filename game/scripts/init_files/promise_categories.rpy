init 2 python:
    promise_types = {} #dictionary of promise categories. (name, PromiseCategory)

    papabile = PromiseCategory("papabile")
    defensive_vote = PromiseCategory("defensive")
    for npc in npcs.values():
        papabile.add_influenced(npc, 40)
        defensive_vote.add_influenced(npc, 20)

    vice_chancellor = PromiseCategory("Vice Chancellor")
    vice_chancellor.add_influenced(medici, 30)

    sacred_palace = PromiseCategory("Sacred Palace")
    vice_chancellor.add_influenced(carafa, 25)

    drive_out_colonna = PromiseCategory("Drive out Colonna")
    drive_out_colonna.add_influenced(orsini, 30)

    independent_genoa = PromiseCategory("Independent Genoa")
    independent_genoa.add_influenced(gentili, 25)

    protect_siena = PromiseCategory("Protect Siena")
    protect_siena.add_influenced(piccolomini, 25)