# special.py
# Cards that need special treatment.

# The following split cards are stored under one multiverseid. HTML for each
# part must be extracted separately.

# (Note: The Invasion and Apocalypse split cards have one multiverseid for
# each half of the card.)

split_cards = {
    109704: ["Assault", "Battery"],         # TSB
    205409: ["Assault", "Battery"],         # Planechase
    126218: ["Boom", "Bust"],               # Planar Chaos
    107373: ["Bound", "Determined"],        # DIS
    205384: ["Order", "Chaos"],             # Planechase
    107285: ["Crime", "Punishment"],        # DIS
    126419: ["Dead", "Gone"],               # Planar Chaos
    107464: ["Supply", "Demand"],           # DIS
    107375: ["Research", "Development"],    # DIS
    107445: ["Odds", "Ends"],               # DIS
    107259: ["Trial", "Error"],             # DIS
    107423: ["Rise", "Fall"],               # DIS
    107315: ["Hide", "Seek"],               # DIS
    107387: ["Hit", "Run"],                 # DIS
    107532: ["Pure", "Simple"],             # DIS
    126420: ["Rough", "Tumble"],            # Planar Chaos
    220502: ["Wax", "Wane"],                # ARC
}

PARTIAL_CARD_URL = "http://gatherer.wizards.com/Pages/Card/Details.aspx?"\
                 + "multiverseid=%(multiverseid)&part=%(partname)"

UNGLUED_TOKENS = [
    5503,     # Goblin
    4979,     # Pegasus
    5560,     # Sheep
    5472,     # Soldier
    5607,     # Squirrel
    5601,     # Zombie
]

