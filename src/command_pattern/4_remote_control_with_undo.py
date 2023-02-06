from command_with_undo import LightOffCommand, LightOnCommand
from invoker import RemoteControlWithUndo
from receiver import Light


def main():
    remote_control = RemoteControlWithUndo()

    living_room_light = Light("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)

    print(remote_control)

    remote_control.on_button_pressed(0)
    remote_control.off_button_pressed(0)
    print(remote_control)
    remote_control.undo_button_pressed()


if __name__ == "__main__":
    main()
