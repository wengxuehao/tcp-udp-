import re
import socket



# 创建一个tcp服务器套接字
# 绑定地址
# 设置监听模式
# 获取客户端的链接
# 　和客户端发送消息(发送响应)



def main():
    '''返回固定页面数据到客户端'''
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口 # 设置监听模式 # 端口复用
    tcp_server_socket.bind(('', 1315))
    tcp_server_socket.listen(128)
    client, addr = tcp_server_socket.accept()
    request_data = client.recv(1024).decode('utf-8')
    # 接收客户端请求报文
    print(request_data)
    # 从请求报文里面正则获取到路径－－request_url
    # request_url = re.match(r'', request_data).group()
    # request_url = re.match(r'[^/]+/([^ ]*)',request_data).group(1)
    # print('当前路径', request_url)
    # if request_url == 'index.html':
    response_line = "HTTP/1.1 200 OK\r\n"
    # Content-Type: text/html;charset=utf-8: 告诉客户端我给你发送数据的内容类型及编码方式
    response_header = "Content-Type: text/html;charset=utf-8\r\n"
    response_body = "hahhah"

    # 拼接响应报文内容
    response_content = response_line + response_header + "\r\n" + response_body
    # 发送响应报文数据
    client.send(response_content.encode("utf-8"))
    client.close()


if __name__ == '__main__':
    main()
