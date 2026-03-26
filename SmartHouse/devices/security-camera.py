from SmartHouse.interfaces.ICamera import ICamera
from SmartHouse.interfaces.ISwitchable import ISwitchable

class SecurityCamera(ICamera, ISwitchable):

    def __init__(self, name):
        self.name = name
        self.is_on = False

    def switch_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")

    def switch_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")

    def take_photo(self):
        if self.is_on:
            print(f"{self.name} took a photo.")
        else:
            print(f"{self.name} is OFF.")

    def record_video(self):
        if self.is_on:
            print(f"{self.name} is recording video.")
        else:
            print(f"{self.name} is OFF.")