from SmartHouse.interfaces.IMusicPlayer import MusicPlayer

class SmartSpeaker(MusicPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.volume = 50

    def play_music(self, song):
        print(f"{self.name} is playing: {song}")

    def stop_music(self):
        print(f"{self.name} has stopped playing music.")

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.volume = volume
            print(f"{self.name} volume set to {self.volume}.")
        else:
            print("Volume must be between 0 and 100.")