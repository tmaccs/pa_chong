import urllib
from urllib import request

def getweb(fullurl,filename):
    """

    :param fullurl: 完整的url
    :param filename: 正在下载的页数
    :return: html
    """
    print('正在下载页面',filename)
    print(fullurl)
    request1 = request.Request(fullurl)
    response = request.urlopen(request1)
    html = response.read()
    return html

def writeweb(html):
    with open('/Users/YangHengyu/Desktop/web','wb') as f :
        f.write(html)
        print('写文件完毕')
        print('-'*30)


def webSpider(url,num):
    pagenum = 50*(int(num)-1)
    fullurl = url + "&pn=" + str(pagenum)
    filename = '第'+str(num)+'页'
    html = getweb(fullurl,filename)
    writeweb(html)



if __name__=='__main__':
    name = input('请输入贴吧名：')
    num = input('请输入要看的页面:')
    url = 'http://tieba.baidu.com/f?kw='

    wd = {'wd': name}
    nameurl = name
    url = url + nameurl
    webSpider(url, num)