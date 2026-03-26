from abc import ABC, abstractmethod

class ITemperatureControl(ABC):

    @abstractmethod
    def set_temperature(self, temperature: float):
        """
        When implemented, this method should set the desired temperature.
        
        :param temperature: The target temperature to be set.
        """
        pass

    @abstractmethod
    def get_current_temperature(self):
        """
        When implemented, this method should return the current temperature.
        
        :return: The current temperature.
        """
        pass