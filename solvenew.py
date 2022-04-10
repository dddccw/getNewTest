from config import *
from py2neo import *
from getnew import *
from matchnew import *
import pandas as pd

class screen_area_data(object):
    '''
        用于筛选爬虫获取到的中高风险地区数据
    '''
    def __init__(self):
        pass
    
    def screen_area_data(self):
        area_data0 =get_middlehigh_region()
        area_data1=area_data0.save_data()
        return area_data1
    
    def get_matchnewdata(self):
        area_getmatch=matchnew()
        area_getmatch1=area_getmatch.matchdatanew()
        return area_getmatch1
        
    def remove_duplicate_data(self):
        '''
        去除掉重复的数据
        规则： 如果重复出现就删除，且出现地区既是高风险，也是中风险地区时，则直接默认为高风险
        执行代码匹配
        将完成匹配的筛选后数据写入neo4j数据库
        '''
        # print(area_data.sort_values(by='风险等级', ascending=False))
        # 获取数据
       
        # 对风险地区按照高风险到中风险排序
        area_data=self.screen_area_data()
        area_data = area_data.sort_values(by='风险等级', ascending=False)
        area_data = area_data.drop_duplicates(subset=['已筛选地区'],keep='first')
        area_data.index = range(len(area_data))
        #print(area_data)
        #向csv文件存入筛选后的地区数据
        area_data.to_csv(screen_csv_url, index=False, encoding='utf-8-sig')
        #将筛选后的地区数据与各级区域代码进行匹配
        area_data12=self.get_matchnewdata()
        print("-----------分割线-------------")
        print(area_data12)
        #将输入存入NEO4J数据库实现可视化
        graph = Graph("http://localhost:7474", auth=("neo4j", "1138891146"))
        graph.delete_all()
        #按风险等级创建两个结点
        p1 = Node("grade", name="高风险")
        p2 = Node("grade", name="中风险")
        graph.create(p1)
        graph.create(p2)
        area_data2=area_data12['风险等级']
        print(area_data2)
        icount=-1
        for area_neo in area_data2:
            print(area_neo)
            icount+=1
            print(icount)
            grade22=str(area_neo)
            #获取区域数据
            area22=area_data12['区域'][icount]
            #获取地区数据
            area21=area_data12['地区'][icount]
            #获取已筛选地区数据
            area23=area_data12['已筛选地区'][icount]
            #获取区县代码数据
            areacode1=str(area_data12['区县代码'][icount])
            #获取地市代码数据
            areacode2=str(area_data12['地市代码'][icount])
            #获取省洲代码数据
            areacode3=str(area_data12['省洲代码'][icount])
            #print(area22)
            #print(area23)
            #判断是否已存在同名同类结点
            matcher = NodeMatcher(graph)
            nodelisth=list(matcher.match("wildareah",name=area21))
            nodelistm=list(matcher.match("wildaream",name=area21))
            nodelisth2=list(matcher.match("bigareah",name=area23))
            nodelistm2=list(matcher.match("bigaream",name=area23))
            if  grade22 == '高风险':
                #当相同区域与地区结点均已存在时
                if  len(nodelisth2) and len(nodelisth):
                    ph2 = Node("specificareah", name=area22)
                    graph.create(ph2)
                    nodelisth2_to_ph2= Relationship(nodelisth2[0], "关联", ph2)
                    graph.create(nodelisth2_to_ph2)
                #当地区结点已存在时
                elif  len(nodelisth):
                    ph3= Node("bigareah",name=area23)
                    graph.create(ph3)
                    nodelisth_to_ph3= Relationship(nodelisth[0],"关联",ph3)
                    graph.create(nodelisth_to_ph3)
                    phcode2= Node("citycode1",name=areacode2)
                    graph.create(phcode2)
                    ph3_to_phcode2= Relationship(ph3,"关联",phcode2)
                    graph.create(ph3_to_phcode2)
                    phcode1= Node("areacode1",name=areacode1)
                    graph.create(phcode1)
                    phcode2_to_phcode1= Relationship(phcode2,"关联",phcode1)
                    graph.create(phcode2_to_phcode1)
                    ph2 = Node("specificareah", name=area22)
                    graph.create(ph2)
                    ph3_to_ph2= Relationship(ph3, "关联", ph2)
                    graph.create( ph3_to_ph2)    
                else:  
                    ph1=Node("wildareah",name=area21)
                    graph.create(ph1)
                    p1_to_ph1=Relationship(p1,"关联",ph1)
                    graph.create(p1_to_ph1)
                    phcode3=Node("provincecode1",name=areacode3)
                    graph.create(phcode3)
                    ph1_to_phcode3=Relationship(ph1,"关联",phcode3)
                    graph.create(ph1_to_phcode3)
                    ph3= Node("bigareah",name=area23)
                    graph.create(ph3)
                    p1_to_ph3= Relationship(ph1,"关联",ph3)
                    graph.create(p1_to_ph3)
                    phcode2= Node("citycode1",name=areacode2)
                    graph.create(phcode2)
                    ph3_to_phcode2= Relationship(ph3,"关联",phcode2)
                    graph.create(ph3_to_phcode2)
                    phcode1= Node("areacode1",name=areacode1)
                    graph.create(phcode1)
                    phcode2_to_phcode1= Relationship(phcode2,"关联",phcode1)
                    graph.create(phcode2_to_phcode1)
                    ph2 = Node("specificareah", name=area22)
                    graph.create(ph2)
                    ph3_to_ph2= Relationship(ph3, "关联", ph2)
                    graph.create(ph3_to_ph2)
            elif grade22 == '中风险':
                 #当相同区域与地区结点均已存在时
                if  len(nodelistm2) and len(nodelistm):
                    pm2 = Node("specificaream", name=area22)
                    graph.create(pm2)
                    nodelistm2_to_pm2= Relationship(nodelistm2[0], "关联", pm2)
                    graph.create(nodelistm2_to_pm2)
                #当地区结点已存在时
                elif  len(nodelistm):
                    pm3= Node("bigaream",name=area23)
                    graph.create(pm3)
                    nodelistm_to_pm3= Relationship(nodelistm[0],"关联",pm3)
                    graph.create(nodelistm_to_pm3)
                    pmcode2= Node("citycode2",name=areacode2)
                    graph.create(pmcode2)
                    pm3_to_pmcode2= Relationship(pm3,"关联",pmcode2)
                    graph.create(pm3_to_pmcode2)
                    pmcode1= Node("areacode2",name=areacode1)
                    graph.create(pmcode1)
                    pmcode2_to_pmcode1= Relationship(pmcode2,"关联",pmcode1)
                    graph.create(pmcode2_to_pmcode1)
                    pm2 = Node("specificaream", name=area22)
                    graph.create(pm2)
                    pm3_to_pm2= Relationship(pm3, "关联", pm2)
                    graph.create( pm3_to_pm2)    
                else:  
                    pm1=Node("wildaream",name=area21)
                    graph.create(pm1)
                    p2_to_pm1=Relationship(p2,"关联",pm1)
                    graph.create(p2_to_pm1)
                    pmcode3=Node("provincecode2",name=areacode3)
                    graph.create(pmcode3)
                    pm1_to_pmcode3=Relationship(pm1,"关联",pmcode3)
                    graph.create(pm1_to_pmcode3)
                    pm3= Node("bigaream",name=area23)
                    graph.create(pm3)
                    p2_to_pm3= Relationship(pm1,"关联",pm3)
                    graph.create(p2_to_pm3)
                    pmcode2= Node("citycode2",name=areacode2)
                    graph.create(pmcode2)
                    pm3_to_pmcode2= Relationship(pm3,"关联",pmcode2)
                    graph.create(pm3_to_pmcode2)
                    pmcode1= Node("areacode2",name=areacode1)
                    graph.create(pmcode1)
                    pmcode2_to_pmcode1= Relationship(pmcode2,"关联",pmcode1)
                    graph.create(pmcode2_to_pmcode1)
                    pm2 = Node("specificaream", name=area22)
                    graph.create(pm2)
                    pm3_to_pm2= Relationship(pm3, "关联", pm2)
                    graph.create(pm3_to_pm2)
            else:
                print(grade22)
        
        