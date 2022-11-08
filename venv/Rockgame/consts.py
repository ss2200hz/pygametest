from enum import Enum
#素材路径
IMG_DIR = "..\\..\\imgs\\"

#窗口大小
WINDOW_SIZE = (800,600)

#角色图大小，暂时写死
PLAYER_IMG_SIZE = (50,50)

#gm开关
IS_TEST = True

#pygame字体
FONT_XINXIMINGTI = "PMingLiU" #新细明体
FONT_XIMINGTI = "MingLiU" #细明体：
FONT_BIAOKAITI = "DFKai-SB" #标楷体
FONT_HEITI = "SimHei" #黑体
FONT_SONGTI = "SimSun" #宋体
FONT_XINSONGTI = "NSimSun" #新宋体
FONT_FANGSONG = "FangSong" #仿宋
FONT_KAITI = "KaiTi" #楷体
FONT_FANGSONG_GB2312 = "FangSong_GB2312" #仿宋_GB2312
FONT_KAITI_GB2312 = "KaiTi_GB2312" #楷体_GB2312
FONT_MS_ZHENGHEI = "Microsoft JhengHei" #微软正黑体
FONT_MS_YAHEI = "Microsoft YaHei" #微软雅黑体

class GameObjectType(Enum):
    Player = 1
    Enemy = 2
    Wall = 3
    Bullet = 4