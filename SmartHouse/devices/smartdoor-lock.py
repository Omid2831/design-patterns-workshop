from SmartHouse.interfaces.ILockable import ILockable
from SmartHouse.devices.device import Device
class SmartDoorLock(Device, ILockable):

    def __init__ (self, id, device_location, name, device_model):
        super().__init__(id, device_location, name, "Smart Door Lock", device_model)
        self.is_locked = False

    def lock(self):
        self.is_locked = True
        self.device_info()
        print(f"{self.name} is now LOCKED.")

    def unlock(self):
        self.is_locked = False
        self.device_info()
        print(f"{self.name} is now UNLOCKED.")
        
    def is_locked(self) -> bool:
        self.device_info()
        return self.is_locked
        