import pygame
from Rockgame import enemy ,consts,player,tools



map_config = tools.get_config_by_name('map')

def get_map_data(map_id):
    for d in map_config():
        if d['id'] == map_id:
            return d

#初始化地图
class map:
    def __init__(self,mapid):
        map_data = get_map_data(map_id)
        self.size = map_data['size']
        self.enemy_list = map_data['enemy_list']
        self.enemy_position = map_data['enemy_position']
        self.enemy_num = map_data['enemy_num']
        self.player_position = map_data['player_position']
        self.wall_list = map_data['wall_list']
        #初始化区块
        area_width = consts.WINDOW_SIZE[0]/size[0]
        area_heigh = consts.WINDOW_SIZE[1]/size[1]
        self.area_list = []
        for i in range(0,size[1]):
            for j in range(0,size[0]):
                id = i * 10 + j+1
                start_point = (area_width*j,area_heigh*i)
                end_point = (area_width*(j+1),area_heigh*(i+1))
                area_data = {'id':id,'start_point':start_point,'end_point':end_point}
                self.area_list.append(area_data.copy())


    def create_enemy(self):

        #生成的时间
        self.create_time = pygame.time.get_ticks()



