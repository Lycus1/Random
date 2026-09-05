import random

owCharacters = {
    'Domina': ('Tank', 'Female', 'Human','Europe','Stalwart'),
    'D.VA': ('Tank', 'Female', 'Human', 'Asia', 'Initiator'),
    'Doomfist': ('Tank', 'Male', 'Human', 'Africa', 'Initiator'),
    'Hazard': ('Tank', 'Male', 'Human', 'Europe', 'Initiator'),
    'Junker Queen': ('Tank', 'Female', 'Human', 'Oceania', 'Stalwart'),
    'Mauga': ('Tank', 'Male', 'Human', 'Oceania', 'Bruiser'),
    'Orisa': ('Tank', 'Female', 'Omnic', 'Africa', 'Bruiser'),
    'Ramattra': ('Tank', 'Male', 'Omnic', 'Asia', 'Stalwart'),
    'Reinhardt': ('Tank', 'Male', 'Human', 'Europe', 'Stalwart'),
    'Roadhog': ('Tank', 'Male', 'Human', 'Oceania', 'Bruiser'),
    'Sigma': ('Tank', 'Male', 'Human', 'Europe', 'Stalwart'),
    'Winston': ('Tank', 'Male', 'Animal', 'Horizon Lunar Colony', 'Initiator'),
    'Wrecking Ball': ('Tank', 'Male', 'Animal', 'Horizon Lunar Colony', 'Initiator'),
    'Zarya': ('Tank', 'Female', 'Human', 'Europe', 'Bruiser'),
    'D.Mon': ('Tank', 'Female', 'Human', 'Asia', 'Stalwart'),
    
    'Anran': ('DPS', 'Female', 'Human', 'Asia', 'Flanker'),
    'Emre': ('DPS', 'Male', 'Human', 'Europe', 'Specialist'),
    'Vendetta': ('DPS', 'Female', 'Human', 'Europe', 'Flanker'),
    'Ashe': ('DPS', 'Female', 'Human', 'Americas', 'Sharpshooter'),
    'Bastion': ('DPS', '?', 'Omnic', 'Europe', 'Specialist'),
    'Cassidy': ('DPS', 'Male', 'Human', 'Americas', 'Sharpshooter'),
    'Echo': ('DPS', 'Female', 'Omnic', 'Unknown', 'Recon'),
    'Freja': ('DPS', 'Female', 'Human', 'Europe', 'Recon'),
    'Genji': ('DPS', 'Male', 'Human', 'Asia', 'Flanker'),
    'Hanzo': ('DPS', 'Male', 'Human', 'Asia', 'Sharpshooter'),
    'Junkrat': ('DPS', 'Male', 'Human', 'Oceania', 'Specialist'),
    'Mei': ('DPS', 'Female', 'Human', 'Asia', 'Specialist'),
    'Pharah': ('DPS', 'Female', 'Human', 'Africa', 'Recon'),
    'Reaper': ('DPS', 'Male', 'Human', 'Americas', 'Flanker'),
    'Soujourn': ('DPS', 'Female', 'Human', 'Americas', 'Sharpshooter'),
    'Soldier: 76': ('DPS', 'Male', 'Human', 'Americas', 'Specialist'),
    'Sombra': ('DPS', 'Female', 'Human', 'Americas', 'Recon'),
    'Symmetra': ('DPS', 'Female', 'Human', 'Asia', 'Specialist'),
    'Torbjorn': ('DPS', 'Male', 'Human', 'Europe', 'Specialist'),
    'Tracer': ('DPS', 'Female', 'Human', 'Europe', 'Flanker'),
    'Venture': ('DPS', 'Female', 'Human', 'Americas', 'Flanker'),
    'Sierra': ('DPS', 'Female', 'Human', 'Americas', 'Recon'),
    'Widowmaker': ('DPS', 'Female', 'Human', 'Europe', 'Sharpshooter'),
    'Shion': ('DPS', 'Female', 'Omnic', 'Asia', 'Flanker'),

    'Jetpack Cat': ('Support', 'Female', 'Animal', 'Europe', 'Tactician'),
    'Ana': ('Support', 'Female', 'Human', 'Africa', 'Tactician'),
    'Mizuki': ('Support', 'Male', 'Human', 'Asia', 'Survivor'),
    'Baptiste': ('Support', 'Male', 'Human', 'Americas', 'Tactician'),
    'Brigette': ('Support', 'Female', 'Human', 'Europe', 'Survivor'),
    'Illari': ('Support', 'Female', 'Human', 'Americas', 'Survivor'),
    'Juno': ('Support', 'Female', 'Human', 'Mars', 'Survivor'),
    'Kiriko': ('Support', 'Female', 'Human', 'Asia', 'Medic'),
    'Lifeweaver': ('Support', 'Male', 'Human', 'Asia', 'Medic'),
    'Lucio': ('Support', 'Male', 'Human', 'Americas', 'Tactician'),
    'Mercy': ('Support', 'Female', 'Human', 'Europe', 'Medic'),
    'Moira': ('Support', 'Female', 'Human', 'Europe', 'Medic'),
    'Wuyang': ('Support', 'Male', 'Human', 'Asia', 'Survivor'),
    'Zenyatta': ('Support', 'Male', 'Omnic', 'Asia', 'Tactician')
}

def main():
    total_guess = 1
    print("Welcome to the Overwatch Guessing Game!")
    print("Guess the hero based on the data given.")
    print('Good luck!')

    randomHero = random.choice(list(owCharacters.keys()))

    
    guess = input('Enter your first guess: ')
    while guess not in owCharacters:
        print("That's not a valid hero. Try again.")
        guess = input('Enter your first guess: ')

    while guess != randomHero:
        for i in range(5):
            if owCharacters[guess][i] == owCharacters[randomHero][i]:
                print(f'Hero is {owCharacters[guess][i]}')
            else:
                print(f'Hero is not {owCharacters[guess][i]}')
        total_guess += 1
        guess = input('Enter your next guess: ')
        while guess not in owCharacters:
            print("That's not a valid hero. Try again.")
            guess = input('Enter your next guess: ')

    print('You guessed correctly! The hero was', randomHero)
    print('total guesses:', total_guess)

if __name__ == "__main__":
    main()
