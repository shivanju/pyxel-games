class Player:
    def __init__(self):
        self.height = 10
        self.width = 16
        self.v_velo = 0
        self.v_acc = 0.3
        self.x_pos = 35
        self.y_pos = 120
        self.wings_pos = 0

    def update_player(self):
        self.y_pos += self.v_velo
        if self.y_pos < 0:
            self.y_pos = 0
        elif self.y_pos > 240 - self.height:
            self.y_pos = 240 - self.height
        self.v_velo += self.v_acc