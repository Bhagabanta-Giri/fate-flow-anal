from Themes._themeloader import select_theme

def pick_your_poison():

    #Here goes Question 1
    print("Q1. Do you enjoy whatever you are doing?")
    print("(a) Yes a lot!")
    print("(b) Maybe,depends on mood...")
    print("(c) Its alright, I can manage")
    print("(d) Nah man, I wanna quit!")

    while True:
        theme_pick = input("> ").strip().lower()
        if theme_pick == "a":
            label = "realistic"
        elif theme_pick == "b":
            label = "wishful"
        elif theme_pick == "c":
            label = "dream"
        elif theme_pick == "d":
            label = "fantasy"
        else:
            print("Invalid input. Please try again!")


    #Here goes Question 2
    