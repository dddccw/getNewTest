from getnew import *
from solvenew import *
from py2neo import *
import pandas as pd
import time
def main():
    '''
    1、获取、筛选，存储疫情地区数据
    2、排序、筛选重复的疫情地区数据，存储筛选后的地区数据
    3、匹配市区编码
    4、导入neo4j数据库实现可视化存储
    5、实现定时自动执行
    '''
    # # 1、获取、存储疫情地区数据
    #do_get_middlehigh_region = get_middlehigh_region()
    #do_get_middlehigh_region.save_data()

    # 2、筛选、存储筛选后的疫情地区数据
    
    #target_time = time.mktime(time.strptime("2022-4-8 14:29", "%Y-%m-%d %H:%M"))
    #获取当前0时区时间
    timet1=time.gmtime()
    #获取当前0时区小时数值
    t1h=timet1.tm_hour+8
    #获取当前0时区的分钟数值
    t1m=timet1.tm_min
    #设置运行时间
    t1hflag=12
    t1mflag=30
    t2hflag=24
    t2mflag=39
    print(t1h)
    print(t1m)
    while True :   
        timet1=time.gmtime()
        t1h=timet1.tm_hour+8
        t1m=timet1.tm_min
        #判断是否已达到执行时间
        if t1h==t1hflag and t1m == t1mflag:
           print(u"到点执行")
           do_screen_area_data = screen_area_data()
           do_screen_area_data.remove_duplicate_data()
        #每次满足执行规定时间时，只执行一次代码   
           time.sleep(61)
        elif t1h==t2hflag and t1m ==t2mflag:
           print(u"到点执行")
           do_screen_area_data = screen_area_data()
           do_screen_area_data.remove_duplicate_data()
           time.sleep(61)
    #do_screen_area_data = screen_area_data()
    #do_screen_area_data.remove_duplicate_data()
   

if __name__ == '__main__':
    main()