# 创建一个tcp客户端，
# 创建套接字，
# 建立链接，
# 发送数据，数据内容就是请求报文
# 接收数据，
# 关闭套接字
import socket


def main():
    '''创建一个tcp的客户端'''
    tcp_client_socket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    # 创建tcp客户端套接字
    tcp_client_socket.connect ( ('127.0.0.1', 1315) )
    # 和确定的服务器端口进行链接
    request_line = 'GET / HTTP/1.1/index/html\r\n'
    request_head = 'Host: 127.0.0.1:8080\r\n'
    request_content = request_line + request_head+ "\r\n"
    # 发送消息给服务器，也就是发送浏览器版本信息给服务器
    tcp_client_socket.send(request_content.encode('utf-8'))
    recv_data = tcp_client_socket.recv(1024)
    print(recv_data.decode('utf-8'))


if __name__ == '__main__':
    main()