import pygame
from Rockgame import bullet,consts

class Player:
    def __init__(self):
        #初始化图片
        self.player_img = pygame.image.load(consts.IMG_DIR + "player1.png")
        #位置
        self.position = (0,0)
        #玩家矩形
        self.player_rect = pygame.Rect(self.position,consts.PLAYER_IMG_SIZE)
        #当前移动速度，二维向量
        self.speed = (0,0)
        #基础移速
        self.base_speed = 1

        self.is_shoot = False

    def add_speed(self,victor):
        x = self.speed[0]
        y = self.speed[1]
        self.speed = (self.base_speed * (x + victor[0]),self.base_speed * (y + victor[1]))


    #移动位置
    def move(self):
        #移动矩形
        self.player_rect[0] = self.position[0]
        self.player_rect[1] = self.position[1]
        #边缘处理
        if self.speed[0] > 0 and self.position[0] >= consts.WINDOW_SIZE[0] - consts.PLAYER_IMG_SIZE[0]:
            self.position = (self.position[0], self.position[1] + self.speed[1])
            return
        if self.speed[0] < 0 and self.position[0] <= 0:
            self.position = (self.position[0], self.position[1] + self.speed[1])
            return
        if self.speed[1] > 0 and self.position[1] >= consts.WINDOW_SIZE[1] - consts.PLAYER_IMG_SIZE[1]:
            self.position = (self.position[0] + self.speed[0], self.position[1])
            return
        if self.speed[1] < 0 and self.position[1] <= 0:
            self.position = (self.position[0] + self.speed[0], self.position[1])
            return

        self.position = (self.position[0] + self.speed[0], self.position[1] + self.speed[1])

