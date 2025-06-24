def start_test_theme():
    return {
        "name": "Test Theme",
        "canon_trigger": {
            "type": "step_counter",
            "threshold": 3
        },
        "counters": {
            "steps": 0,
            "magic_pear": 0,
            "magic_potion": 0
        },
        "available": {
            "steps": 100,
            "magic_pear": 20,
            "magic_potion": 20
        },
        "events": {
            "event_1": {
                "name": "BEAR ATTACK!",
                "description": "A feral bear charges at you from the undergrowth!",
                "type": "combat",
                "win": ("HIDE", "ASSASSINATE") #need to put conditions on wins
            },
            "event_2": {
                "name": "ABANDONED CAMP",
                "description": "You find a deserted camp with a faint smell of stew still in the air.",
                "type": "exploration",
                #need to select win moes and conditions
            },
            "event_3": {
                "name": "MYSTERIOUS TRADER",
                "description": "A hooded figure offers you rare items in exchange for something valuable.",
                "type": "trade",
                #need to select win moes and conditions
            },
            "event_4": {
                "name": "SINKING MUD",
                "description": "Your foot suddenly sinks into mud — it's a trap!",
                "type": "trap",
                #need to select win moes and conditions
            },
            "event_5": {
                "name": "HAUNTED WHISPER",
                "description": "You hear whispers calling your name from the trees...",
                "type": "mystical",
                #need to select win moes and conditions
            },
            "event_6": {
                "name": "CAVE DISCOVERY",
                "description": "You stumble upon a dark cave with glowing crystals inside.",
                "type": "exploration",
                #need to select win moes and conditions
            },
            "event_7": {
                "name": "BANDIT STANDOFF",
                "description": "3 Bandits ambush you! Where did they come from?",
                "type": "combat",
                #need to select win moes and conditions
            },
            "event_8": {
                "name": "WOLF PACK AMBUSH",
                "description": "Eyes in the dark. You’re surrounded. How you move now matters.",
                "type": "combat",
                #need to select win moes and conditions
            },
            "event_9": {
                "name": "RAVEN NEST HOARD",
                "description": "High above, a tangle of shiny things glitters in a giant nest. The birds are watching.",
                "type": "exploration",
                #need to select win moes and conditions
            },
            "event_10": {
                "name": "DISMANTLED SENTINEL",
                "description": "A rusted guardian twitches back to life, scanning you for threats.",
                "type": "combat",
                #need to select win moes and conditions
            }
        },
        "bosses": { #need to create bosses with particular stats and stage various actions
            "boss_1": {
        
            },
            "boss_2": {

            },
            "boss_3": {

            },
            "boss_4": {

            },
            "boss_5": {

            },
            "boss_6": {

            }
        },
        "choices": {
            "combat": {
                    "FIGHT": "Engage in combat.",
                    "HIDE": "Attempt to hide.",
                    "ASSASSINATE": "Go stealth mode.",
                    "RUN": "Flee back.",
                    "NEGOTIATE": "Try to communicate.",
                    "BLUFF": "Try to scare with words."
                },
            "exploration": {
                    "SEARCH": "Search for items",
                    "REST": "Take a short nap to recover HP",
                    "STEAL": "Loot aggressively and leave",
                    "DESTROY": "Rough it up like a maniac"
                },
            "trade": {
                    "TRADE PEAR": "Trade your magic pear",
                    "TRADE POTION": "Trade your potion",
                    "ASK FOR GIFT": "Beg for a freebie",
                    "ROB": "If you think you can win!",
                    "IGNORE": "Just walk away silently"
                },
            "trap": {
                    "STRUGGLE": "Resist against the force",
                    "CALL FOR HELP": "Strain your vocals",
                    "PERCEIVE": "Feel the force and think a way",
                    "SACRIFICE ITEM": "Drop an item to escape"
                },
            "mystical": {
                    "FOLLOW": "Walk towards it",
                    "COVER EARS": "Block it out and run",
                    "CHANT": "Recite a protective chant",
                    "ASK WHO": "Try to converse"
                },
        },
    "types": {
        "combat": 0,
        "exploration": 0,
        "trade": 0,
        "trap": 0,
        "mystical": 0,
        }
    }
