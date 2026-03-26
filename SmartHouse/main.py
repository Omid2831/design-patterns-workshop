from SmartHouse.devices.light import Light
from SmartHouse.devices.thermostat import Thermostat
from SmartHouse.devices.smartdoor_lock import SmartDoorLock
from SmartHouse.devices.smartspeaker import SmartSpeaker
from SmartHouse.devices.security_camera import SecurityCamera

from SmartHouse.controller.smarthouseController import SmartHomeController

def main():
    # Create devices
    light = Light("light1", "Living Room", "Living Room Light", "Philips Hue")
    thermostat = Thermostat("thermo1", "Hall", "Hall Thermostat", "Nest")
    speaker = SmartSpeaker("speaker1", "Kitchen", "Kitchen Speaker", "Amazon Echo")
    camera = SecurityCamera("camera1", "Front Door", "Front Door Camera", "Ring")
    door_lock = SmartDoorLock("lock1", "Main Door", "Main Door Lock", "August")

    # Group switchable devices
    switchable_devices = [light, thermostat, speaker, camera]

    # Controller
    controller = SmartHomeController()

    print("\n--- Turning all devices ON ---")
    controller.turn_all_on(switchable_devices)

    print("\n--- Using devices ---")
    speaker.play("Lo-fi Beats")
    thermostat.set_temperature(22)
    camera.record_video()

    print("\n--- Door actions ---")
    door_lock.unlock()
    door_lock.lock()

    print("\n--- Turning all devices OFF ---")
    controller.turn_all_off(switchable_devices)


if __name__ == "__main__":
    main()