import pygame
from Rockgame import consts,player,physics

class Enemy(physics.Transform):
    def __init__(self,id,type,hp,buff,speed,position,size=(20,20),player_position=(0,0)):
        self.id = id
        self.type = type
        self.hp = hp
        self.buff = []
        if buff:
            for i in buff:
                self.buff.append(i)

        super(Enemy,self).__init__(base_speed=speed,position=position,rect_size=size,aim_point=player_position)
        self.is_dead = False

    def set_speed(self,player_point):
        super(Enemy,self).init_speed(aim_point=player_point)

    def move(self,pos):

        super(Enemy, self).move()


