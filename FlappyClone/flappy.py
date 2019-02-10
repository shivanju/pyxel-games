import pyxel
import player
import level

class Flappy:
    def __init__(self):
        pyxel.init(136,240, caption = "Flappy", fps = 60, scale = 3)
        pyxel.load("flappy.pyxel")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.state = "wait"
        self.player = player.Player()
        self.lvl= level.Level()

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if self.state == "wait":
            if pyxel.btn(pyxel.KEY_Z):
                self.state = "fly"
            return
        
        if pyxel.btn(pyxel.KEY_Z) and self.player.v_velo >= 0:
            self.player.v_velo = -4.5
        
        self.player.update_player()
        if (pyxel.frame_count % 8 == 0):
            self.player.wings_pos = (self.player.wings_pos + 1) % 2

        is_game_over = self.check_collision()
        if is_game_over:
            self.reset()
        self.lvl.update_level()


    def check_collision(self):
        if len(self.lvl.upper_pipes) < 1:
            return
        is_grounded = (self.player.y_pos == 240 - self.player.height)
        is_crashed = False
        if (self.lvl.upper_pipes[0][0] - self.player.width <= self.player.x_pos <= self.lvl.upper_pipes[0][2]) and not (self.lvl.upper_pipes[0][3] < self.player.y_pos < self.lvl.lower_pipes[0][1] - self.player.height):
            is_crashed = True
        return is_grounded or is_crashed

    def draw(self):
        pyxel.cls(6)
        self.draw_player()
        self.draw_lvl()

    def draw_player(self):
        pyxel.blt(self.player.x_pos, self.player.y_pos, 0, 1 if self.player.wings_pos else 17, 0, 16, 10, 0)

    def draw_lvl(self):
        for up in self.lvl.upper_pipes:
            pyxel.rect(up[0], up[1], up[2], up[3], 11)
        for lp in self.lvl.lower_pipes:
            pyxel.rect(lp[0], lp[1], lp[2], lp[3], 11)


if __name__ == "__main__":
    Flappy()