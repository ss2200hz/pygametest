import random
import sys
import time

import pygame

from eyesexamgame import tools,level_controller,num_grid

#游戏结束
is_over = False
#全部通过
is_win = False

is_test = True

config = tools.config_data


def reset_game():
    global is_over
    global is_pass
    global content_list
    global grid_list
    global level

    is_over = False
    is_pass = False

    level = 1
    content_list, grid_list = level_controller.init_level(level)

def on_mouse_clicked(pos):
    global is_over
    grid = num_grid.get_touch_grid(pos,grid_list=grid_list)
    if grid:
        is_Right = level_controller.grid_click_judge(grid,content_list,level_data['level_type'])
        if not is_Right:
            is_over = True
        else:
            del content_list[0]


#帧函数，显示更新
def update():
    global is_over
    global is_pass
    screen.fill((0, 0, 0))  # 填充颜色
    #显示格子
    for i in grid_list:
        screen.blit(i.picture,i.display_coor)
    #显示数字
    for i in content_list:
        font_text = str(i.num)
        font_type = pygame.font.SysFont(i.type,i.size)
        font_color = font_type.render(font_text,1,i.color)
        if not is_test:
            if now_time - start_time < level_data['display_time'] * 1000:
                screen.blit(font_color,i.coor)
        else:
            screen.blit(font_color, i.coor)
    if is_over:
        if is_win:
            final_text = "Your Win"
        else:
            final_text = "Your Lose"
        ft2_font = pygame.font.SysFont("Arial", 50)  # 设置文字字体
        ft2_surf = ft2_font.render(final_text, 1, (253, 177, 6))  # 设置文字颜色
        screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置文字显示位置
        pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上

    pygame.display.update()

if __name__ == '__main__':
    pygame.init()                       # 初始化pygame
    screen = pygame.display.set_mode((800,600))  # 显示窗口
    level = 1
    content_list,grid_list = level_controller.init_level(level)
    level_data = level_controller.level_data
    start_time = pygame.time.get_ticks()
    while True:
        now_time = pygame.time.get_ticks()
        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:#P键暂停
                        isPause = ~isPause
                if event.key == pygame.KSCAN_J:#Enter重置游戏
                    reset_game()
            if not is_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    on_mouse_clicked((x,y))
                if len(content_list) <= 0:
                    if level < level_controller.level_num:
                        level += 1
                        content_list,grid_list = level_controller.init_level(level)
                    else:
                        is_over = True
                        is_win = True
        update()


    pygame.quit()  # 退出pygame