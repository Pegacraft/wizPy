import json

from wizPy import sender


class Light:
    ip: str = ""
    set_request: json = {"method": "setPilot", "params": {}}
    get_request: json = {"method": "getPilot"}

    def __init__(self, ip: str):
        self.ip = ip

    async def apply(self):
        if self.set_request is None:
            print("no set_request available")
        else:
            print(self.set_request)
            await sender.send(self.ip, self.set_request)

    @staticmethod
    def hex_to_percent(val):
        return round((val / 255) * 100)

    @staticmethod
    def clamp(val: int, min_val: int, max_val: int) -> int:
        if val > max_val:
            val = max_val
        if val < min_val:
            val = min_val
        return val

    def set(self, key: str, val):
        self.set_request["params"][key] = val

    def off(self):
        self.set("state", False)

    def on(self):
        self.set("state", True)

    def set_brightness(self, brightness: int):
        self.set("dimming", self.clamp(self.hex_to_percent(brightness), 10, 100))

    def set_rgb(self, r: int = None, g: int = None, b: int = None):
        if r is not None:
            self.set("r", self.clamp(r, 0, 255))
        if g is not None:
            self.set("g", self.clamp(r, 0, 255))
        if b is not None:
            self.set("b", self.clamp(r, 0, 255))

    def set_color_temp(self, kelvin: int):
        self.set("temp", self.clamp(kelvin, 1000, 10000))

    def set_warm_white(self, value: int):
        self.set("w", self.clamp(value, 0, 255))

    def set_cold_white(self, value: int):
        self.set("c", self.clamp(value, 0, 255))

    def set_speed(self, percent: int):
        self.set("speed", self.clamp(percent, 0, 100))

    async def get_data(self, key: str):
        try:
            return json.loads(await sender.send(self.ip, self.get_request))["result"][key]
        except KeyError:
            return None

    async def is_on(self):
        return await self.get_data("state")

    async def get_color_temp(self):
        return await self.get_data("temp")

    async def get_rgb(self):
        return await self.get_data("r"), await self.get_data("g"), await self.get_data("b")

    async def get_warm_white(self):
        return await self.get_data("w")

    async def get_cold_white(self):
        return await self.get_data("c")

    async def get_brightness(self):
        return await self.get_data("dimming")
