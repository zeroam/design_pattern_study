from invoker import RemoteControlWithLambda
from receiver import CeilingFan, GarageDoor, Light


def main():
    remote_control = RemoteControlWithLambda()

    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen Light")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor("Garage")

    remote_control.set_command(0, lambda: living_room_light.on(), lambda: living_room_light.off())
    remote_control.set_command(1, lambda: kitchen_light.on(), lambda: kitchen_light.off())
    remote_control.set_command(2, lambda: ceiling_fan.on(), lambda: ceiling_fan.off())
    remote_control.set_command(3, lambda: garage_door.up(), lambda: garage_door.down())

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
