label interact_menu(npc_list, event_code):
    python:
        options = []
        for npc in npc_list:
            options.append((npc.c.name, npc.name))

        j_int("Who must I speak with?", interact=False)
        result = renpy.display_menu(options)

        renpy.call(result + "_" + event_code)