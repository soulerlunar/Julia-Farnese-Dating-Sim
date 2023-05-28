init 1 python:
    #BASIC

    npcs = {}
    voters = []
    too_young_cards = []

    j_int = Character(None, what_italic=True)
    julia = Character("Dioneo")
    narrator = Character("", what_bold=True)

    # Params:
    # - voter: boolean
    #
    def register_npc(npc, voter=True, too_young=False):
        npcs[npc.name] = npc
        if voter:
            voters.append(npc)
        if too_young:
            too_young_cards.append(npc)

    #------    
    #DATABLE PARTNERS

    #Giuliano della Rovere
    dr = Partner("julius", Character("Cardinal della Rovere"))
    register_npc(dr, True)

    #Rodrigo Borgia
    borgia = Partner("borgia", Character("Cardinal Borgia"))
    register_npc(borgia, True)

    sforza = Voter("sforza", Character("Cardinal Sforza"))
    register_npc(sforza, True, True)

    #FUNCTIONARIES

    #Alessandro Farnese
    alessandro = NPC("alessandro", Character("Alessandro"), julia_op = 90)
    register_npc(alessandro, False, True)

    #Brother Annio
    annio = NPC("annio", Character("Brother Annio"), julia_op = 50)
    register_npc(annio, False)

    #Cesare Borgia
    cesare = NPC("cesare", Character("Cesare"), julia_op = 70)
    register_npc(cesare, False, True)

    #Mario Maffei
    mario = NPC("mario", Character("Mario Maffei"))
    register_npc(mario, False)

    #------
    #VOTERS

    #Raffaele Riario
    riario = Voter("riario", Character("Cardinal Riario"))
    register_npc(riario, True, True)

    #Francesco Piccolomini
    piccolomini = Voter("piccolomini", Character("Cardinal Piccolomini"), self_op = 70)
    register_npc(piccolomini, True)

    #Giovanni de Medici
    medici = Voter("medici", Character("Cardinal Medici"), julia_op = 70)
    register_npc(medici, True, True)

    #Giovanni Colonna
    colonna = Voter("colonna", Character("Cardinal Colonna"))
    register_npc(colonna, True)

    #Oliviero Carafa
    carafa = Voter("carafa", Character("Cardinal Carafa"))
    register_npc(carafa, True)

    #Gianbattista Orsini
    orsini = Voter("orsini", Character("Cardinal Orsini"), self_op = 100)
    register_npc(orsini, True)

    #Antonio Gentili
    gentili = Voter("gentili", Character("Cardinal Gentili"))
    register_npc(gentili, True)

    #------
    #INTRUDERS

    #Caterina Sforza-Riario
    caterina = NPC("caterina", Character("Caterina Sforza-Riario"), julia_op=40)
    register_npc(caterina, False)