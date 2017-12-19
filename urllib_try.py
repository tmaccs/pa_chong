from urllib import request

request1 = request.Request("http://www.baidu.com")
response = request.urlopen(request1)
html = response.read()
print(html)
