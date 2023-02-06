from command_with_undo import (
    CeilingFanHighCommand,
    CeilingFanMediumCommand,
    CeilingFanOffCommand,
)
from invoker import RemoteControlWithUndo
from receiver import CeilingFan


def main():
    remote_control = RemoteControlWithUndo()

    ceiling_fan = CeilingFan("Living Room")

    ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    remote_control.set_command(0, ceiling_fan_medium, ceiling_fan_off)
    remote_control.set_command(1, ceiling_fan_high, ceiling_fan_off)

    remote_control.on_button_pressed(0)  # medium
    remote_control.off_button_pressed(0)  # off
    print(remote_control)
    remote_control.undo_button_pressed()  # medium

    remote_control.on_button_pressed(1)  # high
    print(remote_control)
    remote_control.undo_button_pressed()  # medium


if __name__ == "__main__":
    main()
