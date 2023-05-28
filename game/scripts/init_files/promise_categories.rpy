init 2 python:
    promise_types = {} #dictionary of promise categories. (name, PromiseCategory)

    papabile = PromiseCategory("papabile")
    for npc in npcs.values():
        papabile.add_influenced(npc, 40)