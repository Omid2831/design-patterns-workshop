from SmartHouse.interfaces.ICamera import ICamera
from SmartHouse.interfaces.ISwitchable import ISwitchable
from SmartHouse.devices.device import Device

class SecurityCamera(Device, ICamera, ISwitchable):

    def __init__(self, id, device_location, name, device_model):
        super().__init__(id, device_location, name, "Security Camera", device_model)
        self.is_on = False

    def switch_on(self):
        self.is_on = True
        self.device_info()
        print(f"{self.name} is now ON.")

    def switch_off(self):
        self.is_on = False
        self.device_info()
        print(f"{self.name} is now OFF.")

    def take_photo(self):
        if self.is_on:
            self.device_info()
            print(f"{self.name} took a photo.")
        else:
            print(f"{self.name} is OFF.")

    def record_video(self):
        if self.is_on:
            self.device_info()
            print(f"{self.name} is recording video.")
        else:
            print(f"{self.name} is OFF.")