import pygame
from eyesexamgame import consts

class NumGrid:
    def __init__(self,picture,clicked_pic):
        self.picture = pygame.image.load(consts.IMG_DIR + picture)
        self.clicked_pic = clicked_pic
        self.not_clicked_pic = picture
        self.is_clicked = False
        self.content = None

    def set_content(self,_obj):
        self.content = _obj

    #设置状态
    def on_clicked(self):
        if not self.is_clicked:
            self.picture = pygame.image.load(consts.IMG_DIR + self.clicked_pic)
            self.is_clicked = True
        else:
            self.picture = pygame.image.load(consts.IMG_DIR + self.not_clicked_pic)
            self.is_clicked = False

    #根据坐标设置可点击像素范围
    def set_position(self,position):
        x = position[0] + 1
        y = position[1] + 1
        self.position = (x,y)
        #点击范围最小像素值
        # width_min = x * consts.INTERVAL + (x - 1) * consts.GRID_WIDTH
        # high_min = y * consts.INTERVAL + (y - 1) * consts.GRID_HIGH
        # 点击范围最大像素值
        # width_max = width_min + consts.GRID_WIDTH
        # high_max = high_min + consts.GRID_HIGH

        # self.display_coor = (width_min,high_min) #图片位置
        # self.touch_coor = (width_max,high_max) #最大可点击范围

#生成所有格子
def init_all_grid(width,high,grid_picture,clicked_picture,content_list):
    grid_list = []
    for i in range(0,high):
        for j in range(0,width):
            grid = NumGrid(grid_picture,clicked_picture)
            grid.set_position((j,i))
            for content in content_list:
                if i+1 == content.position[1] and j+1 == content.position[0]:
                    grid.set_content(content)
            grid_list.append(grid)
    return grid_list

#根据点击坐标判断
def get_touch_grid(position,grid_list):
    x = position[0]
    y = position[1]
    for grid in grid_list:
        if x == grid.position[0] and y == grid.position[1]:
            grid.on_clicked()
            return grid