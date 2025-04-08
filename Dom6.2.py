class LowBatteryDevices:
    def __init__(self, devices):
        self.devices = devices
        self.index = 0
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        while self.index < len(self.devices):
            device = self.devices[self.index]
            self.index += 1
            if device[1] < 20:
                return device
        raise StopIteration


devices = [
    ('Smartphonene', 30),
    ('Laptope', 15),
    ('Tablete', 5),
    ('Smartwatche', 50),
    ('Headphonesi', 10)
]

low_battery_devices = LowBatteryDevices(devices)

print("Устройства с нисък заряд на батерията (под 20%) here:")
for device in low_battery_devices:
    print(f"{device[0]}: {device[1]}%")
