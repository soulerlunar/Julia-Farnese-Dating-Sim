label interact_menu(npc_list, event_code):
    python:
        options = []
        for npc in npc_list:
            options.append((npc.c.name, npc.name))

        narrator("Who should I speak with?", interact=False)
        result = renpy.display_menu(options)

        renpy.jump(result + "_" + event_code)