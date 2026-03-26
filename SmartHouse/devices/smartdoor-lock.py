from SmartHouse.interfaces.ILockable import ILockable

class SmartDoorLock(ILockable):

    def __init__ (self, name):
        self.name = name
        self.is_locked = False

    def lock(self):
        self.is_locked = True
        print(f"{self.name} is now LOCKED.")

    def unlock(self):
        self.is_locked = False
        print(f"{self.name} is now UNLOCKED.")
        
    def is_locked(self) -> bool:
        return self.is_locked
        