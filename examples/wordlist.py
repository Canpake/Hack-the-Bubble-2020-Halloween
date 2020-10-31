import random

adjectives = ["frightening", "scary", "spooky", "shivering", "eerie", "sinister", "hairy",
              "stumbling", "crying", "ghastly", "bloody", "vile", "howling", "ancient",
              "ominous", "dark", "filthy", "abandoned", "looming", "silent", "decaying",
              "forsaken", "crusty", "weeping", "wailing", "dying", "musky", "dirty", "horrid", "condemned", "rotting",
              "hairless", "spoopy", "dripping", "crawling", "thirsty", "munching", "hungry", "wicked", "haunting",
              "banished"]
nouns = ["pumpkin", "monster", "skeleton", "witch", "brew", "zombie", "ghoul",
         "ghost", "hag", "beast", "werewolf", "eye", "cobweb", "spider", "snake", "spider", "flesh", "vampire", "smoke",
         "fire", "demon", "cyborg", "robot", "worm", "centipede", "nest", "grave", "tomb", "coffin", "meat", "feet",
         "corncob","skull", "bone", "teeth", "toes", "claws", "horde", "potion", "elixir", "cauldron", "socks", "corpse",
         "spine", "limb", "bones", "trees"]
descriptor = ["blood", "slime", "terror", "fright", "evil", "fear", "death", "coursework",
              "failing my degree", "depression", "sadness", "rot", "bodily fluids", "bile", "drool", "mourning", "hell",
              "doom", "misery", "tears", "deadlines", "assignments", "wetness", "the presidential election", "St. Andrews",
              "Andrew Melville Hall", "mud", "darkness", "madness", "anger", "unethical business", "not paying taxes",
              "Hack-the-Bubble","STACS"]


def get_term():
    return (
        random.choice(adjectives) + " " +
        random.choice(nouns) + " of " +
        random.choice(descriptor)
    )
