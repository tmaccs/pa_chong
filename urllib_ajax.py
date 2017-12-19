from urllib import request,parse
import ssl,json


ssl._create_default_https_context = ssl._create_unverified_context
# 直接得到json数据的URL
json_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action'

url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

form_data = {
    'start': '20',
    'limit': '20'
}
data = parse.urlencode(form_data).encode('utf-8')
request1 = request.Request(json_url,data=data,headers=headers)

html = request.urlopen(request1).read()
myjson = json.loads(html)  # data是向 api请求的响应数据，data必须是字符串类型的
newjson = json.dumps(myjson, ensure_ascii=False)  # ensure_ascii=False 就不会用 ASCII 编码，中文就可以正常显示了

print(newjson)