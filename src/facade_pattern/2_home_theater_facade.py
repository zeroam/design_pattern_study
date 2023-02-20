from lib import AutoScreen, PopcornMachine, Projector, StreamPlayer, SurroundSound


class HomeTheaterFacade:
    def __init__(
        self,
        stream_player: StreamPlayer,
        projector: Projector,
        auto_screen: AutoScreen,
        surround_sound: SurroundSound,
        popcorn_machine: PopcornMachine,
    ):
        self.stream_player = stream_player
        self.projector = projector
        self.auto_screen = auto_screen
        self.surround_sound = surround_sound
        self.popcorn_machine = popcorn_machine

    def watch_movie(self, name: str):
        print("--------- Watch Movie ---------")
        self.stream_player.play(name)
        self.projector.on()
        self.projector.wide_screen_mode()
        self.auto_screen.down()
        self.surround_sound.on()
        self.surround_sound.set_volume(5)
        self.popcorn_machine.on()
        self.popcorn_machine.pop()
        print("-------------------------------")

    def end_movie(self):
        print("--------- End Movie ---------")
        self.popcorn_machine.off()
        self.surround_sound.off()
        self.auto_screen.up()
        self.projector.off()
        self.stream_player.stop()
        print("-----------------------------")


if __name__ == "__main__":
    theater = HomeTheaterFacade(
        StreamPlayer(),
        Projector(),
        AutoScreen(),
        SurroundSound(),
        PopcornMachine(),
    )

    print("Go to theater")
    theater.watch_movie("Inception")
    theater.end_movie()
