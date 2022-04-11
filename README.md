# getNewTest
自动化定时获取疫情数据并筛选，匹配区域代码，最终存入neo4j数据库
## getNew.py
获取疫情数据，并筛选地区，存入疫情数据.csv文件
##  solveNew.py
对疫情数据.csv文件进行重复数据筛选，存入筛选后的地区数据.csv文件，并通过matchNew.py执行代码匹配功能，最终将数据存入neo4j数据库
##  matchNew.py
获取筛选后的地区数据.csv文件的数据，并与区域代码进行匹配，将匹配后的数据再次写入筛选后的地区数据.csv文件供solveNew.py使用
## getNewTest.py
作为main函数执行
