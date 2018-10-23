# 创建tcp套接字，
# 绑定服务器地址，
# 设置监听模式，
# 获取服务器的链接，
# 和服务器收发消息，关闭
import socket
import re


def client_exec(client):
    '''获取请求报文过来，和执行发送消息给客户端浏览器'''
    recv_data = client.recv(1024).decode('utf-8')
    print(recv_data)
    # 正则筛选是否匹配--请求行
    match = re.match(r'[^/]+(/[^ ]*)', recv_data).group(1)
    print(match)
    request_url = ''
    if match:
        request_url = match
        print('当前的路径是', request_url)
        if request_url == '/':
            request_url = 'index.html'
    else:
        client.close()

    if request_url == '/index.html':
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Content-Type: text/html;charset=utf-8\r\n"
        # 空行
        # 响应体
        response_bady = '主页界面'
        response_content = response_line + response_header + '\r\n' + response_bady
        client.send(response_content.encode('utf-8'))
    elif request_url == "/login.html":
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Content-Type: text/html;charset=utf-8\r\n"
        # 空行
        # 响应体
        response_bady = '登录界面'
        response_content = response_line + response_header + '\r\n' + response_bady
        client.send(response_content.encode('utf-8'))
    client.close()


def main():
    '''http协议'''
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定服务器端口
    tcp_server_socket.bind(('', 1314))
    # 设置被动监听模式
    tcp_server_socket.listen(128)
    # 循环获取客户端地址，接收客户端来的消息,请求报文
    while True:
        # 获得客户端链接
        client, addr = tcp_server_socket.accept()
        # 处理请求，客户端发送来的请求报文，自动就会显示，然后给客户端回复响应报文
        client_exec(client)
        # 关闭
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
