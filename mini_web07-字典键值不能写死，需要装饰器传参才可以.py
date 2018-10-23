# 一个函数一个功能
# 函数的入口需要简洁
url_dict = dict()
def set_url(url):  # 把地址url传参进去
    def set_fun(func):
        def call_fun(*args,**kwargs):
            return func(*args,**kwargs)
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
        print('异常',e)
        response_line = 'HTTP /1.1 404 NOT FOUND\r\n'
        response_body = '页面丢失'

    if request_url == '/index.html':
        response_body = index()

    elif request_url == '/center.html':
        response_body = center()
        # 拼接响应报文内容

    elif request_url == '/login.html':

        response_body = login()
    elif request_url == '/abc.html':
        response_body = abc()

    elif request_url == '/post.html':
        response_body = post()

    else:
        # 没有找到页面
        response_line = 'HTTP /1.1 404 NOT FOUND\r\n'
        response_body = '页面丢失'
    return response_line, response_header,response_body
    # 函数需要有返回值才可以的

@set_url('/index.html')
def index():
    response_body = "主页界面"

    return response_body


def post():
    with open('./post.html', 'r') as f:
        content = f.read()
    response_body = content
    return response_body


def abc():
    response_body = 'abc is show'
    return response_body


def login():
    response_body = '登录界面'
    return response_body


def center():
    response_body = '个人中心界面'
    return response_body