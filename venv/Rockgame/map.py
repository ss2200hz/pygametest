import random

# import pygame
from Rockgame import enemy ,consts,player,tools



map_config = tools.get_config_by_name('Map')

def get_map_data(map_id):
    for d in map_config:
        if d['id'] == map_id:
            return d

#初始化地图
class Map:
    def __init__(self,map_id):
        map_data = get_map_data(map_id)
        self.size = map_data['size']
        self.enemy_id = map_data['enemy_id']
        self.enemy_position = map_data['enemy_position']
        self.enemy_num = map_data['enemy_num']
        self.player_position = map_data['player_position']
        self.wall_list = map_data['wall_list']
        #初始化区块
        area_width = consts.WINDOW_SIZE[0]/self.size[0]
        area_heigh = consts.WINDOW_SIZE[1]/self.size[1]
        self.area_list = []
        for i in range(0,self.size[1]):
            for j in range(0,self.size[0]):
                id = i * 10 + j+1
                start_point = (area_width*j,area_heigh*i)
                end_point = (area_width*(j+1),area_heigh*(i+1))
                area_data = {'id':id,'start_point':start_point,'end_point':end_point}
                self.area_list.append(area_data.copy())
        self.enemy_list = []

    def change_area_to_position(self,area):
        for i in self.area_list:
            if i['id'] == area:
                return i['start_point'],i['end_point']

    def create_player(self):
        self._player = player.Player(position=self.player_position)

    #获取当前或者的敌人数量
    def get_enemy_num(self):
        num = 0
        for i in self.enemy_list:
            if not i.is_dead:
                num += 1
        return num
    #生成敌人
    def create_enemy(self):
        if self.get_enemy_num() < self.enemy_num:
            #随机一个可生成的敌人id
            id = self.enemy_id[random.randint(0,len(self.enemy_id)-1)]
            #随机一个位置
            pos = self.enemy_position[random.randint(0,len(self.enemy_position)-1)]
            _enemy = enemy.Enemy(id=id,position=self.change_area_to_position(pos)[0],player_position=self._player.position)
            self.enemy_list.append(_enemy)

        #生成敌人的时间
        # self.create_enemy_time = pygame.time.get_ticks()


