import pygame
from eyesexamgame import consts

class NumGrid:
    def __init__(self,picture,clicked_pic):
        self.picture = pygame.image.load(consts.IMG_DIR + picture)
        self.clicked_pic = clicked_pic
        self.is_clicked = False

    #设置状态
    def on_clicked(self):
        if not self.is_clicked:
            self.picture = pygame.image.load(consts.IMG_DIR + self.clicked_pic)
            self.is_clicked = True
        else:
            self.picture = pygame.image.load(consts.IMG_DIR + self.picture)
            self.is_clicked = False

    #根据坐标设置可点击像素范围
    def set_position(self,position):
        x = position[0] + 1
        y = position[1] + 1
        self.position = (x,y)
        #点击范围最小像素值
        width_min = x * consts.interval + (x - 1) * consts.grid_width
        high_min = y * consts.interval + (y - 1) * consts.grid_high
        # 点击范围最大像素值
        width_max = width_min + consts.grid_width
        high_max = high_min + consts.grid_high

        self.display_coor = (width_min,high_min) #图片位置
        self.touch_coor = (width_max,high_max) #最大可点击范围

#生成所有格子
def init_all_grid(width,high,grid_picture,clicked_picture):
    grid_list = []
    for i in range(0,high):
        for j in range(0,width):
            grid = NumGrid(grid_picture,clicked_picture)
            grid.set_position((j,i))
            grid_list.append(grid)
    return grid_list

#根据点击坐标判断
def get_touch_grid(coor,grid_list,status):
    x = coor[0]
    y = coor[1]
    for grid in grid_list:
        if x<grid.touch_coor[0] and x>grid.display_coor[0]\
            and y<grid.touch_coor[1] and y>grid.display_coor[1]:
            grid.change_status()
            return grid.position