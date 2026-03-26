from SmartHouse.interfaces.ISwitchable import ISwitchable
from SmartHouse.devices.device import Device

class Light(Device, ISwitchable):
    def __init__(self, id, device_location, name, device_model):
        super().__init__(id, device_location, name, "Light", device_model)
        self._is_on = False

    def switch_on(self):
        """Switches the light on."""
        self.device_info()
        self._is_on = True
        print(f"{self.name} light ON")


    def switch_off(self):
        """Switches the light off."""
        self.device_info()
        self._is_on = False
        print(f"{self.name} light OFF")


    def is_on(self):
        """Returns whether the light is currently on."""
        self.device_info()
        print(f"{self.name} light is {'ON' if self._is_on else 'OFF'}")
        return self._is_on