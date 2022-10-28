import pygame
import math
from Rockgame import bullet,consts

class Bullet:
    #初始化，类型，起始位置，大小
    def __init__(self,type,position,size):
        #子弹类型
        self.type = 1
        #设置位置
        self.position = position
        #初始化矩形
        self.bullet_rect = pygame.Rect(position,size)
        #速度
        self.speed = (0,0)
        #基础速度
        self.base_speed = 5
        #是否已被销毁
        self.is_removed = False

    #向目标方向移动
    def set_speed(self,pos):
        if self.type == 1:
            x = pos[0] - self.position[0]
            y = pos[1] - self.position[1]
            l = math.sqrt(x*x + y*y)
            self.speed = (self.base_speed * x/l, self.base_speed * y/l)

    def move(self):
        x = int(self.position[0] + self.speed[0])
        y = int(self.position[1] + self.speed[1])
        self.position = (x,y)

if __name__ == '__main__':
    bullet = Bullet(1,(800,600),(0,0))
    bullet.set_speed((100,80))
    print(bullet.speed)