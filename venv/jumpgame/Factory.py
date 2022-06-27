from jumpgame import player,world
#可视化对象创建工厂
class VisualObjectFactory:
    def create_object(self,obj_type):
        if obj_type == "player":
            obj = player.Player(100,100)
            #根据传参创建对象并添加进对象列表中
            world.visual_object_list.append(obj)
            return obj