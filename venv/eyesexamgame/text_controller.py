import random

import pygame
import tools,consts

class CharContent:
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

    #设置字符
    def set_char(self,char):
        self.char = char
        self.text = char

    def set_position(self,position):
        self.position = position


#读取文本内容配置
def get_text_config():
    for data in tools.config_data:
        if data['sheet_name'] == 'Sentence':
            return data['data']
    raise Exception('not found text config!')

text_config = get_text_config()

#读取配置表内容并生成对应字符列表
def get_text_by_config(index_min,index_max):
    ran_index = random.randint(index_min,index_max)
    content_list = []
    for text_data in text_config:
        if not text_data['id'] or text_data['id'] == '':
            continue
        if text_data['index'] == ran_index:
            content_list.append(text_data)
    if len(content_list) <= 0:
        raise Exception('index out of config range or all id is null !')
    #随机抽取一个
    x = random.randint(0,len(content_list) - 1)
    text_str = content_list[x]['content']
    #生成字符列表
    char_list = []
    for char in text_str:
        char_list.append(char)

    return char_list

#生成随机位置文字序列
def init_content_list(config_data,char_list,coor_list):
    result_list = []
    for i in range(0,len(char_list)):
        char_content = CharContent(display_time=config_data['display_time'],
                         font_color=config_data['font_color'],
                         font_type=config_data['font_type'],
                         font_size=config_data['font_size'])
        char_content.set_char(char_list[i])
        char_content.set_position(coor_list[i])
        result_list.append(char_content)
    return result_list

#获得所有重复字符的结果index集
def get_repeat_obj_list(list):
    result_list = []
    l1 = []
    for i in range(0,len(list)):
        _obj = list[i]
        for j in range(0,len(list)):
            if list[j].char == _obj.char:
                l1.append(j)
        result_list.append(l1.copy())
        l1.clear()

    return result_list

if __name__ == '__main__':
    # char_list = ['一','二','二','三','四','四','一','三','五']
    # print(get_repeat_char_list(char_list))
    for i in range(0,100):
        char_list = get_text_by_config(1,2)
        print(char_list)
