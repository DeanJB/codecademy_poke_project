class Pokemon:
    def __init__(self, name, level, poke_type):
        self.name = name
        self.level = level
        self.poke_type = poke_type
        self.health = level * 10
        self.max_health = level * 10
        self.is_knocked_out = False

    def __repr__(self):
        return "{pokemon}, is a level {level}, {type} type, with {health} health points remaining.".format(pokemon = self.name, level = self.level, type = self.poke_type, health = self.health)
    
    def lose_health(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.is_knocked_out
            print("{pokemon} has fainted".format(pokemon = self.name))
        else:
            print("{pokemon} took {damage} points of damage. {pokemon} now has {health} health.".format(pokemon = self.name, damage = str(damage), health = self.health))
    
    def gain_health(self, gain):
        if self.health == 0:
            print("Cannot heal, {pokemon} is fainted".format(pokemon = self.name))
        else:
            self.health += gain
            print("{pokemon} gained {gain} points of health. {pokemon} now has {health} health.").format(pokemon = self.name, gain = gain, health = self.health)

    def revive(self, gain):
        if self.health > 0:
            print("No need to use revive, {pokemon} is awake.".format(pokemon = self.name))
        elif gain == "revive potion":
            self.health += self.level
            print("{pokemon} is revived!".format(pokemon = self.name))
        else:
            print("Wrong potion, cannot revive {pokemon}.".format(pokemon = self.name))
    def use_potion(self, potion):
        if potion == "healing potion":
            self.gain_health(20)
        elif potion == "super potion":
            self.gain_health(50)
        elif potion == "revive potion":
            self.revive(potion)
    def attack(self, enemy):
        if self.poke_type == enemy.poke_type:
            print("{pokemon} attacks and deals {damage} to {enemy}.".format(pokemon = self.name, damage = self.level, enemy = enemy.name))
            enemy.lose_health(self.level)
        elif self.poke_type == "Fire" and enemy.poke_type == "Grass":
            print("{pokemon} attacks and deals {damage} to {enemy}. It's SUPER EFFECTIVE!".format(pokemon = self.name, damage = (self.level *2), enemy = enemy.name))
            enemy.lose_health(self.level * 2)
        elif self.poke_type == "Water" and enemy.poke_type == "Fire":
            print("{pokemon} attacks and deals {damage} to {enemy}. It's SUPER EFFECTIVE!".format(pokemon = self.name, damage = (self.level *2), enemy = enemy.name))
            enemy.lose_health(self.level * 2)   
        elif self.poke_type == "Grass" and enemy.poke_type == "Water":
            print("{pokemon} attacks and deals {damage} to {enemy}. It's SUPER EFFECTIVE!".format(pokemon = self.name, damage = (self.level *2), enemy = enemy.name))
            enemy.lose_health(self.level * 2)
        elif self.poke_type == "Fire" and enemy.poke_type == "Water":
            print("{pokemon} attacks and deals {damage} to {enemy}. It's not very effective.".format(pokemon = self.name, damage = (self.level /2), enemy = enemy.name))
            enemy.lose_health(self.level / 2)
        elif self.poke_type == "Water" and enemy.poke_type == "Grass":
            print("{pokemon} attacks and deals {damage} to {enemy}. It's not very effective.".format(pokemon = self.name, damage = (self.level /2), enemy = enemy.name))
            enemy.lose_health(self.level / 2)
        elif self.poke_type == "Grass" and enemy.poke_type == "Fire":
            print("{pokemon} attacks and deals {damage} to {enemy}. It's not very effective".format(pokemon = self.name, damage = (self.level /2), enemy = enemy.name))
            enemy.lose_health(self.level / 2)
        else:
            print("{pokemon} attacks and deals {damage} to {enemy}.".format(pokemon = self.name, damage = self.level, enemy = enemy.name))
            enemy.lose_health(self.level)
            


pikachu = Pokemon("Pikachu", 34, "Electric")
charmander = Pokemon("Charmander", 25, "Fire")
bulbasaur = Pokemon("Bulbasaur", 26, "Grass")
squirtle = Pokemon("Squirtle", 24, "Water")


pikachu.lose_health(20)
pikachu.lose_health(35)
print(pikachu)
pikachu.use_potion("revive potion")
print(pikachu)
pikachu.attack(charmander)
charmander.attack(squirtle)