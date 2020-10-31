import random

adjectives = ["frightening", "scary", "spooky", "shivering", "eerie", "sinister", "hairy",
              "stumbling", "crying", "ghastly", "bloody", "vile", "howling", "ancient",
              "ominous", "dark", "filthy", "abandoned", "looming", "silent", "decaying",
              "forsaken", "crusty", "weeping", "wailing", "dying", "musky", "dirty", "horrid", "condemned", "rotting",
              "hairless", "spoopy", "dripping", "crawling", "thirsty", "munching", "hungry", "wicked", "haunting",
              "banished", "crazed", "rabid", "threatening", "growing", "flailing", "crunchy", "gross", "invisible",
              "screaming", "shouting", "laughing", "menacing", "twisted", "banned", "illegal", "lifeless", "fatigued",
              "troubled", "agonized", "charred", "freakish", "brutish", "colourless", "pale"]
nouns = ["pumpkin", "monster", "skeleton", "witch", "brew", "zombie", "ghoul",
         "ghost", "hag", "beast", "werewolf", "eye", "cobweb", "spider", "snake", "spider", "flesh", "vampire", "smoke",
         "fire", "demon", "cyborg", "robot", "worm", "centipede", "nest", "grave", "tomb", "coffin", "meat", "feet",
         "corncob","skull", "bone", "teeth", "toes", "claws", "horde", "potion", "elixir", "cauldron", "socks", "corpse",
         "spine", "limb", "bones", "trees", "fingers", "villain", "caramel apple", "candy apple", "bug", "weapon",
         "crevice", "being", "humanoid", "gamer", "horse", "centaur", "hooves", "cryptid", "corn stalk", "corn field",
         "feast", "bigfoot", "chupacabra", "tentacle", "homicide", "mystery", "bite", "injury", "hole", "eclipse",
         "moth", "pitchfork", "cannibal", "alien", "U.F.O", "creation", "concoction", "wife"]
descriptor = ["blood", "slime", "terror", "fright", "evil", "fear", "death", "coursework",
              "failing my degree", "depression", "sadness", "rot", "bodily fluids", "bile", "drool", "mourning", "hell",
              "doom", "misery", "tears", "deadlines", "assignments", "wetness", "the presidential election", "St. Andrews",
              "Andrew Melville Hall", "mud", "darkness", "madness", "anger", "unethical business", "not paying taxes",
              "Hack-the-Bubble","STACS", "moistness", "tax evasion", "burglary", "identity theft", "loss", "gaming",
              "Eldritch horror", "piracy", "Fife", "2020", "midnight", "the full moon", "a minor car accident",
              "broken mirrors", "space", "the void", "nothingness", "apathy", "unaffordable accommodation", "nihilism",
              "broken hearts", "loneliness", "not having a wife"]


def get_term():
    return (
        random.choice(adjectives) + " " +
        random.choice(nouns) + " of " +
        random.choice(descriptor)
    )
