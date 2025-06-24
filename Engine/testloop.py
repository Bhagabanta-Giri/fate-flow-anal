def start_game(player, theme):
    scenes = theme["scenes"]
    counters = theme["counters"]
    canon = theme["canon_trigger"]

    print("\nGame Begins!\n")

    while player["alive"]:
        location = player["location"]
        scene = scenes.get(location)

        if not scene:
            print(f"Unknown location: {location}")
            break

        print(f"\n{location.upper()}")
        print(scene["description"])

        print("\nWhat will you do?")
        for choice in scene["choices"]:
            print(f" - {choice}")

        command = input("> ").strip().lower()

        if command in scene["choices"]:
            new_location = scene["choices"][command]
            player["location"] = new_location
            counters["steps"] += 1

            # Check for canon event trigger
            if canon["type"] == "step_counter" and counters["steps"] >= canon["threshold"]:
                if player.get("hax") and not player["hax"]["activate"]:
                    print("\nA glitch runs through your fate... HAX activated!")
                    for stat, mod in player["hax"]["modifier"].items():
                        player[stat] += mod
                    player["hax"]["hax_count"] += 1
                else:
                    print("\nYou feel fate pulsing... but it passes.")

        else:
            print("Invalid action.")
