import pygame
from Rockgame import physics,tools

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
        if _obj.__class__.__name__ == 'Bullet':
            if _obj.type == self.type:
                damage = _obj.damage
                self.hp -= damage
                if self.hp <= 0:
                    self.is_dead = True
            else:
                self.grow_up()
        elif _obj.__class__.__name__ == 'Player':
            self.is_dead = True

    #放大
    def grow_up(self):
        #每次增大系数
        grow_x_num = 5
        grow_y_num = 5
        x = self._rect.size[0]
        y = self._rect.size[1]
        self._rect = pygame.Rect(self.position,(x+grow_x_num,y+grow_y_num))