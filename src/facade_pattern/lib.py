class StreamPlayer:
    def play(self, name: str):
        print(f"Play '{name}' in Stream Player")

    def stop(self):
        print("Stop Stream Player")


class Projector:
    def on(self):
        print("On Projector")

    def wide_screen_mode(self):
        print("Wide Screen Mode Projector")

    def off(self):
        print("Off Projector")


class AutoScreen:
    def up(self):
        print("Up Auto Screen")

    def down(self):
        print("Down Auto Screen")


class SurroundSound:
    def on(self):
        print("On Surround Sound")

    def set_volume(self, volume: int):
        print(f"Set volume: {volume}, Surround Sound")

    def off(self):
        print("Off Surround Sound")


class PopcornMachine:
    def on(self):
        print("On Popcorn Machine")

    def pop(self):
        print("Pop Popcorn Machine")

    def off(self):
        print("Off Popcorn Machine")
