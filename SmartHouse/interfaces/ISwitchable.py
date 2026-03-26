from abc import ABC, abstractmethod

class ISwitchable(ABC):
    
    @abstractmethod
    def switch_on(self):
        """
        When implemented, this method should switch on the device.
        """
        pass

    @abstractmethod
    def switch_off(self):
        """
        When implemented, this method should switch off the device.
        """
        pass
    