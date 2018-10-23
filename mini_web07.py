# 一个函数一个功能
# 函数的入口需要简洁
import re

from pymysql import connect

url_dict = dict()


def set_url(url):
    def set_fun(func):
        def call_fun(*args, **kwargs):
            return func(*args, **kwargs)

        print(call_fun)
        url_dict[url] = call_fun
        # 字典的键值不能写死，需要传参才更加合适
        return call_fun

    return set_fun


def appliction(request_url):
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
    # 响应头
    response_header = "Content-Type: text/html;charset=utf-8\r\n"
    # if 大于三个就要考虑使用字典--根据url来获取到函数，也就是键值对
    # url_dict = {'/index.html':index,'/post.html':post}
    # 如果不在字典里面需要捕获异常
    try:
        fun = url_dict[request_url]  # 通过键来返回函数，然后响应报文就是函数执行的结果
        response_body = fun()
    except Exception as e:
        print('异常')
        response_line = 'HTTP /1.1 404 NOT FOUND\r\n'
        response_body = '页面丢失'

    return response_line, response_header, response_body
    # 函数需要有返回值才可以的


###################上面属性框架##############

@set_url('/index.html')
def index():
    # 打开前端网页内容
    with open('./templates/index.html', 'r') as f1:
        content = f1.read()
    row_str = '''<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000036">
        </td>
        </tr>"""
    '''
    # 链接数据库
    # 数据库
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='stock_db', charset='utf8')
    # 获取游标
    cs = conn.cursor()

    # 执行sql
    sql = '''select * from info;
'''
    cs.execute(sql)
    # 获取数据
    data = cs.fetchall()
    # 关闭
    cs.close()
    conn.close()
    # 把数据库的内容一行一行的放进去
    table_str = ''
    for temp1 in data:
        table_str += row_str %(temp1[0],temp1[1],temp1[2],temp1[3],temp1[4],temp1[5],temp1[6],temp1[7])

    # 内容替换
    content = re.sub(r'\{%content%\}', table_str, content)
    return content

# @set_url('/post.html')
# def post():
#     with open('./post.html', 'r') as f:
#         content = f.read()
#
#     response_body = content
#     return response_body
#
#
# @set_url('/abc.html')
# def abc():
#     response_body = 'abc is show'
#     return response_body
#
#
# @set_url('/login.html')
# def login():
#     response_body = '登录界面'
#     return response_body
#
#
@set_url('/center.html')
def center():
    # 打开前端网页内容
    with open('./templates/center.html') as f1:
        content = f1.read()

    # 链接数据库
    # 数据库
    conn = connect(host='localhost', port=3306, user='root', password='mysql', database='stock_db', charset='utf8')
    # 获取游标
    cs = conn.cursor()
    sql = '''select info.code, info.short, info.chg, info.turnover,info.price, info.highs,
focus.note_info from info inner join focus on info.id = focus.info_id;'''

    cs.execute(sql)
    # 获取到数据
    data = cs.fetchall()
    # 关闭
    cs.close()
    conn.close()
    row_str = """<tr>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>
                   <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
               </td>
               <td>
                   <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="300268">
               </td>
           </tr>"""
    # 处理数据
    table_str = ''
    for temp in data:
        table_str += row_str%(temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6])
    content = re.sub(r'{%content%\}',table_str,content)

    return content
