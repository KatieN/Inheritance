class Vehicle:
    def __init__(self, name, speed, size):
        self.name = name
        self.speed = speed
        self.size = size
    
    def switchOn(self):
        print(self.name + " has switched on.")
    