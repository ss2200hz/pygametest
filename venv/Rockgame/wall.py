from Rockgame import physics,consts,tools

class Wall(physics.Transform):
    def __init__(self,position,size):
        super(Wall,self).__init__(position=position,rect_size=size)
        self.is_can_destroy = False
        self.is_destroed = False

    def set_speed(self):
        pass

    def move(self):
        pass

    def on_colliderect(self,_obj=None):
        pass