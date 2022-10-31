import pygame
import math
from Rockgame import bullet,consts

class Bullet:
    #初始化，类型，起始位置，大小，目标点
    def __init__(self,type,position,size,aim=None):
        #子弹类型
        self.type = 1
        #设置位置
        self.position = position
        #初始化矩形
        self.size = size
        self.bullet_rect = pygame.Rect(position,size)
        #基础速度
        self.base_speed = 5
        #是否已被销毁
        self.is_removed = False

        self.set_speed(aim)

    def set_speed(self,aim):
        #设置速度
        if aim != None:
            x = aim[0] - self.position[0]
            y = aim[1] - self.position[1]
            l = math.sqrt(x * x + y * y)
            self.speed = (self.base_speed * x / l, self.base_speed * y / l)
        else:
            self.speed = (0,0)

    def move(self):
        #超出边界
        if self.position[0] < 0 or self.position[0] > consts.WINDOW_SIZE[0]\
            or self.position[1] < 0 or self.position[1] > consts.WINDOW_SIZE[1]:
            self.is_removed = True
            return

        x = self.position[0] + self.speed[0]
        y = self.position[1] + self.speed[1]
        self.position = (x,y)

#子弹构建工厂
class BulletBuilder:
    def __init__(self):
        #子弹池
        self.bullet_list = []
    #创建子弹对象
    def create_bullet(self,type,position,size,aim):
        if len(self.bullet_list) <= 0:
            bullet = Bullet(type=type,position=position,size=size,aim=aim)
            self.bullet_list.append(bullet)
            return bullet

        else:
            for i in self.bullet_list:
                if i.is_removed:
                    i.type = type
                    i.position = position
                    i.size = size
                    i.set_speed(aim)
                    i.is_removed = False
                    return i
            bullet = Bullet(type=type, position=position, size=size,aim=aim)
            self.bullet_list.append(bullet)
            return bullet

#构建工厂实例
bullet_builder = BulletBuilder()

if __name__ == '__main__':
    bullet = Bullet(1,(800,600),(0,0))
    bullet.set_speed((100,80))
    print(bullet.speed)