from collections.abc import Callable

from command import Command, NoCommand
from command_with_undo import Command as CommandWithUndo
from command_with_undo import NoCommand as NoCommandWithUndo


class SimpleRemoteControl:
    slot: Command

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()


class RemoteControl:
    on_commands: list[Command]
    off_commands: list[Command]

    def __init__(self) -> None:
        self.on_commands = []
        self.off_commands = []

        no_command = NoCommand()
        for _ in range(7):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)

    def set_command(self, slot: int, on_command: Command, off_command: Command) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pressed(self, slot: int) -> None:
        self.on_commands[slot].execute()

    def off_button_pressed(self, slot: int) -> None:
        self.off_commands[slot].execute()

    def __str__(self) -> str:
        lines = []
        lines.append("------ RemoteControl ------")
        for i in range(len(self.on_commands)):
            on_command_name = self.on_commands[i].__class__.__name__
            off_command_name = self.off_commands[i].__class__.__name__
            lines.append(f"[slot {i}] {on_command_name:<20}\t{off_command_name}")

        return "\n".join(lines)


class RemoteControlWithLambda:
    on_commands: list[Callable]
    off_commands: list[Callable]

    def __init__(self) -> None:
        self.on_commands = []
        self.off_commands = []

        for _ in range(7):
            self.on_commands.append(lambda: print("None"))
            self.off_commands.append(lambda: print("None"))

    def set_command(self, slot: int, on_command: Callable, off_command: Callable) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pressed(self, slot: int) -> None:
        self.on_commands[slot]()

    def off_button_pressed(self, slot: int) -> None:
        self.off_commands[slot]()

    def __str__(self) -> str:
        lines = []
        lines.append("------ RemoteControl ------")
        for i in range(len(self.on_commands)):
            lines.append(f"[slot {i}] {self.on_commands[i].__name__:<20}\t{self.off_commands[i].__name__}")

        return "\n".join(lines)


class RemoteControlWithUndo:
    on_commands: list[CommandWithUndo]
    off_commands: list[CommandWithUndo]
    undo_command: CommandWithUndo

    def __init__(self) -> None:
        self.on_commands = []
        self.off_commands = []

        no_command = NoCommandWithUndo()
        for _ in range(7):
            self.on_commands.append(no_command)
            self.off_commands.append(no_command)
        self.undo_command = no_command

    def set_command(self, slot: int, on_command: CommandWithUndo, off_command: CommandWithUndo) -> None:
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_pressed(self, slot: int) -> None:
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_pressed(self, slot: int) -> None:
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_pressed(self) -> None:
        self.undo_command.undo()

    def __str__(self) -> str:
        lines = []
        lines.append("------ RemoteControl ------")
        for i in range(len(self.on_commands)):
            on_command_name = self.on_commands[i].__class__.__name__
            off_command_name = self.off_commands[i].__class__.__name__
            lines.append(f"[slot {i}] {on_command_name:<20}\t{off_command_name}")
        lines.append(f"[undo] {self.undo_command.__class__.__name__}")

        return "\n".join(lines)
