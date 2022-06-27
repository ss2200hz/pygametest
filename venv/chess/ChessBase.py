class ChessBase:
    def __init__(self,id,position,movePoint):
        #拿起状态
        self.isPickedUp = False
        #是否移动过
        self.isMoved = False
        #移动点数，用于控制移动的距离
        self.movePoint = movePoint
        pass

    #更新棋子状态
    def chessUpdate(self):
        if not self.isPickedUp:
            self.pic_dir = pygame.image.load(Consts.IMG_DIR + "player.png")
        else:
            self.pic_dir = pygame.image.load(Consts.IMG_DIR + "chesspicked.png")

    def moveChess(self):
        pass
