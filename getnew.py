import requests
import csv
import time
from config import *

class get_middlehigh_region(object):
    """
    获取中高风险地区数据并存储为csv文件
    """
    def __init__(self):
        pass

    def get_data(self):
        '''
        获取中高风险地区数据
        '''
        # 执行api调用并存储响应
        r = requests.get(url)
        # 将api响应存储在变量中
        response_dict = r.json() 
        '''
        print(response_dict ['data'])
        print("-------------")
        print("-------------")
        print("-------------")
        print("-------------")
        '''
        dicts = response_dict ['data']
        update_time = dicts['dateline']
        city_maps= dicts['map']
        #print(city_maps)
        '''
        print("-------------")
        print("-------------")
        print("-------------")
        print("-------------")
        '''
        count = dicts['count']
    

        for item in update_time:
            print('风险地区%s更新时间：%s'%(str(item),str(update_time[item])))
        results = []
        for item in city_maps:
            for item1 in item:
                for item2 in city_maps[item1]:
                    # print('风险地区:%s,省：%s,具体位置：%s'%(str(item),str(item2),str((city_maps[item1][item2]['city']+city_maps[item1][item2]['addr']))))
                    # print(city_maps[item1][item2])
                    areas =city_maps[item1][item2]
                    for area_item in areas:
                        result = []
                        result_selected=[]
                        grade = str(area_item['grade'])
                        if grade == '1':
                            result.append('中风险')
                            #result.append('1')
                        if grade == '2':
                            result.append('高风险')
                            #result.append('2')
                        result.append(str(item2))
                        result.append(str(area_item['city']+'市'+area_item['addr']))
                         #筛选地区
                        if area_item['province'].find('北京') !=-1 or area_item['province'].find('重庆') !=-1 or area_item['province'].find('天津') !=-1 or area_item['province'].find('上海') !=-1:
                            if area_item['addr'].find('市') !=-1:
                                area_select=area_item['province']+'市'+area_item['city']+area_item['addr'][:area_item['addr'].find('市')+1]
                            elif area_item['addr'].find('区') !=-1:
                                area_select=area_item['province']+'市'+area_item['city']+area_item['addr'][:area_item['addr'].find('区')+1]
                            elif area_item['addr'].find('县') !=-1:
                                area_select=area_item['province']+'市'+area_item['city']+area_item['addr'][:area_item['addr'].find('县')+1]
                            else:
                                area_select=area_item['province']+'市'+area_item['city']+area_item['addr']
                        else:
                            if area_item['addr'].find('市') !=-1:
                                area_select= area_item['city']+'市'+area_item['addr'][:area_item['addr'].find('市')+1]
                            elif area_item['addr'].find('区') !=-1:
                                area_select=area_item['city']+'市'+area_item['addr'][:area_item['addr'].find('区')+1]
                            elif area_item['addr'].find('县') !=-1:
                                area_select=area_item['city']+'市'+area_item['addr'][:area_item['addr'].find('县')+1]
                            elif area_item['addr'].find('开发区') !=-1:
                                area_select=area_item['city']+'市'+area_item['addr'][:area_item['addr'].find('开发区')+3]
                            elif area_item['addr'].find('旗') !=-1:
                                area_select=area_item['city']+'市'+area_item['addr'][:area_item['addr'].find('旗')+1]
                            else:
                                area_select=area_item['city']+'市'+area_item['addr']
                        #二轮筛查
                        if area_select.find('县') != -1:
                            area_select = area_select[:area_select.find('县') + 1]
                        if area_select.find('区') != -1:
                            area_select = area_select[:area_select.find('区') + 1]
                        if area_select.find('旗') != -1:
                            area_select = area_select[:area_select.find('旗') + 1]
            # 挑选出直接市下面就是镇的情况
                        if area_select.find('镇') != -1:
                            area_select = area_select[:area_select.find('镇') + 1]
                        result_selected.append(area_select)
                        result.append(area_select)
                        results.append(result)
                        '''
                        for re1 in results:
                                reix+=1
                                print(reix)
                                print(re1[1])
                                if reix == 3:
                                    break
                        '''
        # 优化因最后一行没有出现风险地区的数据
        results[-1] = [results[-2][0], results[-1][0], results[-1][1]]
        print(results[-1])
        area_result1=results[-1]
        area_result2=area_result1[2]
        print(area_result2)
        acount=0
        alocate=0
        for areacount in area_result2:
            if areacount.find('市') !=-1:
                acount+=1
                alocate=areacount.find('市')
            #print(acount)         
        if area_result1[1].find('北京') !=-1 or  area_result1[1].find('重庆') !=-1 or  area_result1[1].find('天津') !=-1 or  area_result1[1].find('上海') !=-1:
            if acount > 1:
                area_result3= area_result2[:alocate+1]
            elif area_result2.find('区') !=-1:
                 area_result3=area_result2[:area_result2.find('区')+1]
            elif area_result2.find('县') !=-1:
                 area_result3=area_result2[:area_result2.find('县')+1]
            else:
                 area_result3=area_result2
        else:
            if acount >1:
                area_result3= area_result2[:alocate+1]
            elif area_result2.find('区') !=-1:
                 area_result3=area_result2[:area_result2.find('区')+1]
            elif area_result2.find('县') !=-1:
                 area_result3=area_result2[:area_result2.find('县')+1]
            elif area_result2.find('开发区') !=-1:
                 area_result3=area_result2[:area_result2.find('开发区')+3]
            elif area_result2.find('旗') !=-1:
                 area_result3=area_result2[:area_result2.find('旗')+1]
            else:
                 area_result3=area_result2
        #二轮筛查
        if  area_result3.find('县') != -1:
             area_result3 =  area_result3[: area_result3.find('县') + 1]
        if  area_result3.find('区') != -1:
             area_result3 =  area_result3[: area_result3.find('区') + 1]
        if  area_result3.find('旗') != -1:
             area_result3 =  area_result3[: area_result3.find('旗') + 1]
            # 挑选出直接市下面就是镇的情况
        if  area_result3.find('镇') != -1:
             area_result3 =  area_result3[: area_result3.find('镇') + 1]
        results[-1].append(area_result3)
        return results

    def save_data(self):
        '''
        将获取中高风险地区数据存储为csv文件
        '''
        # 获取数据
        data = self.get_data()
        # 转为DataFrame格式
        data = pd.DataFrame(data, columns=["风险等级","地区", "区域","已筛选地区"])
        #print(data['风险等级'])
        '''
        print(data)
        for data1 in data:
            for data2 in data[data1]:
                 print(data2)
        
        datat=data['grade2']
        print(datat)
        '''        
        # 存储数据
        data.to_csv(csv_url, index=False, encoding='utf-8')
        print(data)
        return data