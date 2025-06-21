from Themes._themeloader import select_theme
from .combat_styles import simple_combat, hax_combat




def pick_your_poison():

    #Here goes Question 1, for theme
    print("Q1. Do you enjoy whatever you are doing?")
    print("(a) Yes a lot!")
    print("(b) Maybe,depends on mood...")
    print("(c) Its alright, I can manage")
    print("(d) Nah man, I wanna quit!")
    while True:
        theme_pick = input("> ").strip().lower()
        if theme_pick == "a":
            label = "realistic"
            break
        elif theme_pick == "b":
            label = "wishful"
            break
        elif theme_pick == "c":
            label = "dream"
            break
        elif theme_pick == "d":
            label = "fantasy"
            break
        else:
            print("Invalid input. Try again with a letter between a–d!")
    theme = select_theme(label)


    #Here goes Question 2, for combat
    print("Q2. What’s your idea of ‘the best’ way to face fate?")
    print("Choose your style:")
    print(" (a) The Juggernaut     — Powerhouse of health and brute strength")
    print(" (b) The Strategist     — Cold mind, cool nerves, always 3 steps ahead")
    print(" (c) The Berserker      — Chaos-fueled fury and raw muscle")
    print(" (d) The Ghost          — Vanishes in shadows, strikes with precision")
    print(" (e) The Sentinel       — Stalwart and unshakable in body and soul")
    print(" (f) The Oracle         — Sees patterns, connects dots, bends reality")
    print(" (g) The Survivor       — Endures what others can’t. Unkillable, unshaken")
    print(" (h) The Reaper         — A ticking time bomb of perception and rage")
    choices_1 = {
        "a": "Juggernaut",
        "b": "Strategist",
        "c": "Berserker",
        "d": "Ghost",
        "e": "Sentinel",
        "f": "Oracle",
        "g": "Survivor",
        "h": "Reaper"
    }
    while True:
        build_pick = input("> ").strip().lower()
        if build_pick in choices_1:
            build = simple_combat[choices_1[build_pick]]
            break    
        else:
            print("Invalid input. Try again with a letter between a–h!")


    #Here goes Question 3, for Hax
    print("\nDo you wish to activate a HAX module?")
    print("Note: HAX is an active state will only activate when you prompt it.")
    print("Note: HAX prompt will only appear in special canon event.")
    print("Choose your patch (optional glitch upgrade):")
    print(" (a) Glass Cannon       — +10 Strength / -10 HP — Hard hitter, soft shell.")
    print(" (b) Neural Overclock   — +10 Intelligence / -10 Endurance — Fast brain, weak body.")
    print(" (c) Zen Matrix         — +10 Calmness / -10 Rage — Unshakeable but boring in fights.")
    print(" (d) Adrenal Loop       — +10 Rage / -10 Calmness — Always on edge, always dangerous.")
    print(" (e) Soul Firewall      — +10 Willpower / -10 Perception — Strong mind, blind eyes.")
    print(" (f) Perceptive Glitch  — +10 Perception / -10 Intelligence — Sees all, gets confused.")
    print(" (g) Nano Regen Bug     — +10 HP / -10 Strength — Tank mode, noodle arms.")
    print(" (h) Pain Converter     — +10 Endurance / -10 Willpower — Painproof but mentally fragile.")
    print(" (x) No thanks, I follow fate. ")
    choices_2 = {
        "a": "Glass Cannon",
        "b": "Neural Overclock",
        "c": "Zen Matrix",
        "d": "Adrenal Loop",
        "e": "Soul Firewall",
        "f": "Perceptive Glitch",
        "g": "Nano Regen Bug",
        "h": "Pain Converter",
    }
    while True:
        hax_pick = input("> ").strip().lower()
        if hax_pick in choices_2:
            hax = hax_combat[choices_2[hax_pick]]
            Fatebound = False
            break
        elif hax_pick == "x":
            print("\nYou chose no HAX. Fate will reward you in mysterious ways...")
            hax = False
            Fatebound = True
            break
        else:
            print("Invalid input. Choose a–h or x.")


    #Here goes Question 3, for name
    name = input("Enter your name, mortal \n")





    #Here goes the final output of function 1
    return theme, build, hax, Fatebound, name