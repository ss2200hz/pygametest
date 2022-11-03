import pygame
from Rockgame import bullet as _bullet,consts,physics


class Player(physics.Transform):
    def __init__(self,position = (0,0)):
        #初始化图片
        self.player_img = pygame.image.load(consts.IMG_DIR + "player1.png")
        #继承物理移动效果
        super(Player,self).__init__(position=position,base_speed=1,rect_size=consts.PLAYER_IMG_SIZE)

        self.is_shoot = False

        self.last_shoot_time = 0

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
            if pygame.time.get_ticks() - self.last_shoot_time >= 300:
                _bullet.bullet_builder.create_bullet(1,self.position,pos)
                self.last_shoot_time = pygame.time.get_ticks()
                print(len(_bullet.bullet_builder.bullet_list))