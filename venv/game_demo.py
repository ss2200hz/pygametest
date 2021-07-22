import random
import sys
import Room,Road,Player,Consts,MoveController
import pygame

isPause = False

#帧函数，显示更新
def update():
    screen.fill((0, 0, 0))  # 填充颜色
    #显示道路
    for i in roadList:
        screen.blit(i.picDir,i.position)
    #显示房间
    for i in roomList:
        screen.blit(i.roomStatus,i.position)
    #显示玩家位置
    screen.blit(player.pic_dir,(player.roomCoor[0] * 48 + 10,player.roomCoor[1] * 48 + 10))
    #更新玩家矩形
    player.playerUpdate()
    pygame.display.update()

if __name__ == '__main__':
    pygame.init()                       # 初始化pygame
    size = width, height = 640, 480     # 设置窗口大小
    screen = pygame.display.set_mode(size)  # 显示窗口
    roomList,startRoom,endRoom = Room.createMap()#初始化地图
    roadList = Road.initAllRoads(None)#初始化道路
    player = Player.Player()#初始化玩家
    player.roomCoor = startRoom.Coor
    while True:
        for event in pygame.event.get():  # 遍历所有事件
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()
            if event.type == pygame.KEYDOWN:#P键暂停
                if event.key == pygame.K_p:
                    if isPause:
                        isPause = False
                    else:
                        isPause = True

            if not isPause:
                if event.type == pygame.KEYDOWN:#移动角色
                    if event.key == pygame.K_LEFT:
                        moveDirection = Consts.leftDerection
                    if event.key == pygame.K_RIGHT:
                        moveDirection = Consts.rightDerection
                    if event.key == pygame.K_UP:
                        moveDirection = Consts.upDerection
                    if event.key == pygame.K_DOWN:
                        moveDirection = Consts.downDerection
                    if MoveController.isPlayerCanMove(moveDirection=moveDirection,
                                                      roadList=roadList,
                                                      player=player):
                        MoveController.moveCharacter(character=player,direction=moveDirection)
                update()


    pygame.quit()  # 退出pygame