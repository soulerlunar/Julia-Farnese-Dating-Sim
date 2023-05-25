init python:
    #BASIC

    julia = Character(None, what_italic=True)
    narrate = Character("")

    #------    
    #DATABLE PARTNERS

    #Giuliano della Rovere
    dr = Partner(Character("Cardinal della Rovere"))

    #Rodrigo Borgia
    borgia = Partner(Character("Cardinal Borgia"))

    #SUPPORT

    #Alessandro Farnese
    alessandro = NPC(Character("Alessandro"), julia_op = 90)

    #Brother Annio
    annio = NPC(Character("Brother Annio"), julia_op = 50)

    #Cesare Borgia
    cesare = Voter(Character("Cesare"), julia_op = 70)    

    #------
    #VOTERS

    #Raffaele Riario
    riario = Voter(Character("Cardinal Riario"))

    #Francesco Piccolomini
    piccolomini = Voter(Character("Cardinal Piccolomini"), self_op = 70)

    #Giovanni de Medici
    medici = Voter(Character("Giovanni"), julia_op = 70)

    #Giovanni Colonna
    colonna = Voter(Character("Cardinal Colonna"))

    #------
    #INTRUDERS

    #Caterina Sforza-Riario
    caterina = NPC(Character("Caterina Sforza-Riario"), julia_op=40)