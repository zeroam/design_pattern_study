from typing import Protocol

from receiver import CeilingFan, GarageDoor, Light, Stereo


class Command(Protocol):
    def execute(self) -> None:
        ...


class NoCommand(Command):
    def execute(self) -> None:
        print("None")


class LightOnCommand(Command):
    light: Light

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()


class LightOffCommand(Command):
    light: Light

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.off()


class GarageDoorUpCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.up()


class GarageDoorDownCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.down()


class CeilingFanOnCommand(Command):
    ceiling_fan: CeilingFan

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.ceiling_fan.on()


class CeilingFanOffCommand(Command):
    ceiling_fan: CeilingFan

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.ceiling_fan.off()


class StereoOnWithCDCommand(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)


class StereoOffCommand(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo) -> None:
        self.stereo = stereo

    def execute(self) -> None:
        self.stereo.off()
