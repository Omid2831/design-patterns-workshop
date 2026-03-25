from abc import ABC, abstractmethod

class IMusicPlayer(ABC):

    @abstractmethod
    def play(self):
        """
        When implemented, this method should start playing the music.
        """
        pass

    @abstractmethod
    def pause(self):
        """
        When implemented, this method should pause the music.
        """
        pass

    @abstractmethod
    def stop(self):
        """
        When implemented, this method should stop the music.
        """
        pass