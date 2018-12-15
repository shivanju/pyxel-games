import utils

class Player:
    def __init__(self):
        '''player position refers to the position of top left pixel of player block'''
        self.height = 8
        self.width = 6
        self.x_pos = 8
        self.y_pos = 120
        self.h_velo = 0
        self.v_velo = 0
        self.h_accl = 0
        self.v_accl = 0.20
        self.facing = 'right'
        self.state = 'rest'

    def get_player_tile_position(self):
        '''
        returns the player tile position
        '''
        return (math.floor(self.y_pos / 8), math.floor(self.x_pos / 8))

    def get_player_corners(self):
        '''
        returns the dictionary of player's corner tiles
        '''
        return { 
                    'TL': utils.get_tile_from_pos(self.x_pos,self.y_pos),
                    'TR': utils.get_tile_from_pos(self.x_pos + self.width - 1, self.y_pos),
                    'BL': utils.get_tile_from_pos(self.x_pos, self.y_pos + self.height - 1),
                    'BR': utils.get_tile_from_pos(self.x_pos + self.width - 1, self.y_pos + self.height - 1)
        }