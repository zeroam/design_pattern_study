from typing import Protocol

from receiver import CeilingFan, GarageDoor, Light


class Command(Protocol):
    def execute(self) -> None:
        ...

    def undo(self) -> None:
        ...


class NoCommand(Command):
    def execute(self) -> None:
        print("None")

    def undo(self) -> None:
        print("None")


class LightOnCommand(Command):
    light: Light

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightOffCommand(Command):
    light: Light

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.off()

    def undo(self) -> None:
        self.light.on()


class GarageDoorUpCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.up()

    def undo(self) -> None:
        self.garage_door.down()


class GarageDoorDownCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor) -> None:
        self.garage_door = garage_door

    def execute(self) -> None:
        self.garage_door.down()

    def undo(self) -> None:
        self.garage_door.up()


class CeilingFanHighCommand(Command):
    ceiling_fan: CeilingFan
    prev_speed: int

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.high()

    def undo(self) -> None:
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class CeilingFanMediumCommand(Command):
    ceiling_fan: CeilingFan
    prev_speed: int

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.medium()

    def undo(self) -> None:
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class CeilingFanOffCommand(Command):
    ceiling_fan: CeilingFan
    prev_speed: int

    def __init__(self, ceiling_fan: CeilingFan) -> None:
        self.ceiling_fan = ceiling_fan

    def execute(self) -> None:
        self.prev_speed = self.ceiling_fan.speed
        self.ceiling_fan.off()

    def undo(self) -> None:
        # temp = self.ceiling_fan.speed
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()

        # self.prev_speed = temp


class MacroCommand(Command):
    commands: list[Command]

    def __init__(self, commands: list[Command]) -> None:
        self.commands = commands

    def execute(self) -> None:
        for command in self.commands:
            command.execute()

    def undo(self) -> None:
        for command in self.commands:
            command.undo()
