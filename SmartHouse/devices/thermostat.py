from SmartHouse.interfaces.ITemperatureControl import ITemperatureControl
from SmartHouse.interfaces.ISwitchable import ISwitchable
from SmartHouse.devices.device import Device
class Thermostat(Device, ITemperatureControl, ISwitchable):

    def __init__(self, id, device_location, name, device_model):
        super().__init__(id, device_location, name, "Thermostat", device_model)
        self._current_temperature = 20.0  # Default temperature in Celsius
        self._desired_temperature = 20.0
        self.is_on = False

    def switch_on(self):
        self.is_on = True
        self.device_info()
        print(f"{self.name} is now ON.")

    def switch_off(self):
        self.is_on = False
        self.device_info()
        print(f"{self.name} is now OFF.")

    def set_temperature(self, temperature: float):
        """Sets the desired temperature."""
        self._desired_temperature = temperature
        self.device_info()
        print(f"Desired temperature set to {temperature}°C")

    def get_current_temperature(self):
        """Returns the current temperature."""
        self.device_info()
        return self._current_temperature

    def update_current_temperature(self, new_temperature: float):
        """Updates the current temperature (simulating a sensor reading)."""
        self._current_temperature = new_temperature
        self.device_info()
        print(f"Current temperature updated to {new_temperature}°C")