template = [
    "\t".join([
        "{attack_icon} {attack}",
        "{constitution_icon} {constitution}",
        "{mining_icon} {mining}",
    ]),
    "\t".join([
        "{strength_icon} {strength}",
        "{agility_icon} {agility}",
        "{smithing_icon} {smithing}",    
    ]),
    "\t".join([
        "{defence_icon} {defence}",
        "{herblore_icon} {herblore}",
        "{fishing_icon} {fishing}",    
    ]),
    "\t".join([
        "{ranged_icon} {ranged}",
        "{thieving_icon} {thieving}",
        "{cooking_icon} {cooking}",    
    ]),
    "\t".join([
        "{prayer_icon} {prayer}",
        "{crafting_icon} {crafting}",
        "{firemaking_icon} {firemaking}",    
    ]),
    "\t".join([
        "{magic_icon} {magic}",
        "{fletching_icon} {fletching}",
        "{woodcutting_icon} {woodcutting}",    
    ]),
    "\t".join([
        "{runecrafting_icon} {runecrafting}",
        "{slayer_icon} {slayer}",
        "{farming_icon} {farming}",    
    ]),
    "\t".join([
        "{construction_icon} {construction}",
        "{hunter_icon} {hunter}",
        "{summoning_icon} {summoning}",
    ]),
    "\t".join([
       "{dungeoneering_icon} {dungeoneering}",
       "{divination_icon} {divination}",
       "{invention_icon} {invention}"    
    ])
]

skill_page = "\n".join(template)

def insert(icons, values):
    _icons = {
        f"{key}_icon": value 
        for key, value 
        in icons.items()
    }
    return skill_page.format(**_icons, **values)
