class Device:
    def __init__(self, height, width, name):
        self.name = name
        self.height = height
        self.width = width
    
    def powerOn(self):
        print(self.name + " has powered on.")

class Computer(Device):
    def powerOn(self):
        print(self.name + " has powered on.")
    
    def openChrome(self):
        print(self.name + " has opened google chrome.")
    
    def update(self):
        print(self.name + " has been updated.")

computer1 = Computer(10, 50, "Windows")
device1 = Device(2, 5, "Phone")
device1.powerOn()
computer1.powerOn()
computer1.openChrome()
computer1.update()