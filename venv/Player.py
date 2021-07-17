import Consts
import pygame
#玩家角色
class Player(object):
    def __init__(self):
        self.pic_dir = pygame.image.load(Consts.imgs_dir + "player.png")
        self.roomCoor = (0,0)#所在room坐标编号
        self.playerRect = pygame.Rect(0, 0, 50, 50)

    def playerUpdate(self):
        self.playerRect[0] = self.roomCoor[0] * 110 + 25
        self.playerRect[1] = self.roomCoor[1] * 110 + 25

    def move(self,direction):
        if direction == Consts.upDerection:
            if self.roomCoor[1] > Consts.hightMinNo:
                self.roomCoor = (self.roomCoor[0], self.roomCoor[1] - 1)
        elif direction == Consts.downDerection:
            if self.roomCoor[1] < Consts.hightMaxNo:
                self.roomCoor = (self.roomCoor[0], self.roomCoor[1] + 1)
        elif direction == Consts.leftDerection:
            if self.roomCoor[0] > Consts.weightMinNo:
                self.roomCoor = (self.roomCoor[0] - 1, self.roomCoor[1])
        elif direction == Consts.rightDerection:
            if self.roomCoor[0] < Consts.weightMaxNo:
                self.roomCoor = (self.roomCoor[0] + 1, self.roomCoor[1])
