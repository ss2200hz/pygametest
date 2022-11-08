import sys
sys.path.append('E:\\pytest\\game\\venv')
import pygame
from Rockgame import consts,bullet,map,tools

_map = map.Map(1)

create_enemy_time = 0

is_pause = False

is_over = False

#显示刷新
def update():
    screen.fill((0,0,0))
    global is_over
    global create_enemy_time
    if _player.is_dead and not consts.IS_TEST:
        is_over = True
    if not is_over:
        #更新玩家位置
        _player.move()
        # print(_player._rect)
        _player.shoot(mouse_position)
        screen.blit(_player.player_img,_player.position)
        #显示所有子弹
        draw_bullets()
        draw_walls()
        #定时生成敌人
        if pygame.time.get_ticks() - create_enemy_time > 1000:
            _map.create_enemy()
            create_enemy_time = pygame.time.get_ticks()
        #显示所有敌人
        draw_enemy()
    else:
        final_text = "You Dead!!"
        ft2_font = pygame.font.SysFont(consts.FONT_HEITI, 50)  # 设置文字字体
        ft2_surf = ft2_font.render(final_text, 1, (253, 177, 6))  # 设置文字颜色
        screen.blit(ft2_surf, [int(screen.get_width() / 2) - int(ft2_surf.get_width() / 2)
            , int(screen.get_height() / 2) - int(ft2_surf.get_height() / 2)])  # 设置文字显示位置
        pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上
    pygame.display.update()

#显示所有子弹
def draw_bullets():
    for i in bullet.bullet_builder.bullet_list:
        if i.is_removed == True:
            continue
        color = i.color
        if i.type == 1:
            pass
            #子弹颜色
            #三角形各顶点坐标
            # print(i.position)
        elif i.type == 2:
            pass
            # 子弹颜色，暂时写死
        pygame.draw.polygon(screen,color,tools.caculate_bullet_points(i._rect,i.type),2)
        i.move()


#显示所有敌人
def draw_enemy():
    for i in _map.enemy_list:
        if not i.is_dead:
            #绘制颜色
            color = i.color
            #外框矩形
            pygame.draw.rect(screen,color,i._rect,2)
            if i.type == 1:
                pygame.draw.polygon(screen, color, tools.caculate_enemy_points(i._rect,i.type), 2)
            elif i.type == 2:
                pygame.draw.polygon(screen, color, tools.caculate_enemy_points(i._rect, i.type), 2)
            i.move(_player.position)

#显示所有墙壁
def draw_walls():
    for i in _map.wall_list:
        if not i.is_destroed:
            color = (30, 144, 255)
            pygame.draw.rect(screen,color,i._rect,0)

#碰撞检测
def check_colliderect():
    #所有子弹的碰撞
    for i in bullet.bullet_builder.bullet_list:
        if not i.is_removed:
            #与敌人碰撞
            for j in _map.enemy_list:
                if not j.is_dead:
                    if i._rect.colliderect(j._rect):
                        i.on_colliderect(j)
                        j.on_colliderect(i)
    #玩家的碰撞
    for i in _map.enemy_list:
        if not i.is_dead:
            if i._rect.colliderect(_player._rect):
                i.on_colliderect(_player)
                _player.on_colliderect(i)

def reset_game():
    global is_over
    global is_pause
    global _map
    global _player
    global mouse_position
    is_over = False
    is_pause = False
    _map = map.Map(1)
    _map.create_player()
    _player = _map._player
    # 鼠标位置
    mouse_position = (0, 0)

if __name__ == '__main__':
    pygame.init()                            # 初始化pygame
    clock = pygame.time.Clock()              # 设置时钟
    screen = pygame.display.set_mode(consts.WINDOW_SIZE)   # 显示窗口

    _map.create_player()
    _player = _map._player
    #鼠标位置
    mouse_position = (0,0)
    while True:
        #限定帧率为60帧
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #P键暂停
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    is_pause = ~is_pause
            if is_pause:
                continue
            #键盘操作
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    _player.add_speed((0,-1))
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    _player.add_speed((1,0))
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    _player.add_speed((0,1))
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    _player.add_speed((-1,0))
                #切换射击类型
                if event.key == pygame.K_1:
                    _player.shoot_type = 1
                if event.key == pygame.K_2:
                    _player.shoot_type = 2
                #重置游戏
                if event.key == pygame.K_RETURN:
                    reset_game()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    _player.add_speed((0, 1))
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    _player.add_speed((-1, 0))
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    _player.add_speed((0, -1))
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    _player.add_speed((1, 0))

            # #鼠标操作
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:
                    mouse_position = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_position = event.pos
                    _player.is_shoot = True
                elif event.button == 3:
                    _map.create_enemy()


            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    _player.is_shoot = False

        if not is_pause:
            update()
            if not is_over:
                check_colliderect()

