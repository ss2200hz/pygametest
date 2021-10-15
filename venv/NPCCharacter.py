import Consts
import Player
import pygame
#
class NpcCharacter(Player):
    def __init__(self):
        self.pic_dir = pygame.image.load(Consts.IMG_DIR + "player.png")
        self.roomCoor = (0,0)#所在room坐标编号
        self.playerRect = pygame.Rect(0, 0, 50, 50)