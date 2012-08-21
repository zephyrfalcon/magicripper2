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

double_faced_cards = {
    # Innistrad:
    244683: 244687, # Hanweir Watchkeep / Bane of Hanweir (ISD)
    227061: 227072, # Bloodline Keeper / Lord of Lineage
    221209: 221185, # Civilized Scholar / Homicidal Brute
    221212: 221222, # Cloistered Youth / Unholy Fiend
    222118: 222114, # Daybreak Ranger / Nightfall Predator
    226749: 226755, # Delver of Secrets / Insectile Aberration
    245250: 245251, # Garruk Relentless / Garruk, the Veil-Cursed
    227409: 227290, # Gatstaf Shepherd / Gatstaf Howler
    222124: 222123, # Grizzled Outcasts / Krallenhorde Wantons
    222189: 222183, # Mayor of Avabruck / Howlpack Alpha
    222915: 222906, # Villagers of Estwald / Howlpack of Estwald
    227415: 227419, # Instigator Gang / Wildblood Pack
    222112: 222107, # Village Ironsmith / Ironfang
    227084: 227090, # Kruin Outlaw / Terror of Kruin Pass
    221179: 221173, # Ludevic's Test Subject / Ludevic's Abomination
    222111: 222115, # Reckless Waif / Merciless Predator
    222186: 222117, # Tormented Pariah / Rampaging Werewolf
    221211: 221215, # Screeching Bat / Stalking Vampire
    222016: 221190, # Thraben Sentry / Thraben Militia
    222105: 222108, # Ulvenwald Mystics / Ulvenwald Primordials

    # Dark Ascension:
    262675: 262698, # Afflicted Deserter / Werewolf Ransacker
    227417: 227405, # Ravenous Demon / Archdemon of Greed
    226735: 226721, # Chalice of Life / Chalice of Death
    243229: 244712, # Chosen of Markov / Markov's Servant
    244740: 244738, # Elbrus, the Binding Blade / Withengar Unbound
    222178: 242498, # Soul Seizer / Ghastly Haunting
    247125: 247122, # Hinterland Hermit / Hinterland Scourge
    262875: 262699, # Huntmaster of the Fells / Ravager of the Fells,
    253426: 253431, # Wolfbitten Captive / Krallenhorde Killer
    242537: 242509, # Lambholt Elder / Silverpelt Werewolf
    244724: 244734, # Loyal Cathar / Unhallowed Cathar
    253433: 253429, # Mondronen Shaman / Tovolar's Magehunter
    262694: 262659, # Scorned Villager / Moonscarred Werewolf
}
