import re
import socket


# 创建一个tcp服务器套接字
# 绑定地址
# 设置监听模式
# 获取客户端的链接
# 　和客户端发送消息(发送响应)
def client_exec(client):
    request_data = client.recv(1024).decode('utf-8')
    print(request_data)
    match = re.match(r'[^/]+(/[^ ]*)', request_data).group(1)
    # 对正则数据进行判断是否匹配
    request_url = ''
    if match :
        # 匹配到了数据
        request_url = match
        print('当前路径', request_url)
        if request_url == '/':
            request_url = 'index.html'
    else:
    #直接关闭客户端
        client.close()

    if request_url == '/index.html':
        response_line = "HTTP/1.1 200 OK\r\n"
        # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
        response_header = "Content-Type: text/html;charset=utf-8\r\n"
        response_body = "主页界面"
        response_content = response_line + response_header + "\r\n" + response_body
        # 发送响应报文数据
        client.send ( response_content.encode("utf-8"))

    elif request_url == '/center.html':
        response_line = "HTTP/1.1 200 OK\r\n"
        # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
        response_header = "Content-Type: text/html;charset=utf-8\r\n"
        response_body = '个人中心界面'

        # 拼接响应报文内容
        response_content = response_line + response_header + "\r\n" + response_body
        # 发送响应报文数据
        client.send(response_content.encode("utf-8"))
    elif request_url == '/login.html':
        response_line = "HTTP/1.1 200 OK\r\n"
        # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
        response_header = "Content-Type: text/html;charset=utf-8\r\n"
        response_body = '登录界面'

        # 拼接响应报文内容
        response_content = response_line + response_header + "\r\n" + response_body
        # 发送响应报文数据
        client.send(response_content.encode("utf-8"))
    else:
        response_line = "HTTP/1.1 404 not found\r\n"
        # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
        response_header = "Content-Type: text/html;charset=utf-8\r\n"
        response_body = '页面已经丢失'

        # 拼接响应报文内容
        response_content = response_line + response_header + "\r\n" + response_body
        # 发送响应报文数据
        client.send(response_content.encode("utf-8"))

    client.close()


def main():
    '''创建一个tcp服务器'''
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    # 绑定端口 # 设置监听模式 # 端口复用
    tcp_server_socket.bind(('', 1315))
    tcp_server_socket.listen(128)
    # 和客户端浏览器进行链接，接收客户端信息# 接收客户端请求报文
    while True:
        # 获取客户端链接
        client, addr = tcp_server_socket.accept()
        # 处理请求
        client_exec(client)

    # 从请求报文里面正则获取到路径－－request_url
    # 关闭服务器套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()