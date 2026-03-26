from SmartHouse.interfaces.ISwitchable import ISwitchable
from typing import List

class SmartHomeController:

    def turn_all_on(self, devices: List[ISwitchable]):
        for device in devices:
            device.switch_on()

    def turn_all_off(self, devices: List[ISwitchable]):
        for device in devices:
            device.switch_off()