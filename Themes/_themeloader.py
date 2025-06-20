import random

from Themes.city import start_city_theme
from Themes.murder import start_murder_theme
from Themes.village import start_village_theme
from Themes.space import start_space_theme
from Themes.alien import start_alien_theme
from Themes.exoplanet import start_exoplanet_theme
from Themes.forest import start_forest_theme
from Themes.empire import start_empire_theme

themes = {
    "realistic": [start_city_theme, start_murder_theme],
    "wishful": [start_village_theme, start_space_theme],
    "dream": [start_alien_theme, start_exoplanet_theme],
    "fantasy": [start_forest_theme, start_empire_theme],  
}

def select_theme(label):
    theme_list = themes.get(label, False)
    if not theme_list:
        raise ValueError
    return random.choice(theme_list)
