import random
import sys

import pygame

imgs_dir = "..\\imgs\\"
class Player(object):
    def __init__(self):
        self.pic_dir = pygame.image.load(imgs_dir + "player.png")
        self.roomNo = (0,0)#所在room编号
        self.playerRect = pygame.Rect(0, 0, 50, 50)

    def playerUpdate(self):
        self.playerRect[0] = self.roomNo[0] * 110 + 25
        self.playerRect[1] = self.roomNo[1] * 110 + 25

    def moveUp(self):
        if self.roomNo[1] > 0:
            self.roomNo = (self.roomNo[0],self.roomNo[1]-1)
    def moveDown(self):
        if self.roomNo[1] < 9:
            self.roomNo = (self.roomNo[0],self.roomNo[1]+1)
    def moveLeft(self):
        if self.roomNo[0] > 0:
            self.roomNo = (self.roomNo[0]-1,self.roomNo[1])
    def moveRight(self):
        if self.roomNo[0] < 9:
            self.roomNo = (self.roomNo[0]+1,self.roomNo[1])

class Room(object):
    def __init__(self):
        self.position = (0,0)
        self.isPointRoom = False

    def setRoomPosition(self,pos):
        self.position = pos

    def setPointRoom(self,pointRoom):
        self.isPointRoom = pointRoom

    def setRoomNo(self,number):
        self.No = number

#构建地图
def createMap():
    roomList = []
    for i in range(0,9):
        for j in range(0,9):
            room = Room()
            room.setRoomPosition((j*110,i*110))
            room.setRoomNo((j,i))
            roomList.append(room)
    return roomList

roomList = createMap()

def updateMap():
    screen.fill((0, 0, 0))  # 填充颜色
    #显示房间
    for i in roomList:
        screen.blit(i.roomPic,i.position)
    #显示玩家位置
    screen.blit(player.pic_dir,(player.roomNo[0] * 110 + 25,player.roomNo[1] * 110 + 25))
    #更新玩家矩形
    player.playerUpdate()
    pygame.display.update()

if __name__ == '__main__':
    pygame.init()                       # 初始化pygame
    size = width, height = 640, 480     # 设置窗口大小
    screen = pygame.display.set_mode(size)  # 显示窗口
    player = Player()
    while True:  # 死循环确保窗口一直显示
        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.moveLeft()
                    # print(player.roomNo)
                if event.key == pygame.K_RIGHT:
                    player.moveRight()
                    # print(player.roomNo)
                if event.key == pygame.K_UP:
                    player.moveUp()
                    # print(player.roomNo)
                if event.key == pygame.K_DOWN:
                    player.moveDown()
                    # print(player.roomNo)
        updateMap()

    pygame.quit()  # 退出pygame