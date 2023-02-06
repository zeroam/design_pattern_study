from command import (
    CeilingFanOffCommand,
    CeilingFanOnCommand,
    GarageDoorDownCommand,
    GarageDoorUpCommand,
    LightOffCommand,
    LightOnCommand,
    StereoOffCommand,
    StereoOnWithCDCommand,
)
from invoker import RemoteControl
from receiver import CeilingFan, GarageDoor, Light, Stereo


def main():
    remote_control = RemoteControl()

    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen Room")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor("Garage")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    ceiling_fan_on = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)

    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, garage_door_up, garage_door_down)
    remote_control.set_command(4, stereo_on_with_cd, stereo_off)

    print(remote_control)

    remote_control.on_button_pressed(0)
    remote_control.off_button_pressed(0)
    remote_control.on_button_pressed(1)
    remote_control.off_button_pressed(1)
    remote_control.on_button_pressed(2)
    remote_control.off_button_pressed(2)
    remote_control.on_button_pressed(3)
    remote_control.off_button_pressed(3)
    remote_control.on_button_pressed(4)
    remote_control.off_button_pressed(4)


if __name__ == "__main__":
    main()
