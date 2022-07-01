import random
import sys
sys.path.append('E:\\pytest\\game\\venv')
import time

import pygame

from eyesexamgame import tools,level_controller,num_grid,consts

#游戏结束
is_over = False
#全部通过
is_win = False


#重置游戏
def reset_game():
    global is_over
    global is_pass
    global content_list
    global grid_list
    global level
    global level_data
    global level_start_time

    is_over = False
    is_pass = False

    level = 1
    content_list, grid_list = level_controller.init_level(level)
    level_data = level_controller.level_data #刷新关卡数据
    level_start_time = pygame.time.get_ticks()

#点击事件处理
def on_mouse_clicked(pos):
    global is_over
    #数字消失后可点击
    if now_time - level_start_time - consts.READY_TIME * 1000 >= level_data['display_time'] * 1000 or consts.is_test:
        grid = num_grid.get_touch_grid(tools.coor_to_position(coor=pos,
                                                              grid_x=level_data['width'],
                                                              grid_y=level_data['high']),grid_list=grid_list)
        if grid:
            is_Right = level_controller.grid_click_judge(grid,content_list,level_data['level_type'])
            if not is_Right:
                is_over = True
            else:
                del content_list[0]

#通关判定
def pass_level():
    global level
    global content_list
    global grid_list
    global is_over
    global is_win
    global level_data
    global level_start_time

    if len(content_list) <= 0:
        if level < level_controller.level_num:
            level += 1
            content_list, grid_list = level_controller.init_level(level)
            level_data = level_controller.level_data #刷新关卡数据
            level_start_time = pygame.time.get_ticks() #重新开始计算关卡时间
        else:
            is_over = True
            is_win = True

#帧函数，显示更新
def update():
    global is_over
    global is_pass
    screen.fill((0, 0, 0))  # 填充颜色
    #显示格子
    for i in grid_list:
        screen.blit(i.picture,tools.position_to_coor(position=i.position,
                                                     grid_x=level_data['width'],
                                                     grid_y=level_data['high']))
    #显示内容
    for i in content_list:
        font_text = str(i.num)
        font_type = pygame.font.SysFont(i.type,i.size)
        font = font_type.render(font_text,1,i.color)
        if not consts.is_test:
            if now_time - level_start_time - consts.READY_TIME * 1000 < level_data['display_time'] * 1000  or is_over:
                screen.blit(font,tools.number_position_to_coor(position=i.position,
                                                              grid_x=level_data['width'],
                                                              grid_y=level_data['high']))
        else:
            screen.blit(font, tools.number_position_to_coor(position=i.position,
                                                           grid_x=level_data['width'],
                                                           grid_y=level_data['high']))
    if is_over:
        if is_win:
            final_text = consts.WIN_TEXT
        else:
            final_text = consts.LOSE_TEXT
        ft2_font = pygame.font.SysFont("Arial", 50)  # 设置文字字体
        ft2_surf = ft2_font.render(final_text, 1, (253, 177, 6))  # 设置文字颜色
        screen.blit(ft2_surf, [int(screen.get_width() / 2) - int(ft2_surf.get_width() / 2)
            ,int(screen.get_height() / 2) - int(ft2_surf.get_height() / 2)])  # 设置文字显示位置
        pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上

    pygame.display.update()

def cutdown_time():
    screen.fill((0,0,0))
    second = consts.READY_TIME - int((now_time - level_start_time) / 1000)
    font_size = 100

    ft = pygame.font.SysFont("Arial", font_size)
    ft_surf = ft.render(str(second), 1, (253, 177, 6))
    screen.blit(ft_surf, [int(screen.get_width() / 2) - int(ft_surf.get_width() / 2),
                          int(screen.get_height() / 2) - int(ft_surf.get_height() / 2)])
    # pygame.display.flip()
    pygame.display.update()

if __name__ == '__main__':
    pygame.init()                       # 初始化pygame
    screen = pygame.display.set_mode(consts.WINDOW_SIZE)  # 显示窗口
    reset_game()

    while True:
        #获取当前时间
        now_time = pygame.time.get_ticks()
        if now_time - level_start_time <= consts.READY_TIME * 1000:
            for event in pygame.event.get():  # 遍历所有事件
                if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                    sys.exit()
            cutdown_time()
            continue

        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:#P键暂停
                        isPause = ~isPause
                if event.key == pygame.K_RETURN:#Enter重置游戏
                # if event.key == pygame.KSCAN_J:
                    reset_game()
            if not is_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    on_mouse_clicked((x,y))
                #判断是否通关
                pass_level()
        update()
    pygame.quit()  # 退出pygame