from eyesexamgame import tools,num_grid,numbers_controller

#读取关卡配置
def get_level_config():
    for data_direct in tools.config_data:
        if data_direct['sheet_name'] == 'Level':
            return data_direct['data']

    raise Exception('not found level config!')

level_data_config = get_level_config()
level_num = len(level_data_config)

#根据id查找关卡
def get_data_by_id(level_id):
    for dict in level_data_config:
        if int(dict['level_id']) == int(level_id):
            return dict
    raise Exception('not found id!')

level_data = None

#根据id加载关卡
def init_level(level_id):
    data = get_data_by_id(level_id)
    global level_data
    level_data = data
    type = data['level_type']
    if type == 1:
        coor_list = numbers_controller.create_random_coor((data['width'],data['high']),data['num'])
        number_data = {'display_time':data['display_time'],
                       'font_color':data['font_color'],
                       'font_type':data['font_type'],
                       'font_size':data['font_size']}
        number_list = numbers_controller.init_all_numbers(number_data=number_data,
                                                          start_num=data['start_num'],
                                                          is_random=data['is_random'],
                                                          num=data['num'],
                                                          plus_num=data['plus_num'],
                                                          coor_list=coor_list)
        grid_list = num_grid.init_all_grid(width=data['width'],high=data['high'],
                                           grid_picture=data['grid_picture'],
                                           clicked_picture=data['grid_picture_clicked'],
                                           content_list=number_list)
        return number_list,grid_list
    else:
        pass

#格子点击判断,方格对象 数据列表 数据列表位置
def grid_click_judge(grid,content_list,level_type):
    # print(grid_postion)
    if not grid.content:
        return False
    if level_type == 1:
        if len(content_list) > 0:
            if grid.position == content_list[0].position:
                return True
            else:
                return False
        else:
            return True

if __name__ == '__main__':
    list1,list2 = init_level(1)
    for i in list1:
        print(i.position,end="")
    print("++++++++++++++++")
    del list1[0]
    for i in list1:
        print(i.position,end="")
    for i in list2:
        if i.content:
            print(i.position,end="")