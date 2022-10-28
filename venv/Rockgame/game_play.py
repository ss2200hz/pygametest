import sys
sys.path.append('E:\\pytest\\game\\venv')
import pygame
from Rockgame import player,consts,bullet

player = player.Player()

#显示刷新
def update():
    screen.fill((0,0,0))

    player.move()
    screen.blit(player.player_img,player.position)

    pygame.display.update()

if __name__ == '__main__':
    pygame.init()                            # 初始化pygame
    clock = pygame.time.Clock()              # 设置时钟
    screen = pygame.display.set_mode(consts.WINDOW_SIZE)   # 显示窗口

    while True:
        #限定帧率为60帧
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #键盘操作
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.add_speed((0,-1))
                if event.key == pygame.K_RIGHT:
                    player.add_speed((1,0))
                if event.key == pygame.K_DOWN:
                    player.add_speed((0,1))
                if event.key == pygame.K_LEFT:
                    player.add_speed((-1,0))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.add_speed((0, 1))
                if event.key == pygame.K_RIGHT:
                    player.add_speed((-1, 0))
                if event.key == pygame.K_DOWN:
                    player.add_speed((0, -1))
                if event.key == pygame.K_LEFT:
                    player.add_speed((1, 0))

        update()

