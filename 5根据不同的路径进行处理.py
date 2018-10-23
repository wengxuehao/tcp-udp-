import re
import socket
import mini_web07

# 创建一个tcp服务器套接字
# 绑定地址
# 设置监听模式
# 获取客户端的链接
# 　和客户端发送消息(发送响应)
def client_exec(client):
    # 根据不同的请求地址返回不同的页面
    # １ 得到请求数据
    request_data = client.recv(1024).decode('utf-8')
    print(request_data)
    # ２ 通过正则进行筛选出资源路径
    match = re.match(r'[^/]+/([^ ]*)', request_data).group(1)
    # 对正则数据进行判断是否匹配
    request_url = ''
    if match :
        # 匹配到了数据
        request_url = match
        print('当前路径', request_url)
        if request_url == '/':
            request_url = 'index.html'
    else:
    #　直接关闭客户端
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
            response_header = "Content-Type: text/html;charset=utf-8\r\n"
            with open('./images/%s' % request_url, 'rb')as f:
                content = f.read()
            response_body = content
            # 拼接响应报文内容
            response_content = response_line + response_header + "\r\n"
            # 发送响应报文数据
            client.send(response_content.encode("utf-8"))
            client.send(response_body)
        except Exception as e:
            print('异常',e)
            response_line = "HTTP/1.1 404 not found\r\n"
            # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
            response_header = "Content-Type: text/html;charset=utf-8\r\n"
            response_body = '无效页面'

            # 拼接响应报文内容
            response_content = response_line + response_header + "\r\n" + response_body
            # 发送响应报文数据
            client.send(response_content.encode("utf-8"))

    client.close()


def main():
    '''创建一个tcp服务器'''
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,5)
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