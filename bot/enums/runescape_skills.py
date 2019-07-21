from enum import Enum


class Skills(Enum):
    overall = 0
    attack = 1
    defence = 2
    strength = 3
    constitution = 4
    ranged = 5
    prayer = 6
    magic = 7
    cooking = 8
    woodcutting = 9
    fletching = 10
    fishing = 11
    firemaking = 12
    crafting = 13
    smithing = 14
    mining = 15
    herblore = 16
    agility = 17
    thieving = 18
    slayer = 19
    farming = 20
    runecrafting = 21
    hunter = 22
    construction = 23
    summoning = 24
    dungeoneering = 25
    divination = 26
    invention = 27


icons = {
    "overall": "<:all:602507867639250984>",
    "attack": "<:atk:602506169931530301>",
    "defence": "<:def:602506169990381599>",
    "strength": "<:str:602506170032193536>",
    "constitution": "<:hp:602506169873072139>",
    "ranged": "<:ra:602506169881198613>",
    "prayer": "<:pra:602506169566887939>",
    "magic": "<:magic:602506169969278996>",
    "cooking": "<:cook:602506169772277781>",
    "woodcutting": "<:wc:602506170091175936>",
    "fletching": "<:flet:602506169952501760>",
    "fishing": "<:fish:602506170011353089>",
    "firemaking": "<:fm:602506169726140428>",
    "crafting": "<:craft:602506169982124063>",
    "smithing": "<:smith:602506170015678470>",
    "mining": "<:mine:602506170053165068>",
    "herblore": "<:herb:602506169969541159>",
    "agility": "<:agi:602506169558368298>",
    "thieving": "<:thiev:602506170019741736>",
    "slayer": "<:slay:602506170019610644>",
    "farming": "<:farm:602506169969278986>",
    "runecrafting": "<:rc:602506170007027745>",
    "hunter": "<:hu:602506169893912578>",
    "construction": "<:con:602506169961021490>",
    "summoning": "<:sum:602506169759825922>",
    "dungeoneering": "<:dung:602506170242170880>",
    "divination": "<:div:602506170204422174>",
    "invention": "<:inv:602506169948569610>",
}

skills = [
    "overall",
    "attack",
    "defence",
    "strength",
    "constitution",
    "ranged",
    "prayer",
    "magic",
    "cooking",
    "woodcutting",
    "fletching",
    "fishing",
    "firemaking",
    "crafting",
    "smithing",
    "mining",
    "herblore",
    "agility",
    "thieving",
    "slayer",
    "farming",
    "runecrafting",
    "hunter",
    "construction",
    "summoning",
    "dungeoneering",
    "divination",
    "invention",
]

skill_lookup = {
    "overall": Skills.overall,
    "all": Skills.overall,
    "attack": Skills.attack,
    "defence": Skills.defence,
    "def": Skills.defence,
    "strength": Skills.strength,
    "str": Skills.strength,
    "constitution": Skills.constitution,
    "hp": Skills.constitution,
    "health": Skills.constitution,
    "ranged": Skills.ranged,
    "bow": Skills.ranged,
    "prayer": Skills.prayer,
    "magic": Skills.magic,
    "cooking": Skills.cooking,
    "woodcutting": Skills.constitution,
    "fletching": Skills.fletching,
    "fishing": Skills.fishing,
    "firemaking": Skills.firemaking,
    "crafting": Skills.crafting,
    "smithing": Skills.smithing,
    "mining": Skills.mining,
    "herblore": Skills.herblore,
    "agility": Skills.agility,
    "thieving": Skills.thieving,
    "slayer": Skills.slayer,
    "farming": Skills.farming,
    "runecrafting": Skills.runecrafting,
    "hunting": Skills.hunter,
    "hunter": Skills.hunter,
    "construction": Skills.construction,
    "summon": Skills.summoning,
    "summoning": Skills.summoning,
    "dungeoneering": Skills.dungeoneering,
    "dungeon": Skills.dungeoneering,
    "divination": Skills.divination,
    "invention": Skills.invention,
}
