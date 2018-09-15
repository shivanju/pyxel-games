class Plane:
    def __init__(self):
        self.position = (60, 50)
        self.gravity = 0.1
        self.velo = 0

    def update(self, velo = None):
        if velo != None:
            self.velo = velo
        self.position = (self.position[0], self.position[1] + self.velo)
        self.velo += self.gravity