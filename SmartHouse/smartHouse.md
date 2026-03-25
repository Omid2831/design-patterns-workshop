# Assignment: Refactor a Smart Home System (ISP + OOP)

## Goal

Design a **Smart Home system** using:

* **Interface Segregation Principle (ISP)**
* Clean OOP structure
* Avoid “fat” interfaces

---

## Scenario

You are building a system for smart devices in a house.

There are different devices:

* Light
* Thermostat
* Smart Speaker
* Security Camera
* Smart Door Lock

---

## YOUR TASK

### 1. Apply ISP (VERY IMPORTANT)

Break `ISmartDevice` into smaller interfaces like:

* `ISwitchable` → turnOn / turnOff
* `ITemperatureControl` → setTemperature
* `IMusicPlayer` → playMusic
* `ICamera` → recordVideo
* `ILockable` → lock/unlock

---

### 2. Create Classes

Implement these properly:

| Class          | Should Implement                 |
| -------------- | -------------------------------- |
| Light          | ISwitchable                      |
| Thermostat     | ISwitchable, ITemperatureControl |
| SmartSpeaker   | ISwitchable, IMusicPlayer        |
| SecurityCamera | ISwitchable, ICamera             |
| SmartDoorLock  | ILockable                        |

### 5. Bonus

Add:

#### A Controller class

```java
public class SmartHomeController {
    public void turnAllOn(List<ISwitchable> devices)
}
```

#### Or dynamic behavior:

* Loop through devices
* Only call methods they support (polymorphism!)
