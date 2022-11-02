import pygame,math
from Rockgame import consts

class Transform:
    def __init__(self,position=(0,0),base_speed=1,rect_size = (20,20),aim_point=None):
        # 位置
        self.position = position
        # 碰撞矩形
        self._rect = pygame.Rect(self.position, rect_size)
        #速度标量
        self.base_speed = base_speed
        #加速度
        self.acceleration = (0,0)
        #速度向量
        self.init_speed(aim_point)

    #每帧加速度，需外部调用
    def set_acceleration(self,victor):
        self.acceleration = (victor[0],victor[1])

    #每帧速度变化
    def set_speed(self):
        self.speed = (self.speed[0] + self.acceleration[0], self.speed[1] + self.acceleration[1])

    #初始化速度值
    def init_speed(self,aim_point=None):
        if not aim_point:
            self.speed = (0,0)
            return
        x = aim_point[0] - self.position[0]
        y = aim_point[1] - self.position[1]
        l = math.sqrt(x * x + y * y)

        self.speed = (self.base_speed * x/l,self.base_speed * y/l)

    def add_speed(self,victor):
        x = self.speed[0]
        y = self.speed[1]
        self.speed = (self.base_speed * (x + victor[0]),self.base_speed * (y + victor[1]))

    def move(self):

        self.set_speed()
        # 边缘处理
        if not self.is_edge():
            self.position = (self.position[0] + self.speed[0], self.position[1] + self.speed[1])
            # 移动矩形
            self._rect[0] = self.position[0]
            self._rect[1] = self.position[1]

    #发生碰撞后的行为
    def on_colliderect(self,_obj=None):
        return

    #到达边界的行为
    def is_edge(self):
        return self.speed[0] > 0 and self.position[0] >= consts.WINDOW_SIZE[0] - self._rect.size[0]\
        or self.speed[0] < 0 and self.position[0] <= 0\
        or self.speed[1] > 0 and self.position[1] >= consts.WINDOW_SIZE[1] - self._rect.size[1]\
        or self.speed[1] < 0 and self.position[1] <= 0

    #根据目标点坐标获取方向向量
    def get_direct(self,pos):
        x = pos[0] - self.position[0]
        y = pos[1] - self.position[1]
        l = math.sqrt(x * x + y * y)
        return ( x / l, y / l)