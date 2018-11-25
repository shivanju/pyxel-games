import pyxel
import math

class Player:
    def __init__(self):
        '''player position refers to the position of top left pixel of player block'''
        self.x_pos = 8
        self.y_pos = 120
        self.h_velo = 0
        self.v_velo = 0
        self.h_accl = 0
        self.v_accl = 0.27
        self.state = 'rest'

    def get_player_tile_position(self):
        return (math.floor(self.y_pos / 8), math.floor(self.x_pos / 8))   


class App:
    def __init__(self):
        pyxel.init(240, 136, caption="App", fps = 60, scale = 3)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        level_file = open("level.txt", 'r')
        self.level = [[int(x) for x in line.split()] for line in level_file]
        self.player = Player()

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.constants.KEY_Z, 30, 5) and self.is_player_grounded():
            self.player.v_velo = -4
            self.player.state = 'move'
        if pyxel.btn(pyxel.constants.KEY_LEFT):
            self.player.h_velo = -1
            self.player.state = 'move'
        if pyxel.btn(pyxel.constants.KEY_RIGHT):
            self.player.h_velo = 1
            self.player.state = 'move'

        self.update_player()

    def update_player(self):
        if self.player.state == 'rest':
            return
        
        next_x_pos = self.player.x_pos + self.player.h_velo
        self.player.x_pos = self.resolve_h_collision(next_x_pos, self.player.y_pos)
        next_y_pos = self.player.y_pos + self.player.v_velo
        self.player.y_pos = self.resolve_v_collision(self.player.x_pos, next_y_pos)
        if self.player.y_pos != next_y_pos:
            self.player.v_velo = 0
        
        self.player.h_velo = 0
        if not self.is_player_grounded():
            self.player.v_velo += self.player.v_accl
        if self.player.v_velo == 0 and self.is_player_grounded():
            self.player.state = 'rest'

    def draw(self):
        pyxel.cls(12)
        self.draw_level()
        self.draw_player()

    def draw_player(self):
        pyxel.rect(self.player.x_pos, self.player.y_pos, self.player.x_pos + 7, self.player.y_pos + 7, 8)

    def draw_level(self):
        for row in range(17):
            for column in range(30):
                if self.level[row][column] == 1:
                    x_loc = column * 8
                    y_loc = row * 8
                    pyxel.rect(x_loc, y_loc, x_loc + 7, y_loc + 7, 6)

    def resolve_h_collision(self, player_x_pos, player_y_pos):
        player_top_left = self.get_tile_from_pos(player_x_pos,player_y_pos)
        player_top_right = self.get_tile_from_pos(player_x_pos + 7, player_y_pos)
        player_bottom_left = self.get_tile_from_pos(player_x_pos, player_y_pos + 7)
        player_bottom_right = self.get_tile_from_pos(player_x_pos + 7, player_y_pos + 7)
        
        if self.player.h_velo < 0 and (self.level_value_at_tile(player_top_left) or self.level_value_at_tile(player_bottom_left)):
            return (player_top_left[1] * 8) + 8
        elif self.player.h_velo > 0 and (self.level_value_at_tile(player_top_right) or self.level_value_at_tile(player_bottom_right)):
            return (player_top_right[1] * 8) - 8
        return player_x_pos

    def resolve_v_collision(self, player_x_pos, player_y_pos):
        player_top_left = self.get_tile_from_pos(player_x_pos, player_y_pos)
        player_top_right = self.get_tile_from_pos(player_x_pos + 7, player_y_pos)
        player_bottom_left = self.get_tile_from_pos(player_x_pos, player_y_pos + 7)
        player_bottom_right = self.get_tile_from_pos(player_x_pos + 7, player_y_pos + 7)
        
        if self.player.v_velo < 0 and (self.level_value_at_tile(player_top_left) or self.level_value_at_tile(player_top_right)):
            return (player_top_left[0] * 8) + 8
        elif self.player.v_velo > 0 and (self.level_value_at_tile(player_bottom_left) or self.level_value_at_tile(player_bottom_right)):
            return (player_bottom_left[0] * 8) - 8
        return player_y_pos

    def is_player_grounded(self):
        x = self.player.x_pos
        y = self.player.y_pos + 7
        return self.level_value_at_tile(self.get_tile_from_pos(x, y + 1)) or self.level_value_at_tile(self.get_tile_from_pos(x + 7, y + 1))

    def level_value_at_tile(self, tile):
        return self.level[tile[0]][tile[1]]

    def get_tile_from_pos(self, x, y):
        return (math.floor(y / 8), math.floor(x / 8))


if __name__ == '__main__':
    App()