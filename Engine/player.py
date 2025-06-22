def create_player(name, build, hax, Fatebound):
    player = {
        "name": name,
        "alive": True,
        "location": "start",
        "inventory": [],
        "flags": set(),
    }
    player.update(build)

    if hax:
        player["hax"] = {
            "modifier": hax,
            "activate": False,
            "hax_count": 0,
        }
        player["Fatebound"] = False
    
    elif Fatebound:
        player["hax"] = False
        player["Fatebound"] = True

    return player