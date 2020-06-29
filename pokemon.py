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
            self.is_knocked_out = True
            print("{pokemon} has fainted".format(pokemon = self.name))
        else:
            print("{pokemon} took {damage} points of damage. {pokemon} now has {health} health.".format(pokemon = self.name, damage = str(damage), health = self.health))
    
    def gain_health(self, gain):
        if self.health == 0:
            print("Cannot heal, {pokemon} is fainted".format(pokemon = self.name))
        else:
            if self.health <= self.max_health - gain:
                self.health += gain
                print("{pokemon} gained {gain} points of health. {pokemon} now has {health} health.").format(pokemon = self.name, gain = gain, health = self.health)
            else:
                print("{pokemon} gained {gain} points of health. {pokemon} is now at full health".format(pokemon = self.name, gain = self.max_health - self.health))
                self.health = self.max_health

    def revive(self, gain):
        if self.health > 0:
            print("No need to use revive, {pokemon} is awake.".format(pokemon = self.name))
        elif gain == "revive potion":
            self.health += self.level
            print("{pokemon} is revived!".format(pokemon = self.name))
            self.is_knocked_out = False
        else:
            print("Wrong potion, cannot revive {pokemon}.".format(pokemon = self.name))
    
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
caterpie = Pokemon("Caterpie", 18, "Grass")
pidgey = Pokemon("Pidgey", 15, "Normal")
ratata = Pokemon("Ratata", 17, "Normal")
geodude = Pokemon("Geodude", 22, "Ground")
vulpix = Pokemon("Vulpix", 29, "Fire")
goldeen = Pokemon("Goldeen", 26, "Water")

#poke_dex = {"pikachu": pikachu, "charmander": charmander, "squirtle": squirtle, "bulbasaur": bulbasaur, "caterpie": caterpie, "pidgey": pidgey, "ratata": ratata, "geodude": geodude, "vulpix": vulpix, "goldeen": goldeen}
#Testing out above functionality of fighting mechanisms
#pikachu.lose_health(20)
#pikachu.lose_health(35)
#print(pikachu)
#pikachu.use_potion("revive potion")
#print(pikachu)
#pikachu.attack(charmander)
#charmander.attack(squirtle)

class Trainer:
    def __init__(self, name, pokedex, inventory):
        self.name = name
        self.pokedex = pokedex
        self.inventory = inventory
        self.active = self.pokedex[0]
    
    def __repr__(self):
        return "{trainer} wants to be the best trainer in the world.".format(trainer = self.name)

    def attack_other_trainer(self, other_trainer):
        their_active = other_trainer.active
        if self.active.is_knocked_out == True:
            print("{pokemon} cannot attack. {pokemon} is knocked out".format(pokemon = self.active.name))
        else:
            self.active.attack(their_active)
    

    def change_active(self, change_to):
        if self.pokedex[change_to].is_knocked_out == True:
            print("{pokemon} cannot fight. {pokemon} is knocked out!".format(pokemon = self.pokedex[change_to].name))
        else:
            print("That's enough {active}. {change} I choose you.".format(active = self.active.name, change = self.pokedex[change_to].name))
            self.active = self.pokedex[change_to]
    
    def use_potion(self, potion):
        print("{trainer} used {potion}.".format(trainer = self.name, potion = potion))
        try:
            if self.active.health == self.active.max_health:
                print("{pokemon} is already at max health".format(pokemon = self.active.name))
                return
            for use in self.inventory:
                potion_index = self.inventory.index(potion)
                if use == potion:
                    self.inventory.pop(potion_index)                  
            if potion == "potion":
                self.active.gain_health(50)
            elif potion == "super potion":
                self.active.gain_health(100)
            elif potion == "revive potion":
                self.active.revive(potion)
        except:
            print("No {potion}'s in inventory".format(potion = potion)) 


ash = Trainer("Ash", [pikachu, charmander, squirtle], ["super potion", "potion", "revive potion"])
print(ash)

gary = Trainer("Gary", [bulbasaur, vulpix, geodude], ["potion",])

#testing of Trainer methods

ash.attack_other_trainer(gary)
gary.change_active(1)
gary.attack_other_trainer(ash)
ash.attack_other_trainer(gary)
gary.attack_other_trainer(ash)
ash.change_active(2)
ash.attack_other_trainer(gary)
ash.attack_other_trainer(gary)
ash.attack_other_trainer(gary)
ash.attack_other_trainer(gary)
ash.attack_other_trainer(gary)
ash.attack_other_trainer(gary)
gary.attack_other_trainer(ash)
#print(gary.inventory)
gary.use_potion("revive potion")
#print(gary.inventory)

ash.use_potion("potion")
print(ash.inventory)
gary.attack_other_trainer(ash)
ash.use_potion("potion")
gary.change_active(1)