import Consts
import random
import pygame
#地图房间
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
    # 根据坐标得出房间编号
    def getroomCoor(room):
        return room.Coor[0]*10 + room.Coor[1] + 1

#构建地图
def createMap():
    roomList = []
    for i in range(0,10):
        for j in range(0,13):
            room = Room()
            room.setRoomPosition((j*48,i*48))
            room.setRoomCoor((j,i))#房间坐标编号，行数为横轴，列数为纵轴
            roomList.append(room)

    startPoint,endPoint = createRandomPoint(1,130)
    for room in roomList:
        roomCoor = Room.getroomCoor(room)
        if roomCoor == startPoint:
            room.setRoomStatus(Consts.imgs_dir + "point.png")
            startRoom = room
        elif  roomCoor == endPoint:
            room.setRoomStatus(Consts.imgs_dir + "point.png")
        else:
            room.setRoomStatus(Consts.imgs_dir + "room.png")
    return roomList,startRoom

#随机生成起终点
def createRandomPoint(min,max):
    list = []
    for i in range(min,max+1):
        list.append(i)
    a = random.randint(0, len(list) - 1)
    start = list[a]
    list.remove(a)#确保两点不重复

    b = random.randint(0, len(list) - 1)
    end = list[b]
    return start,end