import json
import openpyxl
import os
import consts

#初始化配置
def init_config():
    config_path = "config.json"
    with open(config_path,'r') as file:
        config_data = json.load(file)
    return config_data

config_data = init_config()

#格子坐标向像素值转换
def position_to_coor(position,grid_x,grid_y):
    pos_x = position[0]
    pos_y = position[1]
    x = (pos_x - 1) * consts.GRID_WIDTH + pos_x * consts.INTERVAL
    y = (pos_y - 1) * consts.GRID_HIGH + pos_y * consts.INTERVAL

    grid_full_x = consts.GRID_WIDTH * grid_x + (grid_x + 1) * consts.INTERVAL
    grid_full_y = consts.GRID_HIGH * grid_y + (grid_y + 1) * consts.INTERVAL
    coor_x = x + (consts.WINDOW_WIDTH - grid_full_x) / 2
    coor_y = y + (consts.WINDOW_HIGH - grid_full_y) / 2
    return int(coor_x),int(coor_y)

#数字坐标转换像素值
def number_position_to_coor(position,grid_x,grid_y):
    pos_x = position[0]
    pos_y = position[1]
    x = (pos_x - 1) * consts.GRID_WIDTH + pos_x * consts.INTERVAL
    y = (pos_y - 1) * consts.GRID_HIGH + pos_y * consts.INTERVAL

    grid_full_x = consts.GRID_WIDTH * grid_x + (grid_x + 1) * consts.INTERVAL
    grid_full_y = consts.GRID_HIGH * grid_y + (grid_y + 1) * consts.INTERVAL
    coor_x = x + (consts.WINDOW_WIDTH - grid_full_x) / 2
    coor_y = y + (consts.WINDOW_HIGH - grid_full_y) / 2

    #美观起见，略微偏移一些
    return int(coor_x) + consts.FONT_OFFSET_X, int(coor_y) + consts.FONT_OFFSET_Y

#像素值向格子坐标转换
def coor_to_position(coor,grid_x,grid_y):
    grid_full_x = consts.GRID_WIDTH * grid_x + (grid_x + 1) * consts.INTERVAL
    grid_full_y = consts.GRID_HIGH * grid_y + (grid_y + 1) * consts.INTERVAL
    coor_x = coor[0]
    coor_y = coor[1]

    old_x = coor_x - (consts.WINDOW_WIDTH - grid_full_x) / 2
    old_y = coor_y - (consts.WINDOW_HIGH - grid_full_y) / 2

    x = old_x / (consts.GRID_WIDTH + consts.INTERVAL)
    y = old_y / (consts.GRID_HIGH + consts.INTERVAL)
    return int(x) + 1,int(y) + 1



#Excel工具
class ExcelTool:
    # 遍历目录下所有文件并返回excel文件list
    # def getFilesInPath(self,path="E:/configtable/0717/fns_config-master"):
    #     fileList = []
    #     for root, dir, files in os.walk(path):
    #         dir[:] = []  # 跳过子目录
    #         for name in files:
    #             if re.match(r'.+xlsx', name) or re.match(r'.+xls', name) and '$' not in name:
    #                 filePath = path + '/' + name
    #                 fileList.append(filePath)
    #     return fileList

    # 将文件转换结果保存为JSON
    def saveDataByJson(self,data, file, outputPath='E:/configtable/0717/test'):
        jsonData = json.dumps(obj=data, sort_keys=False, indent=4, ensure_ascii=False)
        fileName = os.path.basename(file).replace(".xlsx", ".json")
        with open(outputPath + "/" + fileName, "w", encoding='utf-8') as f:
            f.write(jsonData)

    # 获取文件中的所有sheet数据
    def getAllSheetData(self,file):
        try:
            workBook = openpyxl.open(file)
            resultList = []
            for sheet in workBook.sheetnames:
                # d = {'sheet_name': sheet.title()}
                d = {}
                # resultList.append({'sheet_name': sheet.title()})
                dataList = self.changeSheetData2Json(workBook[sheet])
                d['sheet_name'] = sheet.title()
                d['data'] = dataList
                resultList.append(d)
            return resultList
        except IOError as e:
            print("打开文件出错，文件名:" + file)
            raise e
        except Exception as e:
            raise e

    #转换sheet数据
    def changeSheetData2Json(self,sheet):
        try:
            resultList = []
            if sheet.max_row <= 0:
                return resultList
            rowList = list(sheet.rows)
            idRow = rowList[1]
            for i in range(2, len(rowList)):
                dataRow = rowList[i]
                dictValue = {}
                for j in range(0, len(dataRow)):
                    id = str(idRow[j].value) if idRow[j].value != None else ""
                    # print(dataRow[j].value)
                    dataValue = dataRow[j].value if dataRow[j].value != None else ""
                    dictValue[id] = dataValue
                resultList.append(dictValue.copy())
            return resultList
        except:
            print("处理表格出错，sheet名:" + sheet.title)

if __name__ == '__main__':
    excel_tool = ExcelTool()
    file_path = 'E:\\pytest\\game\\venv\\eyesexamgame\\config.xlsx'
    data = excel_tool.getAllSheetData(file=file_path)
    excel_tool.saveDataByJson(data=data,file=file_path,outputPath='E:\\pytest\\game\\venv\\eyesexamgame')