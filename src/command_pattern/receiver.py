from typing import Final


class Light:
    def __init__(self, name: str = "") -> None:
        self.name = name

    def on(self) -> None:
        print(f"{self.name} Light On")

    def off(self) -> None:
        print(f"{self.name} Light Off")


class GarageDoor:
    def __init__(self, name: str = "") -> None:
        self.name = name

    def up(self):
        print(f"{self.name} GarageDoor Up")

    def down(self):
        print(f"{self.name} GarageDoor Down")

    def stop(self):
        print(f"{self.name} GarageDoor Stop")

    def light_on(self):
        print(f"{self.name} GarageDoor Light On")

    def light_off(self):
        print(f"{self.name} GarageDoor Light Off")


class CeilingFan:
    HIGH: Final[int] = 3
    MEDIUM: Final[int] = 2
    LOW: Final[int] = 1
    OFF: Final[int] = 0
    location: str
    speed: int

    def __init__(self, location: str = "") -> None:
        self.location = location
        self.speed = self.OFF

    def on(self) -> None:
        self.speed = self.MEDIUM
        print(f"{self.location} CeilingFan On")

    def off(self) -> None:
        self.speed = self.OFF
        print(f"{self.location} CeilingFan Off")

    def high(self):
        self.speed = self.HIGH
        print(f"{self.location} CeilingFan High")

    def medium(self):
        self.speed = self.MEDIUM
        print(f"{self.location} CeilingFan Medium")

    def low(self):
        self.speed = self.LOW
        print(f"{self.location} CeilingFan Low")


class Stereo:
    def __init__(self, name: str = "") -> None:
        self.name = name

    def on(self) -> None:
        print(f"{self.name} Stereo On")

    def set_cd(self) -> None:
        print(f"{self.name} Stereo Set CD")

    def set_volume(self, volume: int) -> None:
        print(f"{self.name} Stereo Set Volume {volume}")

    def off(self) -> None:
        print(f"{self.name} Stereo Off")
