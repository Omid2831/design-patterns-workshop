from SmartHouse.interfaces.IMusicPlayer import IMusicPlayer
from SmartHouse.interfaces.ISwitchable import ISwitchable

class SmartSpeaker(IMusicPlayer, ISwitchable):

    def __init__(self, name):
        self.name = name
        self.volume = 50
        self.is_on = False

    def switch_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")
    
    def switch_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")

    def play(self, song):
        print(f"{self.name} is playing: {song}")

    def pause(self):
        print(f"{self.name} is paused")

    def stop(self):
        print(f"{self.name} has stopped playing")

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"{self.name} volume set to {self.volume}.")
        else:
            print("Volume must be between 0 and 100.")