import random

adjectives = ["frightening", "scary", "spooky", "shivering", "eerie", "sinister", "hairy",
              "stumbling", "crying", "ghastly", "bloody", "vile", "howling", "ancient",
              "ominous", "dark", "filthy", "abandoned", "looming", "silent", "decaying"]
nouns = ["pumpkin", "monster", "skeleton", "witch", "brew", "zombie", "ghoul",
         "ghost", "hag", "beast", "werewolf", "eye", "cobweb", "spider", "snake"]
descriptor = ["blood", "slime", "terror", "fright", "evil", "fear", "death"]


def get_term():
    return (
        random.choice(adjectives) + " " +
        random.choice(nouns) + " of " +
        random.choice(descriptor)
    )
