import pyxel

class Music:
    def __init__(self):
        self.init_audio()
        self.is_playing = [0, 0, 0]

    def init_audio(self):
        pyxel.sound(0).set("c1g1c1", 'n', "5", 's', 20)
        pyxel.sound(1).set("c3e3", 'n', '7', 'f', 6)

    def play_sfx(self, state = "alive"):
        if state == "dead" and not(self.is_playing[0]):
            self.is_playing = [1, 0, 0]
            pyxel.play(0, 0, loop = False)

        elif state == "alive" and not(self.is_playing[1]):
            self.is_playing = [0, 1, 0]
            pyxel.play(0, 1, loop = True)

        elif state == "paused" and not(self.is_playing[2]):
            self.is_playing = [0, 0, 1]
            pyxel.stop(0)