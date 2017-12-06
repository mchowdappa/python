class Init:

    def __init__(self):
        print("In Init!!")
    def function(self):
        print("In function")


init = Init()
init.function()

class Enimy:
    life = 0
    def __init__(self, life):
        self.life = life
        print("In init")

    def attack(self):
        self.life -=1

    def get_life(self):
        print(str(self.life) + " Life left")

enimy1 = Enimy(10)
enimy1.attack()
enimy1.get_life()


enimy1 = Enimy(5)
enimy1.attack()
enimy1.get_life()

