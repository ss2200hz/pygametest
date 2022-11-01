import pygame
import math
from Rockgame import bullet,consts,physics

class Bullet(physics.Transform):
    #初始化，类型，起始位置，大小，目标点
    def __init__(self,type,position,size,pos=None):
        #子弹类型
        self.type = type
        #伤害值
        self.damage = 1
        # 继承物理移动效果
        super(Bullet,self).__init__(position=position,base_speed=5,rect_size=size)
        #是否已被销毁
        self.is_removed = False

        if self.type == 1:
            self.speed = (self.base_speed * self.get_direct(pos)[0], self.base_speed * self.get_direct(pos)[1])
        elif self.type == 2:
            self.speed = (1,0)

    def is_edge(self):
        if self.position[0] < 0 or self.position[0] > consts.WINDOW_SIZE[0] - self._rect.size[0] \
            or self.position[1] < 0 or self.position[1] > consts.WINDOW_SIZE[1] - self._rect.size[1]:
            self.is_removed = True
        super(Bullet,self).is_edge()

    def move(self):
        if self.type == 1:
            pass
        elif self.type == 2:
            x = self.speed[0]
            y = self.speed[1]
            sin_speed = x/math.sqrt(x*x + y*y)
            cos_speed = y/math.sqrt(x*x + y*y)
            a = (0.03*cos_speed,0.03*sin_speed)
            print(a)
            print(self.speed)
            self.set_acceleration(a)
        super(Bullet,self).move()

    #重置状态
    def reset_status(self,type,position,size,pos):
        self.type = type
        self.position = position
        self.size = size
        self.is_removed = False
        if self.type == 1:
            self.speed = (self.base_speed * self.get_direct(pos)[0], self.base_speed * self.get_direct(pos)[1])
        elif self.type == 2:
            self.speed = (3,0)

#子弹构建工厂
class BulletBuilder:
    def __init__(self):
        #子弹池
        self.bullet_list = []
    #创建子弹对象
    def create_bullet(self,type,position,size,pos):
        if len(self.bullet_list) <= 0:
            bullet = Bullet(type=type,position=position,size=size,pos=pos)
            self.bullet_list.append(bullet)
            return bullet

        else:
            for i in self.bullet_list:
                if i.is_removed:
                    i.reset_status(type,position,size,pos)
                    return i
            bullet = Bullet(type=type, position=position, size=size,pos=pos)
            self.bullet_list.append(bullet)
            return bullet

#构建工厂实例
bullet_builder = BulletBuilder()

if __name__ == '__main__':
    bullet = Bullet(1,(800,600),(0,0))
    bullet.set_speed((100,80))
    print(bullet.speed)