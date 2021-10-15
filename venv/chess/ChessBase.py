class ChessBase:
    def __init__(self,id,position,movePoint):
        #移动状态
        self.isPickUp = False
        #是否移动过
        self.isMoved = False
        #移动点数，用于控制移动的距离
        self.movePoint = movePoint
        pass
