import random

class Level:
    def __init__(self):
        self.speed = 1
        self.gap = 70
        self.max_hieght_diff_btw_pipes = 70
        self.pipe_width = 35
        self.pipe_distance = 70
        self.max_pipe_len = 140
        self.min_pipe_len = 30
        self.pipe_positions = [140]
        self.pipe_heights = [100]
        self.upper_pipes = []
        self.lower_pipes = []

    def update_level(self):
        if len(self.pipe_heights) < 3:
            size = len(self.pipe_heights) - 1
            self.pipe_positions.append(self.pipe_positions[size] + self.pipe_width + self.pipe_distance)
            self.pipe_heights.append(random.randint(max(self.min_pipe_len, self.pipe_heights[size] - self.max_hieght_diff_btw_pipes), min(self.max_pipe_len, self.pipe_heights[size] + self.max_hieght_diff_btw_pipes)))
            for x in range(size + 1):
                x1 = self.pipe_positions[x]
                x2 = x1 + self.pipe_width - 1
                uy1 = 0
                uy2 = uy1 + self.pipe_heights[x] - 1
                ly1 = self.pipe_heights[x] + self.gap - 1
                ly2 = 239
                self.upper_pipes.append([x1, uy1, x2, uy2])
                self.lower_pipes.append([x1, ly1, x2, ly2])
            return
            

        for x in range(len(self.pipe_positions)):
            self.pipe_positions[x] -= 1

        if self.pipe_positions[0] < -self.pipe_width:
            self.pipe_positions.pop(0)
            self.pipe_positions.append(self.pipe_positions[1] + self.pipe_width + self.pipe_distance)
            self.pipe_heights.pop(0)
            self.pipe_heights.append(random.randint(max(self.min_pipe_len, self.pipe_heights[1] - self.max_hieght_diff_btw_pipes), min(self.max_pipe_len, self.pipe_heights[1] + self.max_hieght_diff_btw_pipes)))
            
        for x in range(3):
            x1 = self.pipe_positions[x]
            x2 = x1 + self.pipe_width - 1
            uy1 = 0
            uy2 = uy1 + self.pipe_heights[x] - 1
            ly1 = self.pipe_heights[x] + self.gap - 1
            ly2 = 239
            self.upper_pipes[x] = [x1, uy1, x2, uy2]
            self.lower_pipes[x] = [x1, ly1, x2, ly2]


    def spawn_pipe_heights(self):
        pipe_heights = []
        return pipe_heights
        for x in range(3):
            pipe_heights.append(random.randint(self.min_pipe_len, self.max_pipe_len))
        return pipe_heights
