import pyxel
import plane
import random
import tunnel
import math
import music

class Copter:
    def __init__(self):
        pyxel.init(240, 136, caption = "Copter", fps = 60, scale = 3)
        pyxel.image(0).load(0, 0, "copter_8x16-sheet.png")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.sfx = music.Music()
        self.sfx.play_sfx()
        self.speed = 1
        self.tunnel = tunnel.Tunnel()
        self.score = 0
        self.is_paused = False
        self.plane = plane.Plane()
        self.jump_velo = -1
        self.is_game_over = False

    def update(self):
        if pyxel.btn(pyxel.constants.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.constants.KEY_P, 30, 30):
            self.is_paused = not(self.is_paused)
            if self.is_paused:
                self.sfx.play_sfx(state = "paused")
            else:
                self.sfx.play_sfx(state = "alive")
        if self.is_paused:
            return

        if self.is_game_over:
            self.sfx.play_sfx(state = "dead")
            if pyxel.btn(pyxel.constants.KEY_Q):
                pyxel.quit()
            if pyxel.btn(pyxel.constants.KEY_R):
                self.reset()
            return

        if pyxel.btnp(pyxel.constants.KEY_Z, 5, 1):
            self.plane.update(self.jump_velo)
        else:
            self.plane.update()

        self.score += math.floor(self.tunnel.speed)
        self.tunnel.speed = min(self.score / 5000 + 1, 3)
        self.tunnel.update()
        self.is_crashed()

    def is_crashed(self):
        for obstacle in self.tunnel.obstacles:
            if (self.tunnel.pillars[obstacle[0]][2] -15 <= self.plane.position[0] <= self.tunnel.pillars[obstacle[0]][2] + 7) and (obstacle[1] - 7 <= self.plane.position[1] <= obstacle[2]):
                self.is_game_over = True
                break
        self.is_game_over = self.is_game_over or self.plane.position[1] + 7 >= min(self.tunnel.pillars[8][1], self.tunnel.pillars[9][1], self.tunnel.pillars[10][1]) or self.plane.position[1] <= max(self.tunnel.pillars[8][0], self.tunnel.pillars[9][0], self.tunnel.pillars[10][0])

        return self.is_game_over

    def draw_crash_screen(self):
        pyxel.cls(0)
        pyxel.text(100, 50, "Q: quit", 8)
        pyxel.text(100, 57, "R: restart", 3)
        pyxel.text(100, 64, "SCORE: ", 9)
        pyxel.text(124, 64, str(self.score), 7)

    def draw(self):
        if self.is_paused:
            return
        if self.is_game_over:
            self.draw_crash_screen()
            return

        pyxel.cls(0)
        for pillar in self.tunnel.pillars:
            pyxel.rect(pillar[2], 0, pillar[2] + 7, pillar[0], 1)
            pyxel.rect(pillar[2], 136, pillar[2] + 7, pillar[1], 1)

        for obstacle in self.tunnel.obstacles:
            pyxel.rect(self.tunnel.pillars[obstacle[0]][2], obstacle[1], self.tunnel.pillars[obstacle[0]][2] + 7, obstacle[2], 8)

        pyxel.blt(self.plane.position[0], self.plane.position[1], 0, 0 if pyxel.frame_count % 2 else 16, 0, 16, 8, 0)
        pyxel.text(0, 4, "SCORE: ", 9)
        pyxel.text(24, 4, str(self.score), 7)

if __name__ == "__main__":
    Copter()