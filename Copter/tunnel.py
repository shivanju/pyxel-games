import random

class Tunnel:
    """Class that describes the tunnel with obstacles in which our helicopter will fly"""
    def __init__(self, speed = 1):
        self.pillars = [] #list of [pillar_up_y, pillar_down_y, pillar_x]
        self.obstacles = [] #list of [pillar_num, obstacle_y1, obstacle_y2]
        self.size = 32 #Pillar width is 8px, screen width is 240, keeping 2 extra pillar for spawning purpose
        self.speed = speed
        self.obstacle_height = 30
        self.current_pillar_height = 2
        self.total_pillar_length = 36
        self.increment = -1 #pillar height increment 
        self.pattern_length = random.randint(1, 30)
        self.obstacle_spawn_time = 100
        
        #generate initial tunnel layout
        for x in range(self.size):
            self.pillars.append([self.current_pillar_height - 1, 136 - self.total_pillar_length + self.current_pillar_height + 1, (x - 1) * 8])
            self.current_pillar_height += 1

    def update(self):
        self.obstacle_spawn_time -= self.speed
        for pillar in self.pillars:
            pillar[2] -= self.speed

        if self.pillars[0][2] < -8:
            if not(self.pattern_length) or self.current_pillar_height < 1 or self.current_pillar_height > self.total_pillar_length - 2:
                self.pattern_length = random.randint(3, 30)
                self.increment *= -1
            self.add_pillar()
            for obstacle in self.obstacles:
                obstacle[0] = obstacle[0] - 1
            if len(self.obstacles) and self.obstacles[0][0] < 0:
                self.obstacles.pop(0)

        if self.obstacle_spawn_time <= 0:
            self.obstacle_spawn_time = random.randint(90, 130)
            obstacle_y_pos = random.randint(self.pillars[31][0] + 1, self.pillars[31][1] - self.obstacle_height)
            self.obstacles.append([31, obstacle_y_pos, obstacle_y_pos + self.obstacle_height - 1])


    def add_pillar(self):
        self.pillars.pop(0)
        self.pillars.append([self.current_pillar_height - 1, 136 - self.total_pillar_length + self.current_pillar_height + 1, self.pillars[-1][2] + 8])
        self.pattern_length -= 1
        self.current_pillar_height += self.increment
