# 链接数据库
from pymysql import connect  # 数据库
conn = connect(host='localhost', port=3306, user='root', password='mysql', database='stock_db', charset='utf8')
    # 获取游标
cs = conn.cursor()
sql = '''
select info.code, info.short, info.chg, info.turnover,info.price, info.highs,
focus.note_info from info inner join focus on info.id = focus.info_id;'''
cs.execute(sql)
# 获取数据
data = cs.fetchall()
# 关闭
cs.close()
conn.close()
# 把数据库的内容一行一行的放进去
table_str = ''
for temp1 in data:
    # table_str += row_str %(temp1[0],temp1[1],temp1[2],temp1[3],temp1[4],temp1[5],temp1[6],temp1[7])
    print(temp1)