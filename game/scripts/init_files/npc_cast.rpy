init 1 python:
    #BASIC

    npcs = []
    voters = []

    j_int = Character(None, what_italic=True)
    julia = Character("Dioneo")
    narrator = Character("")

    #------    
    #DATABLE PARTNERS

    #Giuliano della Rovere
    dr = Partner("julius", Character("Cardinal della Rovere"))
    npcs.append(dr)
    voters.append(dr)

    #Rodrigo Borgia
    borgia = Partner("borgia", Character("Cardinal Borgia"))
    npcs.append(borgia)
    voters.append(borgia)

    #FUNCTIONARIES

    #Alessandro Farnese
    alessandro = NPC("alessandro", Character("Alessandro"), julia_op = 90)
    npcs.append(alessandro)

    #Brother Annio
    annio = NPC("annio", Character("Brother Annio"), julia_op = 50)
    npcs.append(annio)

    #Cesare Borgia
    cesare = Voter("cesare", Character("Cesare"), julia_op = 70)
    npcs.append(cesare)

    #------
    #VOTERS

    #Raffaele Riario
    riario = Voter("riario", Character("Cardinal Riario"))
    npcs.append(riario)
    voters.append(riario)

    #Francesco Piccolomini
    piccolomini = Voter("piccolomini", Character("Cardinal Piccolomini"), self_op = 70)
    npcs.append(piccolomini)
    voters.append(piccolomini)

    #Giovanni de Medici
    medici = Voter("medici", Character("Giovanni"), julia_op = 70)
    npcs.append(medici)
    voters.append(medici)

    #Giovanni Colonna
    colonna = Voter("colonna", Character("Cardinal Colonna"))
    npcs.append(colonna)
    voters.append(colonna)

    #------
    #INTRUDERS

    #Caterina Sforza-Riario
    caterina = NPC("caterina", Character("Caterina Sforza-Riario"), julia_op=40)
    npcs.append(caterina)

    for npc in npcs:
        print(npc.name)