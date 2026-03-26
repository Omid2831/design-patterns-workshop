from SmartHouse.interfaces.IMusicPlayer import IMusicPlayer
from SmartHouse.interfaces.ISwitchable import ISwitchable
from SmartHouse.devices.device import Device
class SmartSpeaker(Device, IMusicPlayer, ISwitchable):

    def __init__(self, id, device_location, name, device_model):
        super().__init__(id, device_location, name, "Smart Speaker", device_model)
        self.volume = 50
        self.is_on = False

    def switch_on(self):
        self.is_on = True
        self.device_info()
        print(f"{self.name} is now ON.")
    
    def switch_off(self):
        self.is_on = False
        self.device_info()
        print(f"{self.name} is now OFF.")

    def play(self, song):
        self.device_info()
        print(f"{self.name} is playing: {song}")

    def pause(self):
        self.device_info()
        print(f"{self.name} is paused")

    def stop(self):
        self.device_info()
        print(f"{self.name} has stopped playing")

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            self.device_info()
            print(f"{self.name} volume set to {self.volume}.")
        else:
            print("Volume must be between 0 and 100.")