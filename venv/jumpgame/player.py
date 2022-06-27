import pygame
from jumpgame import tools
#玩家角色
class Player():
    move_speed = 5
    def __init__(self,position_x,position_y):
        self.position_x = position_x
        self.position_y = position_y
        #当前状态下的图片
        self.state_img = pygame.image.load(tools.Consts.IMG_DIR + "player.png")
        self.rect = pygame.Rect(position_x,position_y,50,50)

    def playerUpdate(self):
        self.rect[0] = self.position_x
        self.rect[1] = self.position_y

    def move(self,direction):
        if direction == tools.Consts.LEFT_DIRECTION:
            self.position_x -= self.move_speed
        elif direction == tools.Consts.RIGHT_DIRECTION:
            self.position_x += self.move_speed