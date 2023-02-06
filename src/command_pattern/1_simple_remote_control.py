from command import GarageDoorUpCommand, LightOnCommand
from invoker import SimpleRemoteControl
from receiver import GarageDoor, Light


def main():
    remote = SimpleRemoteControl()
    light = Light()
    garage_door = GarageDoor()
    light_on_command = LightOnCommand(light)
    garage_door_command = GarageDoorUpCommand(garage_door)

    remote.set_command(light_on_command)
    remote.button_was_pressed()

    remote.set_command(garage_door_command)
    remote.button_was_pressed()


if __name__ == "__main__":
    main()
