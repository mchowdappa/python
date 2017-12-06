class Parent():
    def last_name(self):
        print("Machupalli")

class Child(Parent):
    fn = ""
    def __init__(self, first_name):
        self.fn = first_name

    def first_name(self):
        print(str(self.fn))

    def last_name(self):
        print("My last name is:"+"Manchupalli")
chowdi = Child("chowdi")
chowdi.first_name()
chowdi.last_name()


jaasri = Child("jaasri")
jaasri.first_name()
jaasri.last_name()



class Big():

    def function1(self):
        print("In Big function")

class Small():
    def function2(self):
        print("In Small function")

class Mixer(Big,Small):
    pass

abc = Mixer()
abc.function1();
abc.function2();
