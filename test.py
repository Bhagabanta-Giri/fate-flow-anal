test = "Value"

if test:
    print("Success!")
else:
    print("Failure")



from Engine.fate import pick_your_poison
from Engine.player import create_player



theme, build, hax, Fatebound, name = pick_your_poison()

player = create_player(name, build, hax, Fatebound)

print(player)
print(theme) 