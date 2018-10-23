import re
#
str = '''
GET /index.html HTTP/1.1
Host: 127.0.0.1:1315
Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: csrftoken=q4R6EeJKOL3iQ7tXVnRcbTWSiIGXuK7CpZFtnS8ERkFClLczuIXP7F6iAj1EfrYM'''
request_url = re.match(r'[^/]+(/[^ ]*)', str).group(1)
# ^ 非斜杠开始　^ 非空格结束
print('当前路径',request_url)



