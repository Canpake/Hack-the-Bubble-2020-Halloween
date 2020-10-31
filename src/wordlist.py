import random
import os.path
from enum import Enum


class WordType(Enum):
    NOUN = 1
    ADJECTIVE = 2
    DESCRIPTOR = 3


adjectives = ["frightening", "scary", "spooky", "shivering", "eerie", "sinister", "hairy",
              "stumbling", "crying", "ghastly", "bloody", "vile", "howling", "ancient",
              "ominous", "dark", "filthy", "abandoned", "looming", "silent", "decaying",
              "forsaken", "crusty", "weeping", "wailing", "dying", "musky", "dirty", "horrid", "condemned", "rotting",
              "hairless", "spoopy", "dripping", "crawling", "thirsty", "munching", "hungry", "wicked", "haunting",
              "banished", "crazed", "rabid", "threatening", "growing", "flailing", "crunchy", "gross", "invisible",
              "screaming", "shouting", "laughing", "menacing", "twisted", "banned", "illegal", "lifeless", "fatigued",
              "troubled", "agonized", "charred", "freakish", "brutish", "colourless", "pale", "melting", "spineless",
              "torn", "spiked", "wild", "stormy", "screeching", "trembling", "dusty", "awoken", "bubbling", "slithering",
              "creeping", "exploding", "whispering", "cursed", "destroyed", "demolished", "poisonous", "venomous"]
nouns = ["pumpkin", "monster", "skeleton", "witch", "brew", "zombie", "ghoul",
         "ghost", "hag", "beast", "werewolf", "eye", "cobweb", "spider", "snake", "spider", "flesh", "vampire", "smoke",
         "fire", "demon", "cyborg", "robot", "worm", "centipede", "nest", "grave", "tomb", "coffin", "meat", "feet",
         "corncob","skull", "bone", "teeth", "toes", "claws", "horde", "potion", "elixir", "cauldron", "socks", "corpse",
         "spine", "limb", "bones", "trees", "fingers", "villain", "caramel apple", "candy apple", "bug", "weapon",
         "crevice", "being", "humanoid", "gamer", "horse", "centaur", "hooves", "cryptid", "corn stalk", "corn field",
         "feast", "bigfoot", "chupacabra", "tentacle", "homicide", "mystery", "bite", "injury", "hole", "eclipse",
         "moth", "pitchfork", "cannibal", "alien", "U.F.O", "creation", "concoction", "wife", "Eldritch horror", "human",
         "stampede", "flock", "briefcase", "elbow", "bone marrow", "crow", "circus"]
descriptor = ["blood", "slime", "terror", "fright", "evil", "fear", "death", "coursework",
              "failing my degree", "depression", "sadness", "rot", "bodily fluids", "bile", "drool", "mourning", "hell",
              "doom", "misery", "tears", "deadlines", "assignments", "wetness", "the presidential election", "St. Andrews",
              "Andrew Melville Hall", "mud", "darkness", "madness", "anger", "unethical business", "not paying taxes",
              "Hack-the-Bubble","STACS", "moistness", "tax evasion", "burglary", "identity theft", "loss", "gaming",
               "piracy", "Fife", "2020", "the full moon", "a minor car accident", "existence",
              "broken mirrors", "space", "the void", "nothingness", "apathy", "unaffordable accommodation", "nihilism",
              "broken hearts", "loneliness", "not having a wife", "putting pickles in a blender", "dampness",
              "drinking pickles from a blender", "wearing unmatched socks", "the night", "computer science",
              "parallel parking", "cold big macs", "not having a girlfriend", "minecraft", "goo", "nightmares", "chaos",
              "disorder", "unsustainable farming", "disgrace"]

def get_term():
    return (
        random.choice(adjectives) + " " +
        random.choice(nouns) + " of " +
        random.choice(descriptor)
    )


def get_adjective():
    return random.choice(adjectives)


def get_noun():
    return random.choice(nouns)


def get_descriptor():
    return random.choice(descriptor)


# Checks if an image already exists
def is_drawn(image):
    imagepath = '../images/' + image + '.png'
    os.path.isfile(imagepath)


def new_words(word_type):
    if word_type == WordType.ADJECTIVE:
        array = adjectives
    elif word_type == WordType.NOUN:
        array = nouns
    elif word_type == WordType.DESCRIPTOR:
        array = descriptor

    new = []
    for obj in array:
        if not is_drawn(obj):
            new.append(obj)
    return new


def get_new_word(word_type):
    return random.choice(new_words(word_type))


if __name__ == '__main__':
    print(get_term())
    print(get_term())
    print(get_term())
