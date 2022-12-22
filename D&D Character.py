from random import randint

class Character:
    def __init__(self):
        abilities = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        for ability in abilities:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return sum(sorted(randint(1,6) for _ in range(4))[1:])
    
def modifier(num):
    return (num - 10) // 2
