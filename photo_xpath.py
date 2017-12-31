from lxml import etree
from urllib import request,parse
import ssl,re


ssl._create_default_https_context = ssl._create_unverified_context

class Photo_Spider:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&'


    def gethtml(self,url):
        #通过url爬取对应页面
        request1 = request.Request(url)
        response = request.urlopen(request1)
        html = response.read().decode('utf-8')
        return html

    def loadtiezi(self,tieba_url):
        # 爬取该页贴吧中标题的url

        request1 = request.Request(tieba_url)
        response = request.urlopen(request1)
        tiezi_html = response.read().decode('utf-8')

        content = etree.HTML(tiezi_html)
        linklist = content.xpath('//div[contains(@class,"threadlist_lz")]//a[@class="j_th_tit "]/@href')
        print(linklist)
        #linklist = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        # linklist = content.xpath('//a/text()')
        for link in linklist:
            fulllink = 'https://tieba.baidu.com' + link
            # 进入该主题页
            self.loadphoto(fulllink)
            print(fulllink)



    def loadphoto(self,photo_html_url):
        # 爬取帖子里的图片链接
        # photo_html 主题页
        if photo_html_url:
            photo_html = self.gethtml(photo_html_url)
            photo_url_list = etree.HTML(photo_html).xpath('//img[@class="BDE_Image"]/@src')

            # 通过每个图片链接进入图片页面，下载保存到本地
            # 若该页有图片

            for photo_url in photo_url_list:
                request1 = request.Request(photo_url)
                response = request.urlopen(request1)
                photo = response.read()
                filename = photo_url[-10:]
                print('正在下载:',filename)
                with open('/Users/YangHengyu/Desktop/photos/'+filename,'wb') as f:
                    f.write(photo)

    def start_spider(self):
        tieba_name = input('请输入贴吧名:')
        tieba_name = parse.urlencode({'kw':tieba_name})

        start_page = input('请输入从第几页开始：')
        end_page = input('请输入到第几页结束：')
        for i in range(int(start_page),(int(end_page)+1)):
            tieba_url = self.url + tieba_name + '&pn=' + str((i-1)*50)
            self.loadtiezi(tieba_url)
            print('第%s页内容中的图片下载完成'%i)
            print('-'*80)


if __name__ == "__main__":
    photospider = Photo_Spider()
    photospider.start_spider()