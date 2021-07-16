import random
import sys

import pygame

imgs_dir = "..\\imgs\\"
weightMinNo = 0
weightMaxNo = 12
hightMinNo = 0
hightMaxNo = 9
class Player(object):
    def __init__(self):
        self.pic_dir = pygame.image.load(imgs_dir + "player.png")
        self.roomNo = (0,0)#所在room编号
        self.playerRect = pygame.Rect(0, 0, 50, 50)

    def playerUpdate(self):
        self.playerRect[0] = self.roomNo[0] * 110 + 25
        self.playerRect[1] = self.roomNo[1] * 110 + 25

    def moveUp(self):
        if self.roomNo[1] > hightMinNo:
            self.roomNo = (self.roomNo[0],self.roomNo[1]-1)
    def moveDown(self):
        if self.roomNo[1] < hightMaxNo:
            self.roomNo = (self.roomNo[0],self.roomNo[1]+1)
    def moveLeft(self):
        if self.roomNo[0] > weightMinNo:
            self.roomNo = (self.roomNo[0]-1,self.roomNo[1])
    def moveRight(self):
        if self.roomNo[0] < weightMaxNo:
            self.roomNo = (self.roomNo[0]+1,self.roomNo[1])

class Room(object):
    def __init__(self):
        self.position = (0,0)
    # 房间位置
    def setRoomPosition(self,pos):
        self.position = pos
    #设置起终点图片
    def setRoomStatus(self,pic):
        self.roomStatus = pygame.image.load(pic)
    #设置房间坐标
    def setRoomCoor(self,coor):
        self.Coor = coor
    #房间编号
    def setRoomNo(self,no):
        self.No = no

#构建地图
def createMap():
    roomList = []
    no = 1
    for i in range(0,10):
        for j in range(0,13):
            room = Room()
            room.setRoomPosition((j*48,i*48))
            room.setRoomCoor((j,i))
            room.setRoomNo(no)
            no = no + 1
            roomList.append(room)

    startPoint,endPoint = createRandomPoint(1,150)
    for room in roomList:
        if room.No == startPoint or room.No == endPoint:
            room.setRoomStatus("../imgs/point.png")
        else:
            room.setRoomStatus("../imgs/room.png")
    return roomList

#随机生成起终点
def createRandomPoint(min,max):
    list = []
    for i in range(min,max+1):
        list.append(i)
    a = random.randint(0, len(list) - 1)
    start = list[a]
    list.remove(a)
    b = random.randint(0, len(list) - 1)
    end = list[b]
    return start,end

roomList = createMap()

def updateMap():
    screen.fill((0, 0, 0))  # 填充颜色
    #显示房间
    for i in roomList:
        screen.blit(i.roomStatus,i.position)
    #显示玩家位置
    screen.blit(player.pic_dir,(player.roomNo[0] * 48 + 10,player.roomNo[1] * 48 + 10))
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