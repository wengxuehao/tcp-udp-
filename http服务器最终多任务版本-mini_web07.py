import re
import socket

import gevent

import mini_web07
from gevent import monkey

monkey.patch_all()


# 面向对象开发，一个函数一个功能


class Web_server(object):
    def client_exec(self, client):
        # 根据不同的请求地址返回不同的页面
        # １ 得到请求数据
        request_data = client.recv(1024).decode('utf-8')
        print(request_data)
        # ２ 通过正则进行筛选出资源路径 # 从请求报文里面正则获取到路径－－request_url
        match = re.match(r'[^/]+(/[^ ]*)', request_data)
        # 对正则数据进行判断是否匹配
        request_url = ''
        if match:
            # 匹配到了数据
            request_url = match.group(1)
            print('当前路径', request_url)
            if request_url == '/':
                request_url = 'index.html'
        else:
            # 直接关闭客户端
            client.close()
            # 如果是.html结尾的
        if request_url.endswith('.html'):
            response_line, response_header, response_body, = mini_web07.appliction(request_url)
            # 拼接响应报文内容
            response_content = response_line + response_header + "\r\n" + response_body
            # 发送响应报文数据
            client.send(response_content.encode("utf-8"))
        else:
            # 如果找不到资源，捕捉异常
            try:
                response_line = "HTTP/1.1 200 OK\r\n"
                # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
                response_header = ""
                with open('./static%s' % request_url, 'rb')as f:
                    content = f.read()
                response_body = content
                # 拼接响应报文内容
                response_content = response_line + response_header + "\r\n"
                # 发送响应报文数据
                client.send(response_content.encode("utf-8"))
                client.send(response_body)
            except Exception as e:
                print('异常', e)
                response_line = "HTTP/1.1 404 not found\r\n"
                # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
                response_header = "Content-Type: text/html;charset=utf-8\r\n"
                response_body = ''

                # 拼接响应报文内容
                response_content = response_line + response_header + "\r\n" + response_body
                # 发送响应报文数据

                client.send(response_content.encode("utf-8"))

        client.close()

    def run_server(self):
        while True:
            # 获取客户端链接
            client, addr = self.tcp_server.accept()
            # 和客户端浏览器进行链接，接收客户端信息# 接收客户端请求报文
            # 处理请求
            gevent.spawn(self.client_exec, client)
        tcp_server.close()

    def __init__(self):
        # 定义一个方法用来初始化服务器

        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 5)
        # 绑定端口 # 设置监听模式 # 端口复用
        self.tcp_server.bind(('', 1315))
        self.tcp_server.listen(128)
        # 返回tcp_server
        # return self.tcp_server


def main():
    # 初始化web服务器
    server = Web_server()

    # 初始化tcp

    # 开启服务
    server.run_server()

    # 关闭服务器套接字


if __name__ == '__main__':
    main()
