import csv
# https://cuiqingcai.com/5571.html
# 如果不指定路径,默认保存在此模块的路径中
# 如果该csv没有  就创建此CSV文件
with open("data.csv","w") as csvfile:
    writer = csv.writer(csvfile)  # 初始化写入对象
    # writer = csv.writer(csvfile)  # 初始化写入对象 文件以空格分隔
    writer.writerow(['id','name','age'])  # writerow方法会写入一行
    writer.writerow(['10001','Mike','20'])
    writer.writerow(['10002', 'Bob', '26'])
    # 可以用writerows方法同时写入多行  此时参数就需要为二维列表
    writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])