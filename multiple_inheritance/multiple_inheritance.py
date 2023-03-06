class Animal:
    def eat(self):
        print("Animal is eating")

class Pet(Animal):
    def play(self):
        print('Pet is playing')

class Toy:
    def move(self):
        print('Toy is moving')

class PetToy(Pet, Toy):
    def interact(self):
        self.play()
        self.move()