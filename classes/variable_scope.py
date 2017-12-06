class Girl:

    gender = "female" # class variable
    def __init__(self, name):
        self.name = name    # instance variable

r = Girl("Raji")
s =Girl("Souji")

print(r.gender)
print(s.gender)

print(r.name)
print(s.name)
