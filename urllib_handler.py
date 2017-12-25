from urllib import request


proxyswitch = False

# 构建一个Handler处理器对象，参数必须是一个字典
httpproxy_handler = request.ProxyHandler({'http': "124.89.33.75:9999"})

nullproxy_handler = request.ProxyHandler({})

if proxyswitch:
    opener = request.build_opener(httpproxy_handler)
else:
    opener = request.build_opener(nullproxy_handler)

request1 = request.Request('http://www.baidu.com')
respone = opener.open(request1)

print(respone.read().decode('utf-8'))

# # 构建一个全局的opener,之后所有的请求都可以用urlopen()方法去发送，也附带Handler的功能
# request.install_opener(opener)
# request1 = request.Request('http://www.baidu.com')
# response = request.urlopen(request1)
#
# print(response.read().decode('utf-8'))