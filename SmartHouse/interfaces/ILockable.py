from abc import ABC, abstractmethod

class ILockable(ABC):

    @abstractmethod
    def lock(self):
        """
        When implemented, this method should lock the device.
        """
        pass

    @abstractmethod
    def unlock(self):
        """
        When implemented, this method should unlock the device.
        """
        pass

    @abstractmethod
    def is_locked(self) -> bool:
        """
        When implemented, this method should return whether the device is currently locked.
        
        :return: True if the device is locked, False otherwise.
        """
        pass