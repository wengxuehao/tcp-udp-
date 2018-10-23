def appliction(request_url):
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
    # 响应头
    response_header = "Content-Type: text/html;charset=utf-8\r\n"
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