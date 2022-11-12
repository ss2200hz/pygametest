from Rockgame import physics

#气球爆炸后留下的痕迹
class BoomTrace(physics.Transform):
    def __init__(self,position,size):
        super(BoomTrace,self).__init__(position=position,rect_size=size)


    def set_speed(self):
        pass

    def move(self):
        pass

    def on_colliderect(self,_obj=None):
        pass