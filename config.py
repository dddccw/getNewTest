# 直辖市名单
city_list_2 = ['北京', '天津', '重庆', '上海']
# 获取数据来源，数据来源市该来源的json文件地址
url = 'https://m.sm.cn/api/rest?format=json&method=Huoshenshan.riskArea&_=1628665447912'
# 疫情数据表单名称
csv_url = '疫情数据.csv'
# 筛选完成后的疫情数据表单名称
screen_csv_url = '筛选后的地区数据.csv'

# 导入重复的包
import pandas as pd
