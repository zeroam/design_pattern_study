from command_with_undo import (
    CeilingFanHighCommand,
    CeilingFanOffCommand,
    LightOffCommand,
    LightOnCommand,
    MacroCommand,
)
from invoker import RemoteControlWithUndo
from receiver import CeilingFan, Light


def main():
    remote_control = RemoteControlWithUndo()

    living_room_light = Light("Living Room")
    ceiling_fan = CeilingFan("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    party_on = [living_room_light_on, ceiling_fan_high]
    party_off = [living_room_light_off, ceiling_fan_off]

    pary_on_macro = MacroCommand(party_on)
    party_off_macro = MacroCommand(party_off)

    remote_control.set_command(0, pary_on_macro, party_off_macro)
    print(remote_control)

    remote_control.on_button_pressed(0)
    remote_control.off_button_pressed(0)


if __name__ == "__main__":
    main()
