from http.cookiejar import CookieJar
from urllib import request,parse


# 构建一个CookieJar对象，保存cookie值
cookie = CookieJar()

cookie_handler = request.HTTPCookieProcessor(cookie)

# 构建一个自定义的opener
opener = request.build_opener(cookie_handler)

opener.addheaders = [("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36")]

url = "http://www.renren.com/PLogin.do"

data = {"email":"15881027187","password":"yhy236668777"}
data1 = parse.urlencode(data).encode("utf-8")

request1 = request.Request(url,data=data1)

response = opener.open(request1)
print(response.read().decode("utf-8"))