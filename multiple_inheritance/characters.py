class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def get_info(self):
        print(f'{self.name}: Health = {self.health}, Attack = {self.attack}')
    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} takes {damage} damage.')

class Player(Character):
    def __init__(self, name, health, attack, level):
        super().__init__(name, health, attack)
        self.level = level
    def level_up(self):
        self.level += 1
        self.attack *= 1.2
        self.health *= 1.2
        print(f'{self.name} gets level {self.level}')

class Enemy(Character):
    def __init__(self, name, health, attack, reward):
        super().__init__(name, health, attack)
        self.reward = reward
    def give_reward(self):
        print(f'This player is getting {self.reward} xp')
        return self.reward

class Boss(Player, Enemy):
    def __init__(self, name, health, attack, level, reward, weakness):
        Player.__init__(self, name, health, attack, level)
        Enemy.__init__(self, name, health, attack, reward)
        self.weakness = weakness
    def get_weakness(self):
        print(f'This boss has a weakness: {self.weakness}')