


class Enimy:
    life=3
    def attact(self):
        print("outch!")
        self.life-=1

    def checkLife(self):
        if(self.life<=0):
            print("I am dead")
        else:
            print(str(self.life)+" life left")

enimy1 = Enimy()
enimy1.attact();enimy1.attact();
enimy1.checkLife()

enimy2 = Enimy()
enimy2.attact();
enimy2.checkLife()
