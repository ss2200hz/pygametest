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
        # self.walls = map_data['walls']
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
        #所有敌人
        self.enemy_list = []
        # #加载爆炸后的痕迹
        self.trace_list = []

    #获得区域坐标
    def change_area_to_position(self,area):
        for i in self.area_list:
            if i['id'] == area:
                return i['start_point'],i['end_point']
        print(area)

    #坐标位置所在区域
    def change_pos_to_area(self,pos):
        area_width = consts.WINDOW_SIZE[0] / self.size[0]
        area_heigh = consts.WINDOW_SIZE[1] / self.size[1]
        a = pos[0] / area_width
        b = pos[1] / area_heigh
        return  b * 10 + a + 1

    def create_player(self):
        self._player = player.Player(position=self.player_position)

    #获取当前活着的敌人数量
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

    #获得所有敌人死亡痕迹所占区域
    def add_trace(self):
        for i in self.enemy_list:
            if i.is_dead:
                #该敌人的四个顶点坐标
                a = (i._rect[0],i._rect[1])
                b = (i._rect[0] + i._rect[2],i._rect[1])
                c = (i._rect[0],i._rect[1] + i._rect[3])
                d = (i._rect[0] + i._rect[2],i._rect[1] + i._rect[3])
                for j in [a,b,c,d]:
                    area_id = self.change_pos_to_area(j)
                    self.trace_list.append(area_id)



