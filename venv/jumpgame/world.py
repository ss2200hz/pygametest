import tools
import pygame

visual_object_list = []

class GameWorld:
    def __init__(self,gravity,ground):#世界环境，重力大小，地面位置
        self.gravity = gravity
        self.ground = ground

#相机类，position所处位置，scope视野范围
class Camera:
    def __init__(self,position_x,position_y,scope_x,scope_y,screen):
        self.position_x = position_x
        self.position_y = position_y
        self.scope_x = scope_x
        self.scope_y =scope_y
        self.screen = screen

    #设置相机跟随，跟随物体，跟随坐标，偏移量
    def camera_follow(self,follow_obj,follow_direct,offset=(0,0)):
        #是否触达地图边界
        if self.position_x - scope_x <= 0 or self.position_x + scope >= 2000:
                return
        if follow_direct == tools.Consts.ALL:
            self.position_x = follow_obj.position_x + offset[0]
        elif follow_direct == tools.Consts.HORIZONTAL:
            self.position_y = follow_obj.position_y + offset[1]
        elif follow_direct == tools.Consts.VERTICAL:
            self.position_x = follow_obj.position_x + offset[0]
            self.position_y = follow_obj.position_y + offset[1]

    #显示内容
    def display(self):
        for obj in visual_object_list:
            try:
                #转换坐标
                x = obj.position_x - self.position_x
                y = obj.position_y - self.position_y
                print("x: %d, y: %d"%(x,y))
                self.screen.blit(obj.state_img,(x,y))
            except Exception as e:
                print(e)
                continue