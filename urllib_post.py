from urllib import request,parse
import json

url = "http://fy.iciba.com/ajax.php?a=fy"
headers = {
    "Host": "fy.iciba.com",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7"
}
key = input("请输入要翻译的文字：")
form_data = {
    'f':'en',
    't':'zh',
    'w':key
}

data = parse.urlencode(form_data).encode(encoding='utf-8')
request1 = request.Request(url,data=data,headers=headers)
respond = request.urlopen(request1)
html = respond.read()

myjson = json.loads(html)  # data是向 api请求的响应数据，data必须是字符串类型的
newjson = json.dumps(myjson, ensure_ascii=False)  # ensure_ascii=False 就不会用 ASCII 编码，中文就可以正常显示了

print(newjson)
print(html)




