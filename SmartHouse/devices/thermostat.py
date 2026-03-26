from SmartHouse.interfaces.ITemperatureControl import ITemperatureControl

class Thermostat(ITemperatureControl):
    
    def __init__(self):
        self._current_temperature = 20.0  # Default temperature in Celsius
        self._desired_temperature = 20.0

    def set_temperature(self, temperature: float):
        """Sets the desired temperature."""
        self._desired_temperature = temperature
        print(f"Desired temperature set to {temperature}°C")

    def get_current_temperature(self):
        """Returns the current temperature."""
        return self._current_temperature

    def update_current_temperature(self, new_temperature: float):
        """Updates the current temperature (simulating a sensor reading)."""
        self._current_temperature = new_temperature
        print(f"Current temperature updated to {new_temperature}°C")