import random
import sys
import time

import pygame

from eyesexamgame import tools,num_grid,numbers_controller

is_over = False
is_Win = False
is_test = tools.config_data['is_test']

config = tools.config_data

grid_list = num_grid.grid_list
number_list = numbers_controller.number_list
#当前正确的点击数字
now_number=0

def reset_game():
    global now_number
    global is_over
    global is_Win
    global number_list
    global grid_list
    # 当前正确的点击数字
    now_number = 0
    is_over = False
    is_Win = False

    num_grid.grid_list = num_grid.init_all_grid()
    numbers_controller.number_list = numbers_controller.init_all_numbers_controller()
    grid_list = num_grid.grid_list
    number_list = numbers_controller.number_list


#被点击的坐标，当前正确的点击数字
def judge(coor):
    global now_number
    global is_over
    global is_Win
    grid_postion = num_grid.get_touch_grid(coor)

    if grid_postion:
        print(grid_postion)
        if number_list[now_number].position == grid_postion:
            now_number += 1
            if now_number == len(number_list):
                is_Win = True
                is_over = True
        else:
            is_Win = False
            is_over = True

#帧函数，显示更新
def update():
    global is_over
    global is_Win
    screen.fill((0, 0, 0))  # 填充颜色
    #显示格子
    for i in grid_list:
        screen.blit(i.picture,i.display_coor)
    #显示数字
    for i in number_list:
        font_text = str(i.num)
        font_type = pygame.font.SysFont(i.type,i.size)
        font_color = font_type.render(font_text,1,i.color)
        if not is_test:
            if now_time - start_time < tools.config_data['display_time'] * 1000:
                screen.blit(font_color,i.coor)
        else:
            screen.blit(font_color, i.coor)
    if is_over:
        if is_Win:
            final_text = "Your Win"
        else:
            final_text = "Your Lose"
        ft2_font = pygame.font.SysFont("Arial", 50)  # 设置文字字体
        ft2_surf = ft2_font.render(final_text, 1, (253, 177, 6))  # 设置文字颜色
        screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  # 设置文字显示位置
        pygame.display.flip()  # 更新整个待显示的Surface对象到屏幕上
        is_over = True

    pygame.display.update()

if __name__ == '__main__':
    pygame.init()                       # 初始化pygame
    screen = pygame.display.set_mode(tools.get_window_size())  # 显示窗口
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
                    judge((x,y))
        update()


    pygame.quit()  # 退出pygame