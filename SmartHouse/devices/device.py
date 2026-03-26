class Device:
    def device_info(self):
        print(f"[Device Info] id={self.id}, location={self.device_location}, name={self.name}, type={self.device_type}, model={self.device_model}")

    def __init__(self, id, device_location, name, device_type, device_model):
        self.id = id
        self.device_location = device_location
        self.name = name
        self.device_type = device_type
        self.device_model = device_model

    def __str__(self):
        return f"""Device(
                id={self.id},
                location={self.device_location},
                name={self.name}, type={self.device_type},
                model={self.device_model}
        )"""