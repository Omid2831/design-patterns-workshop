from abc import ABC, abstractmethod

class ICamera(ABC):

    @abstractmethod
    def take_photo(self):
        """
        When implemented, this method should take a photo.
        """
        pass

    @abstractmethod
    def record_video(self):
        """
        When implemented, this method should record a video.
        """
        pass