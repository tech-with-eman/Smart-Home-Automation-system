class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.is_on = False 

    def turn_on(self):
        self.is_on = True   
        print(f"{self.name} is now turned ON.")

    def turn_off(self):
        self.is_on = False 
        print(f"{self.name} is now turned OFF.")

class Light(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 100
    def adjust_brightness(self, level):
        self.brightness = level
        print(f"{self.name} adjusted to {self.brightness}")
        return self.brightness

class Thermostat(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 25

    def adjust_temperature(self, degree):
        self.temperature = degree
        print(f"{self.name} adjusted to {self.temperature}")

class SmartHome:
    def __init__(self, house_name):
        self.house_name = house_name
        self.devices = []  # An empty list to store all our smart devices

    def add_device(self, device):
        """Adds any device (Light or Thermostat) to our home inventory"""
        self.devices.append(device)
        print(f"Added {device.name} to {self.house_name}.")

    def turn_all_on(self):
        """Loops through every device in the house and turns it on"""
        print(f"\n--- Turning on all devices in {self.house_name} ---")
        for device in self.devices:
            device.turn_on()

    def turn_all_off(self):
        """Loops through every device in the house and turns it off"""
        print(f"\n--- Turning off all devices in {self.house_name} ---")
        for device in self.devices:
            device.turn_off()

    
