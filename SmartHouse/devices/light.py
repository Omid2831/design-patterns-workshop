from SmartHouse.interfaces.ISwitchable import ISwitchable


class Light(ISwitchable):
    def __init__(self):
        self._is_on = False

    def switch_on(self):
        """Switches the light on."""
        self._is_on = True


    def switch_off(self):
        """Switches the light off."""
        self._is_on = False


    def is_on(self):
        """Returns whether the light is currently on."""
        return self._is_on