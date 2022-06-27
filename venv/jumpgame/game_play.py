import random
import sys
import pygame
from jumpgame import Factory,world,player,tools

consts = tools.Consts
visual_object_factory = Factory.VisualObjectFactory()
player = visual_object_factory.create_object("player")
isPause = False
isOver = False


#帧函数，显示更新
def update():
    player.playerUpdate()
    pygame.display.update()
    camera.display()

if __name__ == '__main__':
    pygame.init()  # 初始化pygame
    size = width, height = 640, 480  # 设置窗口大小
    screen = pygame.display.set_mode(size)  # 显示窗口
    camera = world.Camera(0, 0, 500, 500,screen)
    font = pygame.font.SysFont("Arial", 50)  # 设置字体和大小
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move(consts.LEFT_DIRECTION)
                elif event.key == pygame.K_RIGHT:
                    player.move(consts.RIGHT_DIRECTION)
            update()