# sets.py
#
# Also see:
# http://en.wikipedia.org/wiki/List_of_Magic:_The_Gathering_sets

class S:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(**kwargs)
    def __getattr__(self, name):
        return None

set_info = {

    # Set names are those used by Gatherer.
    # Set trigrams (keys) are those used by Wikipedia.

    # aliases are sometimes used in the sidebar of search results (e.g. "ODY"
    # -> "OD"), in order to find multiple versions of the same card (usually
    # basic lands).

    '10E': S(name="Tenth Edition",
             cards=383,
             date="2007-07-14"),

    '2ED': S(name="Unlimited Edition",
             cards=302,
             date="1993-12",
             alias="2U"),

    '3ED': S(name="Revised Edition",
             cards=306,
             date="1994-04",
             alias="3E"),

    '4ED': S(name="Fourth Edition",
             cards=378,
             date="1995-04",
             alias="4E"),

    '5DN': S(name="Fifth Dawn",
             cards=165,
             date="2004-06-04"),

    '5ED': S(name="Fifth Edition",
             cards=449,
             date="1997-03-24",
             alias="5E"),

    '6ED': S(name="Classic Sixth Edition",
             cards=350,
             date="1999-04-28",
             alias="6E"),

    '7ED': S(name="Seventh Edition",
             cards=350,
             date="2001-04-11",
             alias="7E"),

    '8ED': S(name="Eighth Edition",
             cards=357,
             date="2003-07-28"),

    '9ED': S(name="Ninth Edition",
             cards=360, # Wikipedia says 359, hmm
                        # includes 4 versions of each basic land
             date="2005-07-29"),

    'ALA': S(name="Shards of Alara",
             cards=249, # 229 + 4*5 basic lands
             date="2008-10-03"),

    'ALL': S(name="Alliances",
             cards=144, # all commons had 2 alternate art versions; these have
                        # the same ids in Gatherer, otherwise the set size
                        # would be 199
             date="1996-06-10"),

    'APC': S(name="Apocalypse",
             cards=143,
             date="2001-06-04"),

    'ARB': S(name="Alara Reborn",
             cards=145,
             date="2009-04-30"),

    'ARN': S(name="Arabian Nights",
             cards=78, # 92 if counting alternate art versions
             date="1993-12"),

    'ATQ': S(name="Antiquities",
             cards=85, # 100 if counting alternate art versions
             date="1994-03"),

    'BOK': S(name="Betrayers of Kamigawa",
             cards=165,
             date="2005-02-04"),

    'CHK': S(name="Champions of Kamigawa",
             cards=307, # 306+1; Brothers Yamazaki has two versions with
                        # different ids
             date="2004-10-01"),

    'CHR': S(name="Chronicles",
             cards=16, # 125 when counting alternate art versions
             date="1995-07"),

    'CON': S(name="Conflux",
             cards=145,
             date="2009-02-06"),

    'CSP': S(name="Coldsnap",
             cards=155,
             date="2006-07-21"),

    'DIS': S(name="Dissension",
             cards=180,
             date="2006-05-05"),

    'DRK': S(name="The Dark",
             cards=119,
             date="1994-08"),

    'DST': S(name="Darksteel",
             cards=165,
             date="2004-02-06"),

    'EVE': S(name="Eventide",
             cards=180,
             date="2008-07-25"),

    'EXO': S(name="Exodus",
             cards=143,
             date="1998-06-15"),

    'FEM': S(name="Fallen Empires",
             cards=102, # 187 when counting alternate art versions
             date="1994-11"),

    'FUT': S(name="Future Sight",
             cards=180,
             date="2007-05-04"),

    'GPT': S(name="Guildpact",
             cards=165,
             date="2006-02-03"),

    'HML': S(name="Homelands",
             cards=115, # 140 when counting alternate art versions
             date="1995-10"),

    'ICE': S(name="Ice Age",
             cards=383,
             date="1996-06",
             alias="IA"),

    'INV': S(name="Invasion",
             cards=355, # 350 "physical" cards, of which 5 are split cards 
                        # which count double (and have two multiverse ids, 
                        # one for each part)
             date="2000-10-02",
             alias="IN"),

    'JUD': S(name="Judgment",
             cards=143,
             date="2002-05-27"),

    'LEA': S(name="Limited Edition Alpha",
             cards=295,
             date="1993-08-05",
             alias="1E"),

    'LEB': S(name="Limited Edition Beta",
             cards=302,
             date="1993-10",
             alias="2E"),

    'LEG': S(name="Legends",
             cards=310,
             date="1994-06"),

    'LGN': S(name="Legions",
             cards=145,
             date="2003-02-03"),

    'LRW': S(name="Lorwyn",
             cards=301,
             date="2007-10-12"),

    'M10': S(name="Magic 2010",
             cards=249,
             date="2009-07-17"),

    'M11': S(name="Magic 2011",
             cards=249,
             date="2010-07-16"),

    'MIR': S(name="Mirage",
             cards=350,
             date="1996-10-08",
             alias="MI"),

    'MMQ': S(name="Mercadian Masques",
             cards=350,
             date="1999-10-04",
             alias="MM"),

    'MOR': S(name="Morningtide",
             cards=150,
             date="2008-02-01"),

    'MRD': S(name="Mirrodin",
             cards=306,
             date="2003-10-02"),

    'NMS': S(name="Nemesis",
             cards=143,
             date="2000-02-14"),

    'ODY': S(name="Odyssey",
             cards=350,
             date="2001-10-01",
             alias="OD"),

    'ONS': S(name="Onslaught",
             cards=350,
             date="2002-10-07"),

    'P02': S(name="Portal Second Age",
             cards=165,
             date="1998-06",
             alias="P2"),

    'PCY': S(name="Prophecy",
             cards=143,
             date="2000-06-05"),

    'PDS': S(name="Premium Deck Series: Slivers",
             cards=41, # 60-card deck with 41 unique cards
             date="2009-11-20"),

    'PLC': S(name="Planar Chaos",
             cards=165,
             date="2007-02-02"),

    'PLS': S(name="Planeshift",
             cards=143,
             date="2001-02-05"),

    'POR': S(name="Portal",
             cards=222,
             date="1997-06",
             alias="PO"),

    'PTK': S(name="Portal Three Kingdoms",
             cards=180,
             date="1999-05",
             alias="PK"),

    'RAV': S(name="Ravnica: City of Guilds",
             cards=306,
             date="2005-10-07"),

    'ROE': S(name="Rise of the Eldrazi",
             cards=248,
             date="2010-04-23"),

    'S00': S(name="Starter 2000",
             cards=57,
             date="2000-07",
             alias="P4"),

    'S99': S(name="Starter 1999",
             cards=173,
             date="1999-07",
             alias="P3"),

    'SCG': S(name="Scourge",
             cards=143,
             date="2003-05-26"),

    'SHM': S(name="Shadowmoor",
             cards=301,
             date="2008-05-02"),

    'SOK': S(name="Saviors of Kamigawa",
             cards=165,
             date="2005-06-03"),

    'SOM': S(name="Scars of Mirrodin",
             cards=249,
             date="2010-10-01"),

    'STH': S(name="Stronghold",
             cards=143,
             date="1998-03-02"),

    'TMP': S(name="Tempest",
             cards=350,
             date="1997-10-14",
             alias="TE"),

    'TOR': S(name="Torment",
             cards=143,
             date="2002-02-04"),

    'TSB': S(name='Time Spiral "Timeshifted"',
             cards=121,
             date="2006-10-06"),

    'TSP': S(name="Time Spiral",
             cards=301,
             date="2006-01-06"),

    'UDS': S(name="Urza's Destiny",
             cards=143,
             date="1999-06-07"),

    'ULG': S(name="Urza's Legacy", 
             cards=143,
             date="1999-02-15"),

    'USG': S(name="Urza's Saga",
             cards=350,
             date="1998-10-12",
             alias="UZ"),

    'VIS': S(name="Visions",
             cards=167,
             date="1997-02-03"),

    'WTH': S(name="Weatherlight",
             cards=167,
             date="1997-06-09"),

    'WWK': S(name="Worldwake",
             cards=145,
             date="2010-02-05"),

    'ZEN': S(name="Zendikar",
             cards=249, # 229 + 8*5 basic lands; each basic land has 4 "regular"
                        # versions and 4 versions without a text box
             date="2009-10-2"),

}


# TODO: aliases:
# Starter 2000 = P4
# Beatdown Box Set = BD
# Battle Royale Box Set = BR
# Mercadian Masques = MM
# Starter 1999 = P3
# Portal Three Kingdoms = PK
# Unglued = UG
# Portal Second Age = P2
# Portal = PO
# Unlimited Edition = 2U
# Limited Edition Beta = 2E
# Limited Edition Alpha = 1E
# Revised Edition = 3E

