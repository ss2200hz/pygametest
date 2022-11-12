import pygame
from Rockgame import bullet as _bullet,consts,physics


class Player(physics.Transform):
    def __init__(self,position = (0,0)):
        #初始化图片
        self.player_img = pygame.image.load(consts.IMG_DIR + "player1.png")
        #继承物理移动效果
        super(Player,self).__init__(position=position,base_speed=1,rect_size=consts.PLAYER_IMG_SIZE)

        self.is_shoot = False
        #攻击速度,两次射击间的最短时间间隔
        self.attack_speed = 200

        self.last_shoot_time = 0
        #射出的子弹类型
        self.shoot_type = 1

        self.is_dead = False

    def is_edge(self):
        if self.speed[0] > 0 and self.position[0] >= consts.WINDOW_SIZE[0] - self._rect.size[0]:
            self.position = (self.position[0], self.position[1] + self.speed[1])
            return True
        if self.speed[0] < 0 and self.position[0] <= 0:
            self.position = (self.position[0], self.position[1] + self.speed[1])
            return True
        if self.speed[1] > 0 and self.position[1] >= consts.WINDOW_SIZE[1] - self._rect.size[1]:
            self.position = (self.position[0] + self.speed[0], self.position[1])
            return True
        if self.speed[1] < 0 and self.position[1] <= 0:
            self.position = (self.position[0] + self.speed[0], self.position[1])
            return True

    def shoot(self,pos):
        if self.is_shoot:
            #连续射击间隔
            if pygame.time.get_ticks() - self.last_shoot_time >= self.attack_speed:
                _bullet.bullet_builder.create_bullet(self.shoot_type,self.position,pos)
                self.last_shoot_time = pygame.time.get_ticks()

    def on_colliderect(self,_obj=None):
        if _obj.__class__.__name__ == 'Enemy':
            super(Player, self).on_colliderect(_obj)
            self.is_dead = True
            