import sys
sys.path.append('E:\\pytest\\game\\venv')
import pygame
from Rockgame import player,consts,bullet

player = player.Player()


#显示刷新
def update():
    screen.fill((0,0,0))
    #更新玩家位置
    player.move()
    player.shoot(mouse_position)
    screen.blit(player.player_img,player.position)
    #显示所有子弹
    draw_bullets()
    pygame.display.update()

#显示所有子弹
def draw_bullets():
    for i in bullet.bullet_builder.bullet_list:
        if i.is_removed == True:
            continue
        if i.type == 1:
            #子弹颜色，暂时写死
            color = (30,144,255)
            #三角形各顶点坐标
            a = i.position
            b = (i.position[0],i.position[1] + i.size[1])
            c = (i.position[0] + i.size[0],i.position[1] + i.size[1]/2)
            pygame.draw.polygon(screen,color,[a,b,c],2)
            i.move()
            # print(i.position)


if __name__ == '__main__':
    pygame.init()                            # 初始化pygame
    clock = pygame.time.Clock()              # 设置时钟
    screen = pygame.display.set_mode(consts.WINDOW_SIZE)   # 显示窗口


    #鼠标位置
    mouse_position = (0,0)
    while True:
        #限定帧率为60帧
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            #键盘操作
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.add_speed((0,-1))
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.add_speed((1,0))
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.add_speed((0,1))
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.add_speed((-1,0))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.add_speed((0, 1))
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.add_speed((-1, 0))
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.add_speed((0, -1))
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.add_speed((1, 0))
                    
            # #鼠标操作
            if event.type == pygame.MOUSEMOTION:
                if event.buttons[0] == 1:
                    mouse_position = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_position = event.pos
                    player.is_shoot = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    player.is_shoot = False

        update()

