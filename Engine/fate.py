from Themes._themeloader import select_theme
from .combat_styles import (
    simple_combat, 
    hax_combat, 
    luck_factor
)



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
            print("Invalid input. Please try again!")
    theme = select_theme(label)


    #Here goes Question 2, for combat
    print("Q2. What is your idea of survival?")
    print("(a) Attack anything and everything! Make it your own before others!")
    print("(b) Analyse the situtation but attack whenever high win chances")
    print("(c) Analyse the situtation but defend whenever possible")
    print("(d) Always defend, avoid dangers!")
    while True:
        combat_pick = input("> ").strip().lower()
        if combat_pick == "a":
            