from Themes._themeloader import select_theme
from .combat_styles import simple_combat
                    # more import of following required:
                    # hax_combat, 
                    # luck_factor



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








    #Here goes the final output of function 1
    return theme, build