from urllib import request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.zhihu.com/#signin'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "accept-language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
    "Cookie": "d_c0=AAAACpCS2AmPTqaPbVGvhRe98UG-yDkG6_E=|1461932757; _zap=080124f3-5ed0-4753-b968-69ec4314ca1a; q_c1=4297196535cc44039ae4d78c44d8b52e|1503416053000|1455784257000; __utmz=51854390.1501245825.7.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.000--|2=registration_date=20130702=1^3=entry_date=20160218=1; q_c1=4297196535cc44039ae4d78c44d8b52e|1511363064000|1455784257000; aliyungf_tc=AQAAAHMIOwOD7g4ABwvet9R+OCZrkMsL; _xsrf=96deb87c-1050-40fa-8475-6b1c49e7e6ba; __utma=51854390.89319140.1455784970.1507208760.1513786465.11; __utmb=51854390.0.10.1513786465; __utmc=51854390; r_cap_id=MWQ2N2ExMTlkNTBiNGQxMWFiNTUyNzE3ZjU1MjBhZjA=|1513787499|210df96d70fb209e9537a79736b1c52dbd48f52c; cap_id=ZDcxZmJjZDNjZDIwNGM1YmE2M2ZmNjk4YjI5Y2E2M2I=|1513787499|32bb089c2a96c81b333aaf5f3114f9f1708bc3fd; z_c0=Mi4xVXI4UEFBQUFBQUFBQUFBS2tKTFlDUmNBQUFCaEFsVk45OTRuV3dDNUhaTUstU1M3dldjcHczQ2taZVQtOFRVZHN3|1513787639|f615739c199e7a0005f4fd9c29bb33f955bb2fda"
}

request1 = request.Request(url,headers=headers)
reponse = request.urlopen(request1)
html = reponse.read()
print(str(html,'utf-8'))
with open('/Users/YangHengyu/Desktop/web', 'wb') as f:
    f.write(html)

