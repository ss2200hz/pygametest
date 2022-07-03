import random

import pygame
from eyesexamgame import consts,tools

class Numbers:
    def __init__(self,display_time,font_color,font_type,font_size):
        self.display_time = display_time
        #设置颜色
        if ',' in font_color:
            _color = font_color.split(',')
            color = []
            for i in _color:
                color.append(int(i))
            self.color = tuple(color)
        else:
            self.color = (255,255,255)

        #设置字体
        if font_type != None and font_type != '':
            self.type = font_type
        else:
            self.type = 'Arial'
        #字体大小
        self.size = font_size

    def set_num(self,num):
        self.num = num
        self.text = num

    def set_position(self,position):
        self.position = position
        # x = position[0]
        # y = position[1]
        # width = x * consts.INTERVAL + (x - 1) * consts.GRID_WIDTH + 10
        # high = y * consts.INTERVAL + (y - 1) * consts.GRID_HIGH - 5
        # self.coor = (width,high)

#根据格子数量生成一组数字
def init_all_numbers(number_data,start_num,is_random,num,plus_num,coor_list):
    number_list = []
    #根据规则随机生成指定数量数字
    # start_num = consts.config_data['start_num']
    numbers = [start_num]
    #固定间隔大小生成
    if not is_random:
        for i in range(1,num):
            n = start_num + i * plus_num
            numbers.append(n)
    #按照指定范围随机生成
    else:
        pass
    #随机生成位置
    for i in range(0,num):
        number = Numbers(display_time=number_data['display_time'],
                         font_color=number_data['font_color'],
                         font_type=number_data['font_type'],
                         font_size=number_data['font_size'])
        number.set_num(numbers[i])
        number.set_position(coor_list[i])
        number_list.append(number)
    return number_list

#生成指定个数随机无重复坐标
def create_random_coor(coor=(0,0),num=0):
    x = coor[0]
    y = coor[1]
    coor_list = []
    result_list = []
    for i in range(1,x+1):
        for j in range(1,y+1):
            coor_list.append((i,j))
    for i in range(0,num):
        a = random.randint(0,len(coor_list) - 1)
        result_list.append(coor_list[a])
        coor_list.remove(coor_list[a])
    return result_list

# number_list = init_all_numbers()

if __name__ == '__main__':
    list = init_all_numbers()
    for i in list:
        print(i.num,i.position)