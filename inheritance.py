class Animal:
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour
    
    def make_noise(self):
        print("Animal made a noise!")

class OrcaWhale(Animal):
    def make_noise(self):
        print("Whale noise!")
    
    def flip_seal(self):
        print("Seal is being flipped!")