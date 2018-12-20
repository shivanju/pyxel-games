import pyxel
import math
import player
import utils

class App:
    def __init__(self):
        pyxel.init(240, 136, caption="WhatAmI", fps = 60, scale = 4)
        pyxel.load("whatami.pyxel")
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        level_file = open("level.txt", 'r')
        self.level = [[int(x) for x in line.split()] for line in level_file]
        self.player = player.Player()
        self.player_animation = 0
        self.player_move_count = 0

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.constants.KEY_Z) and self.is_player_grounded():
            self.player.v_velo = -3.2
            self.player.state = 'jump'
        if pyxel.btn(pyxel.constants.KEY_LEFT):
            self.player.h_velo = -1
            self.player.state = 'move'
            self.player.facing = 'left'
            self.player_move_count = (self.player_move_count + 1) % 6
        if pyxel.btn(pyxel.constants.KEY_RIGHT):
            self.player.h_velo = 1
            self.player.state = 'move'
            self.player.facing = 'right'
            self.player_move_count = (self.player_move_count + 1) % 6


        self.update_player()

    def update_player(self):
        if self.player.state == 'rest':
            self.player_animation = 0
            return
        
        if self.player_move_count == 0 and self.player.state == 'move':
            self.player_animation = (self.player_animation + 1) % 4

        self.player.x_pos = self.player.x_pos + self.player.h_velo
        self.resolve_h_collision()
        self.player.y_pos = self.player.y_pos + self.player.v_velo
        v_collision_happened = self.resolve_v_collision()
        
        #set vertical velocity to zero if any vertical collision occurs
        if v_collision_happened:
            self.player.v_velo = 0
        self.player.h_velo = 0

        if not self.is_player_grounded():
            self.player.v_velo += self.player.v_accl
        
        if self.player.v_velo == 0 and self.is_player_grounded():
            self.player.state = 'rest'

    def draw(self):
        pyxel.cls(13)
        self.draw_level()
        self.draw_player()

    def draw_player(self):
        floor = lambda x: math.floor(x) 
        pyxel.blt(floor(self.player.x_pos), floor(self.player.y_pos), 0, 8 + self.player_animation * 8, 0, 6 if self.player.facing == 'right' else -6, 8, 7)

    def draw_level(self):
        for row in range(17):
            for column in range(30):
                if self.level[row][column] == 1:
                    x_loc = column * 8
                    y_loc = row * 8
                    pyxel.rect(x_loc, y_loc, x_loc + 7, y_loc + 7, 6)

    def resolve_h_collision(self):
        player_corners = self.player.get_player_corners()
        if self.player.h_velo < 0 and (self.level_value_at_tile(player_corners['TL']) or self.level_value_at_tile(player_corners['BL'])):
            self.player.x_pos = (player_corners['TL'][1] * 8) + 8
            return True
        elif self.player.h_velo > 0 and (self.level_value_at_tile(player_corners['TR']) or self.level_value_at_tile(player_corners['BR'])):
            self.player.x_pos = (player_corners['TR'][1] * 8) - self.player.width
            return True
        return False

    def resolve_v_collision(self):
        player_corners = self.player.get_player_corners()
        if self.player.v_velo < 0 and (self.level_value_at_tile(player_corners['TL']) or self.level_value_at_tile(player_corners['TR'])):
            self.player.y_pos = (player_corners['TL'][0] * 8) + 8
            return True
        elif self.player.v_velo > 0 and (self.level_value_at_tile(player_corners['BL']) or self.level_value_at_tile(player_corners['BR'])):
            self.player.y_pos = (player_corners['BL'][0] * 8) - 8
            return True
        return False

    def is_player_grounded(self):
        x = self.player.x_pos
        y = self.player.y_pos + self.player.height - 1
        return self.level_value_at_tile(utils.get_tile_from_pos(x, y + 1)) or self.level_value_at_tile(utils.get_tile_from_pos(x + self.player.width - 1, y + 1))

    def level_value_at_tile(self, tile):
        return self.level[tile[0]][tile[1]]


if __name__ == '__main__':
    App()