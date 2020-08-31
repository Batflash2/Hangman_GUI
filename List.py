import random


def pick():
    movies = [
        'aquaman', 'hungama', 'joker', 'gemini man', 'hera pheri', 'sonic',
        'shazam', 'justice league', 'wonder woman', 'hindi medium',
        'spies in disguise', 'free guy', 'the god father', 'the wizard of oz',
        'the shawshank redemption', 'pulp fiction', 'forest gump', 'et',
        'a space odyssey', 'schindlers list', 'star wars', 'back to the future',
        'hunger games', 'jaws', 'the sound of music', 'maze runner',
        'ready player one', 'the matrix', 'toy story', 'titanic', 'jurassic park',
        'the dark knight', 'iron man', 'taxi driver', 'babys day out',
        'ghost busters', 'avatar', 'the lion king', 'gladiator', 'frankenstein'
    ]
    return random.choice(movies)
