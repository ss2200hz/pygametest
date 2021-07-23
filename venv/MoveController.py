import Room,Road,Player,Consts

#判断玩家是否可移动
def isPlayerCanMove(moveDirection,roadList,player):
    if player == None:
        raise "找不到角色"
    isRoad = False
    isNotEdge = False
    x = player.roomCoor[0]
    y = player.roomCoor[1]
    if moveDirection == Consts.UP_DIRECTION:
        nextRoom = (x,y-1)
        if player.roomCoor[1] > Consts.HIGHT_MIN_NO:
            isNotEdge = True
    elif moveDirection == Consts.DOWN_DIRECTION:
        nextRoom = (x, y + 1)
        if player.roomCoor[1] < Consts.WEIGHT_MAX_NO:
            isNotEdge = True
    elif moveDirection == Consts.LEFT_DIRECTION:
        nextRoom = (x - 1, y)
        if player.roomCoor[0] > Consts.WEIGHT_MIN_NO:
            isNotEdge = True
    elif moveDirection == Consts.RIGHT_DIRECTION:
        nextRoom = (x + 1, y)
        if player.roomCoor[0] < Consts.WEIGHT_MAX_NO:
            isNotEdge = True
    for road in roadList:
        if player.roomCoor in road.linkedRooms and nextRoom in road.linkedRooms:
            isRoad = True
            break
    # print(str(isRoad) +" "+ str(isNotEdge))
    return isRoad and isNotEdge #具有道路且不在边界方可移动

#移动角色
def moveCharacter(character,direction):
    if direction == Consts.UP_DIRECTION:
            character.roomCoor = (character.roomCoor[0], character.roomCoor[1] - 1)
    elif direction == Consts.DOWN_DIRECTION:
            character.roomCoor = (character.roomCoor[0], character.roomCoor[1] + 1)
    elif direction == Consts.LEFT_DIRECTION:
            character.roomCoor = (character.roomCoor[0] - 1, character.roomCoor[1])
    elif direction == Consts.RIGHT_DIRECTION:
            character.roomCoor = (character.roomCoor[0] + 1, character.roomCoor[1])