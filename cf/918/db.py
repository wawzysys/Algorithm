import pymysql
import time
# 连接到MySQL数据库
connection = pymysql.connect(host='localhost', user='root', password='wawzysys', db='BookStore')
try:
    with connection.cursor() as cursor:
        query = "SELECT * FROM Books WHERE Author = 'Stephen King'"

        # 记录开始时间
        start_time = time.time()

        # 执行查询1000次
        for _ in range(1000):
            cursor.execute(query)

        # 记录结束时间
        end_time = time.time()

    # 打印总执行时间
    print(f"Total execution time for 1000 queries: {end_time - start_time} seconds")
finally:
    connection.close()
