import Consts
import pygame
#玩家角色
class Player(object):
    def __init__(self):
        self.pic_dir = pygame.image.load(Consts.IMG_DIR + "player.png")
        self.roomCoor = (0,0)#所在room坐标编号
        self.playerRect = pygame.Rect(0, 0, 50, 50)

    def playerUpdate(self):
        self.playerRect[0] = self.roomCoor[0] * 110 + 25
        self.playerRect[1] = self.roomCoor[1] * 110 + 25

    def move(self,direction):
        if direction == Consts.UP_DIRECTION:
            if self.roomCoor[1] > Consts.HIGHT_MIN_NO:
                self.roomCoor = (self.roomCoor[0], self.roomCoor[1] - 1)
        elif direction == Consts.DOWN_DIRECTION:
            if self.roomCoor[1] < Consts.HIGHT_MAX_NO:
                self.roomCoor = (self.roomCoor[0], self.roomCoor[1] + 1)
        elif direction == Consts.LEFT_DIRECTION:
            if self.roomCoor[0] > Consts.WEIGHT_MIN_NO:
                self.roomCoor = (self.roomCoor[0] - 1, self.roomCoor[1])
        elif direction == Consts.RIGHT_DIRECTION:
            if self.roomCoor[0] < Consts.WEIGHT_MAX_NO:
                self.roomCoor = (self.roomCoor[0] + 1, self.roomCoor[1])