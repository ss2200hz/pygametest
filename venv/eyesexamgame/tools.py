import json
import openpyxl
import os

#初始化配置
def init_config():
    config_path = "config.json"
    with open(config_path,'r') as file:
        config_data = json.load(file)
    return config_data

config_data = init_config()

#根据格子数量计算分辨率
def get_window_size():
    width_num = config_data['width'] #横向数量
    high_num = config_data['high'] #纵向数量

    window_width = width_num * (grid_width + width_num + 1)
    window_high = high_num * (grid_high + high_num + 1)

    return window_width,window_high

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
    file_path = 'config.xlsx'
    list = excel_tool.getAllSheetData(file_path)
    excel_tool.saveDataByJson(data=list,file=file_path,outputPath='D:\\pytest\\game\\venv\\eyesexamgame\\test')