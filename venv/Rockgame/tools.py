import json
import openpyxl
import os
from Rockgame import consts

#初始化配置
def init_config():
    config_path = "config.json"
    with open(config_path,'r',encoding='utf-8') as file:
        config_data = json.load(file)
    return config_data

config_data = init_config()

def get_config_by_name(name):
    for d in config_data:
        if d['sheet_name'] == name:
            return d['data']
    raise 'Not Found Map config!'

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
        with open(outputPath + "\\" + fileName, "w", encoding='utf-8') as f:
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
            typeRow = rowList[1]
            idRow = rowList[2]
            for i in range(3, len(rowList)):
                dataRow = rowList[i]
                dictValue = {}
                for j in range(0, len(dataRow)):
                    id = str(idRow[j].value) if idRow[j].value != None else ""
                    # print(dataRow[j].value)
                    # if ',' in str(dataRow[j].value):
                    #     dataValue = str(dataRow[j].value).split(',')
                    # else:
                    #     dataValue = dataRow[j].value if dataRow[j].value != None else ""
                    dataValue = ''
                    if typeRow[j].value:
                        if typeRow[j].value == 'list':
                            dataValue = str(dataRow[j].value).split(',')
                            for i in range(0,len(dataValue)):
                                try:
                                    dataValue[i] = int(dataValue[i])
                                except Exception as e:
                                    print(e)
                                    continue
                        elif typeRow[j].value == 'int':
                            dataValue = int(dataRow[j].value)
                    else:
                        dataValue = dataRow[j].value
                    dictValue[id] = dataValue
                resultList.append(dictValue.copy())
            return resultList
        except Exception as e:
            print("处理表格出错，sheet名:" + sheet.title)
            print(e)

if __name__ == '__main__':
    excel_tool = ExcelTool()
    file_path = 'config.xlsx'
    data = excel_tool.getAllSheetData(file=file_path)
    excel_tool.saveDataByJson(data=data,file=file_path,outputPath='D:\\pytest\\game\\venv\\Rockgame')
    # excel_tool.saveDataByJson(data=data, file=file_path, outputPath='E:\\pytest\\game\\venv\\Rockgame')