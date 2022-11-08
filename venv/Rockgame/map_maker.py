import pygame,sys
from Rockgame import map,consts

def update():
    screen.fill((0, 0, 0))
    #显示墙壁
    for i in wall_list:
        color = (30, 144, 255)
        wall_pos = _map.change_area_to_position(i)[0]
        # print(wall_pos)
        pygame.draw.rect(screen, color, pygame.Rect(int(wall_pos[0]),int(wall_pos[1]),size_x,size_y), 0)
    #显示敌人生成点
    for i in enemy_list:
        color = (50, 50, 50)
        enemy_pos = _map.change_area_to_position(i)[0]
        pygame.draw.rect(screen, color, pygame.Rect(int(enemy_pos[0]),int(enemy_pos[1]),size_x,size_y), 0)
    #显示玩家出生点
    pygame.draw.rect(screen, (125,125,125), pygame.Rect(int(player_position[0]),int(player_position[1]), size_x, size_y), 0)
    pygame.display.update()

#获得每个区块大小
def get_area_size():
    x = _map.area_list[0]['end_point'][0] - _map.area_list[0]['start_point'][0]
    y = _map.area_list[1]['end_point'][1] - _map.area_list[1]['start_point'][1]
    # print((x,y))
    return x.__int__(),y.__int__()

def change_pos_to_area(pos):
    x = pos[0]
    y = pos[1]
    for i in _map.area_list:
        if i['start_point'][0] <= x and i['end_point'][0] > x\
            and i['start_point'][1] <= y and i['end_point'][1] > y:
            return i['id']

if __name__ == '__main__':
    pygame.init()  # 初始化pygame
    clock = pygame.time.Clock()  # 设置时钟
    screen = pygame.display.set_mode(consts.WINDOW_SIZE)  # 显示窗口

    _map = map.Map(map_id=1)
    #玩家位置
    player_position = (0,0)
    #墙壁列表
    wall_list = []
    #敌人生成点
    enemy_list = []
    #返回结果集
    result_dict = {'walls':wall_list,'player_position':player_position,'enemy_list':enemy_list}

    size_x,size_y = get_area_size()
    # print((size_x,size_y))
    #添加类型，0墙壁，1敌人生成器，2玩家初始点
    draw_type = 0
    while True:
        # 限定帧率为60帧
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    draw_type = 0
                elif event.key == pygame.K_2:
                    draw_type = 1
                elif event.key == pygame.K_3:
                    draw_type = 2
                if event.key == pygame.K_RETURN:

                    print(result_dict)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                area = change_pos_to_area(mouse_position)
                if event.button == 1:
                    if draw_type == 0:
                        if area not in wall_list:
                            wall_list.append(area)
                    elif draw_type == 1:
                        if area not in wall_list:
                            enemy_list.append(area)
                    elif draw_type == 2:
                        pos = _map.change_area_to_position(area)[0]
                        player_position(int(pos[0]),int(pos[1]))
                        result_dict['player_position'] = player_position

                elif event.button == 3:
                    if draw_type == 0:
                        if area in wall_list:
                            wall_list.remove(area)
                    elif draw_type == 1:
                        if area in enemy_list:
                            enemy_list.remove(area)
                print(result_dict)

        update()