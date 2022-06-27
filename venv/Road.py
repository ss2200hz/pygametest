import Consts
import random
import pygame
#链接房间的道路
class Road(object):
    def __init__(self):
        self.picDir = pygame.image.load(Consts.IMG_DIR+"road.png")
        self.position = (0,0)
        self.isBroken = False
        self.linkedRooms = []
    def setPosition(self,pos):
        self.position = pos

    def setLinkedRooms(self,roomCoor,direct):
        x = roomCoor[0]
        y = roomCoor[1]
        if direct == Consts.UP_DIRECTION:
            self.linkedRooms = [(x,y),(x,y-1)]
        if direct == Consts.DOWN_DIRECTION:
            self.linkedRooms = [(x, y), (x, y + 1)]
        if direct == Consts.LEFT_DIRECTION:
            self.linkedRooms = [(x, y), (x - 1, y)]
        if direct == Consts.RIGHT_DIRECTION:
            self.linkedRooms = [(x, y), (x + 1, y)]

#根据room位置及方向生成通路
def initRoadByRoom(roomCoor,derection):
    x = roomCoor[0]*48
    y = roomCoor[1]*48
    road = Road()
    if derection == Consts.LEFT_DIRECTION:
        road.setPosition((x-20,y+10))
    elif derection == Consts.UP_DIRECTION:
        road.setPosition((x+10,y-20))
    elif derection == Consts.RIGHT_DIRECTION:
        road.setPosition((x+40,y+10))
    elif derection == Consts.DOWN_DIRECTION:
        road.setPosition((x+10,y+40))
    road.setLinkedRooms(roomCoor,derection)
    return road

#根据房间编号删除road
def deleteRoadByRoom(roomCoor_1,roomCoor_2,roadList):
    for i in roadList:
        if i.linkedRooms == [roomCoor_1,roomCoor_2] or \
            i.linkedRooms == [roomCoor_2,roomCoor_1]:
            print("delete road")
            i.isBroken = True
            return

#横向优先生成起终点通路
def createHLTypeRoad(startRoom,endRoom):
    x1 = startRoom.Coor[0]
    x2 = endRoom.Coor[0]
    y1 = startRoom.Coor[1]
    y2 = endRoom.Coor[1]
    roadList = []
    if x1<x2:
        for x in range(x1,x2):
            roadList.append(initRoadByRoom((x,y1),Consts.RIGHT_DIRECTION))
    elif x1>x2:
        x = x1
        while x>x2:
            roadList.append(initRoadByRoom((x,y1),Consts.LEFT_DIRECTION))
            x-=1
    if y1<y2:
        for y in range(y1,y2):
            roadList.append(initRoadByRoom((x2, y), Consts.DOWN_DIRECTION))
    elif y1>y2:
        for y in range(y2,y1):
            roadList.append(initRoadByRoom((x2, y), Consts.DOWN_DIRECTION))
    return roadList

#纵向优先生成起终点通路
def createVLTypeRoad(startRoom,endRoom):
    x1 = startRoom.Coor[0]
    x2 = endRoom.Coor[0]
    y1 = startRoom.Coor[1]
    y2 = endRoom.Coor[1]
    roadList = []
    if y1<y2:
        for y in range(y1,y2):
            roadList.append(initRoadByRoom((x1,y),Consts.DOWN_DIRECTION))
    elif y1>y2:
        y=y1
        while y>y2:
            roadList.append(initRoadByRoom((x1,y),Consts.UP_DIRECTION))
            y-=1
    if x1<x2:
        for x in range(x1,x2):
            roadList.append(initRoadByRoom((x,y2),Consts.RIGHT_DIRECTION))
    elif x1>x2:
        for x in range(x2,x1):
            roadList.append(initRoadByRoom((x,y2),Consts.RIGHT_DIRECTION))
    return roadList

#根据起终点位置生成路线
def initAllRoads():
    roadList = []
    for i in range(0, 10):
        for j in range(0, 13):
            for k in [0,3]:
                if j == 12 and k == 3:
                    pass
                else:
                    roadList.append(initRoadByRoom((j,i),k))
    return roadList
