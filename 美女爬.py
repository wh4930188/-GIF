#conding:utf-8
import urllib.request
import re
import time
# a=1
# def get_content(url):
#     global a
#     html=urllib.request.urlopen(url)
#     content=html.read().decode()
#     # print(content)
#     html.close()
#     return content
# # src="http://wx2.sinaimg.cn/mw1024/85b205d9gy1fcy20cq8hrg206o03r1l1.gif"
# def get_img(info):
#     res= r'.*?.gif'
#     pat=re.compile(res)
#
#     imgs_code=re.findall(pat,info)
#     i=0
#     for img_url in imgs_code:
#         print(img_url)
# #         urllib.request.urlretrieve(img_url,'%s.jpg' % i)
# #         i+=1
# url="http://www.ivsky.com/bizhi/"
# info=get_content(url)

def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

def make_url(target):
    for i in range(1,13):
        url='http://www.cf131.com/meinvtu/list_%s.html' %i
        print("正在爬取的网址为：",url)
        target.send(url)


# @init
# def get1():
#     while True:
#         url=yield
#         print(url)
# make_url(get1())

@init
def getHtml(target):
    while True:
        url=yield
        req = urllib.request.Request(url)
        time.sleep(2)
        page = urllib.request.urlopen(req)  #urllib.urlopen()方法用于打开一个URL地址
        html = page.read().decode('gbk') #read()方法用于读取URL上的数据
        print(">>>>>>>>>>>>>>>>>>")
        target.send(html)
# make_url(getHtml())
@init
def getImg():
    x=0
    while True:
        html=yield
        # print(html)
# make_url(getHtml(getImg()))
        reg = r'img src="(.+?\.gif)"'    #正则表达式，得到图片地址
        imgre = re.compile(reg)     #re.compile() 可以把正则表达式编译成一个正则表达式对象.
        imglist = re.findall(imgre,html)      #re.findall() 方法读取html 中包含 imgre（正则表达式）的    数据
        # 把筛选的图片地址通过for循环遍历并保存到本地
        # 核心是urllib.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
        for imgurl in imglist:
            try:
                print("正在下载%s张邪恶图片" % x)
                urllib.request.urlretrieve(imgurl,'%s.gif' % x)
                time.sleep(1)
                x+=1
            except ValueError:
                continue
# http://www.cf131.com/meinvtu/list_3.html
# html = getHtml("http://www.cf131.com/meinvtu/")
g=make_url(getHtml(getImg()))
