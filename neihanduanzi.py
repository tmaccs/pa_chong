import re,ssl
from urllib import request


ssl._create_default_https_context = ssl._create_unverified_context
class Spider_neihan:
    def __init__(self):
        self.pagenum=1
        self.switch = True

    def download_page(self):
        url='https://www.qiushibaike.com/8hr/page/'+str(self.pagenum)+'/'
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
        request1 = request.Request(url,headers=headers)
        response = request.urlopen(request1)
        html = response.read().decode('utf-8')
        self.dealpage(html)
        print(url)

    def dealpage(self,html):
        pattern = re.compile('<div\sclass="content">(.*?)</div>',re.S)
        duanzis = pattern.findall(html)
        for duanzi in duanzis:
            duanzi = duanzi.replace('<span>','').replace('</span>','').replace('<br/>','')
            print('正在写段子......',duanzi)
            self.writepage(duanzi)

    def writepage(self,content):
        with open('/Users/YangHengyu/Desktop/duanzi.txt','a',encoding='utf-8') as f:
            f.write(content)

    def startwork(self):

        while self.switch:
            self.download_page()
            self.writepage('-' * 80)
            iscontinue = input('继续请回车，否则请输入exit退出获取段子')
            if iscontinue == 'exit':
                self.switch = False
            # else:
            #     self.pagenum += 1
            self.pagenum += 1



if __name__=="__main__":
    Spider_neihan = Spider_neihan()
    Spider_neihan.startwork()