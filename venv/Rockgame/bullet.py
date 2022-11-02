import pygame
import math
from Rockgame import bullet,consts,physics,tools

bullet_config = tools.get_config_by_name('Bullets')

class Bullet(physics.Transform):
    #初始化，类型，起始位置，大小，目标点
    def __init__(self,type,damage,speed,size,start_pos,end_pos=None):
        #子弹类型
        self.type = type
        #伤害值
        self.damage = damage
        # 继承物理移动效果
        super(Bullet,self).__init__(position=start_pos,base_speed=speed,rect_size=size,aim_point=end_pos)
        #是否已被销毁
        self.is_removed = False

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
    def reset_status(self,type,damage,speed,size,start_pos,end_pos=None):
        self.__init__(type,damage,speed,size,start_pos,end_pos)




#子弹构建工厂
class BulletBuilder:

    def get_bullet_data_by_id(self,id):
        for d in bullet_config:
            if d['id'] == id:
                return d

    def __init__(self):
        #子弹池
        self.bullet_list = []
    #创建子弹对象
    def create_bullet(self,bullet_id,start_pos,end_pos):
        config_dict = self.get_bullet_data_by_id(bullet_id)
        type = config_dict['type']
        damage = config_dict['damage']
        speed = config_dict['speed']
        size = (int(config_dict['size'][0]),int(config_dict['size'][1]))

        if len(self.bullet_list) > 0:
            for i in self.bullet_list:
                if i.is_removed:
                    i.__init__(type=type,damage=damage,speed=speed,size=size,start_pos=start_pos,end_pos=end_pos)
                    return i
        bullet = Bullet(type=type,damage=damage,speed=speed,size=size,start_pos=start_pos,end_pos=end_pos)
        self.bullet_list.append(bullet)
        return bullet

#构建工厂实例
bullet_builder = BulletBuilder()

if __name__ == '__main__':
    bullet = Bullet(1,(800,600),(0,0))
    bullet.set_speed((100,80))
    print(bullet.speed)