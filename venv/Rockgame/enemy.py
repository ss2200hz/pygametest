import pygame
from Rockgame import consts,player,physics,tools

enemy_config = tools.get_config_by_name('Enemy')
def get_enemy_data(id):
    for i in enemy_config:
        if i['id'] == id:
            return i

class Enemy(physics.Transform):
    def __init__(self,id,position,player_position=(0,0)):
        self.id = id
        data = get_enemy_data(id)
        self.type = data['type']
        self.hp = data['hp']
        self.buff = data['buff']

        super(Enemy,self).__init__(base_speed=data['speed'],position=position,rect_size=tuple(data['size']),aim_point=player_position)
        self.is_dead = False

    # def set_speed(self,player_point):
    #     super(Enemy,self).init_speed(aim_point=player_point)

    def move(self,player_point):
        super(Enemy, self).init_speed(aim_point=player_point)
        super(Enemy, self).move()

    def on_colliderect(self,_obj=None):
        print("enemy")


