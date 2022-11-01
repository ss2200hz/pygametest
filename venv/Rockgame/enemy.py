import pygame
from Rockgame import consts,player,physics

class Enemy(physics.Transform):
    def __init__(self,type=1,position=(0,0),size=(20,20)):
        self.hp = 1
        self.type = 1
        super(Enemy,self).__init__(position=position,rect_size=size)
        self.is_dead = False
    
    def move(self,pos):
        self.set_speed(pos)
        super(Enemy, self).move()
        
class EnemyBuilder:
    def __init__(self):
        self.enemy_list = []
        
    def create_enmemy(self,type,position):
        if len(self.enemy_list) <= 0:
            enemy = enemy(type=type,position=position)
            self.enemy_list.append(enemy)
            return enemy
        else:
            for i in self.enemy_list:
                if i.is_removed:
                    i.type = type
                    i.position = position
                    i.set_speed(aim)
                    return i
            enemy = enemy(type=type, position=position)
            self.enemy_list.append(enemy)
            return enemy