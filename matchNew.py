from config import *
from py2neo import *
from getNew import *
import pandas as pd
import xlrd as xd
class matchnew(object):
    '''
    将筛选后的地区数据与区域行政代码相匹配，存储匹配后的数据到.csv文件
    ''' 
    def __init__(self):
        pass

    def matchdatanew(self):
        #读取xlsx文件中的数据
        sd1 = pd.read_excel('全国行政(1)(1)(1).xlsx',sheet_name='区县')
        sd2 = pd.read_excel('全国行政(1)(1)(1).xlsx',sheet_name='地市')
        sd3 = pd.read_excel('全国行政(1)(1)(1).xlsx',sheet_name='省州')
        '''
        print("获取到区县所有的值:\n{}".format(data1))
        print("获取到地市所有的值:\n{}".format(data2))
        print("获取到省州所有的值:\n{}".format(data3))
        '''
        #print("sheet3行数为：")
        #获取sheet行数
        #print(len(sd3.index.values))
        #获取sheet列数
        #print("sheet3列数为：")
        #print(len(sd3.columns.values))
        #读取筛选后地区数据
        data =  pd.read_csv(screen_csv_url,engine='python',encoding='utf-8')
        #获取有效数据行数
        sc0=len(data.index.values)
        print(sc0)
        sc01=sc0-1
        #print(data)
        area_sc=data['地区']
        area_sc21=data['已筛选地区']
        print(area_sc21[0])
        #用于存储匹配后的省洲代码
        area_code=[]
        #存储匹配后的地市代码
        area_codecity=[]
        #存储匹配后的区县代码
        area_codearea=[]
        #省洲列表数据下标
        xe1=1
        ye1=2
        #地市列表数据下标
        xe2=1
        ye2=2
        #区县列表数据下标
        xe3=1
        ye3=2
        #筛选后地区数据下标
        sc2=0
        #用于判断3级匹配是否成功
        areacount=-1
        for area_sc3 in area_sc:
            print("地区")
            #用于判断是否已找到与之对应匹配的代码
            area_flag=0
            area_flag2=0
            area_flag3=0
            #循环遍历，判断是否存在与地区匹配的省洲级代码
            while xe1 < len(sd3.index.values) and area_flag!=1:
                    #获取省洲级代码对应的地区名
                    data11 = sd3.iloc[xe1, ye1]
                    #print(data11)
                    #判断地区名是否相匹配
                    if area_sc3.find(data11)!=-1:
                        print(data11)
                        #匹配成功，存入地区名对应的省级代码
                        data12=sd3.iloc[xe1,1]
                        area_code.append(data12)
                        area_flag=1
                        print("--------------")
                        print("匹配成功")
                        print(data12)
                        #循环遍历，判断是否存在与地区匹配的地市级代码
                        while xe2 < len(sd2.index.values) and area_flag2!=1:
                                 #获取地市级代码对应的地区名
                                data21=sd2.iloc[xe2,ye2]
                                area_data21=str(data21)
                                area_data12=str(data12)
                                #获取地市级代码对应的地区名的省级代码
                                data22=sd2.iloc[xe2,3]
                                area_sc22=str(data22)
                                area_sc221=str(area_sc21[sc2])
                                #判断地区名及其上级省洲代码是否与1级匹配中相同
                                if area_sc221.find(area_data21)!=-1 and area_data12.find(area_sc22)!=-1:
                                    data222=sd2.iloc[xe2,1]
                                    print("--------------")
                                    print("匹配2级成功")
                                    print(area_sc221)
                                    print(data222)
                                    area_codecity.append(data222)
                                    #print("--------------")
                                    area_flag2=1
                                    area_sc222=str(data222)
                                    ##循环遍历，判断是否存在与区县匹配的地市级代码
                                    while xe3 < len(sd1.index.values) and area_flag3!=1:
                                            data32=sd1.iloc[xe3,ye3]
                                            data33=sd1.iloc[xe3,3]
                                            area_sc32=str(data32)
                                            area_sc33=str(data33) 
                                            #判断地区名及其上级地市代码是否与2级匹配中相同
                                            if area_sc221.find(area_sc32)!=-1 and area_sc222.find(area_sc33)!=-1:
                                                data333=sd1.iloc[xe3,1]
                                                #print("--------------")
                                                print("匹配3级成功")
                                                areacount+=1
                                                print(areacount)
                                                area_codearea.append(data333)
                                                #print(area_sc221)
                                                print(data333)
                                                #print("--------------")
                                                area_flag3=1
                                            xe3+=1
                                            if xe3 == len(sd1.index.values) and area_flag3!=1:
                                                area_codearea.append('未收录')
                                xe2+=1
                        
                    xe1+=1
            #print(xe1)
            print(sc2)      
            xe1=0
            xe2=0
            xe3=0
            #不超过有效数据行数
            if sc2!=sc01:
                sc2+=1
        
            #print()

        data['省洲代码']=area_code
        data['地市代码']=area_codecity
        data['区县代码']=area_codearea
        data = pd.DataFrame(data, columns=["风险等级","地区", "区域", "已筛选地区", "省洲代码",'地市代码','区县代码'])
        #print(data)
        #将完成匹配的筛选后地区数据写入CSV文件
        data.to_csv(screen_csv_url, index=False, encoding='utf-8')
        return data
        #print(data33)

#  列索引
#print(sd3.columns.values)
'''
data1=xd.open_workbook('全国行政(1)(1)(1).xlsx')
sh = data1.sheet_by_name('区县')
print(sh.cell(0,0).value)
'''


 