import Consts
import random
import pygame
#链接房间的道路
class Road(object):
    def __init__(self):
        self.picDir = pygame.image.load(Consts.imgs_dir+"road.png")
        self.position = (0,0)
        self.linkedRooms = []
    def setPosition(self,pos):
        self.position = pos

    def setLinkedRooms(self,roomCoor,direct):
        x = roomCoor[0]
        y = roomCoor[1]
        if direct == Consts.upDerection:
            self.linkedRooms = [(x,y),(x,y-1)]
        if direct == Consts.downDerection:
            self.linkedRooms = [(x, y), (x, y + 1)]
        if direct == Consts.leftDerection:
            self.linkedRooms = [(x, y), (x - 1, y)]
        if direct == Consts.rightDerection:
            self.linkedRooms = [(x, y), (x + 1, y)]

#根据room位置及方向生成通路
def initRoadByRoom(roomCoor,derection):
    x = roomCoor[0]*48
    y = roomCoor[1]*48
    road = Road()
    if derection == Consts.leftDerection:
        road.setPosition((x-20,y+10))
        road.setLinkedRooms(roomCoor,Consts.leftDerection)
    elif derection == Consts.upDerection:
        road.setPosition((x+10,y-20))
        road.setLinkedRooms(roomCoor, Consts.upDerection)
    elif derection == Consts.rightDerection:
        road.setPosition((x+40,y+10))
        road.setLinkedRooms(roomCoor, Consts.rightDerection)
    elif derection == Consts.downDerection:
        road.setPosition((x+10,y+40))
        road.setLinkedRooms(roomCoor, Consts.downDerection)
    return road


def createLTypeRoad(startRoom,endRoom):
    x1 = startRoom.Coor[0]
    x2 = endRoom.Coor[0]
    y1 = startRoom.Coor[1]
    y2 = endRoom.Coor[1]

#根据起终点位置生成路线
def initAllRoads():
    roadList = []
    for i in range(0, 10):
        for j in range(0, 13):
            for k in [0,3]:
                roadList.append(initRoadByRoom((j,i),k))
    return roadList
