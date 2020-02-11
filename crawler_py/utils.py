import time


def log(*args, **kwargs):
    # time.time() 返回 unix time
    # 如何把 unix time 转换为普通人类可以看懂的格式呢？
    format = '%Y/%m/%d %H:%M:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    print(dt, *args, **kwargs)


def ensure(condition, message):
    if not condition:
        log('xxxxx 测试失败', message)
    else:
        log('>>>>> 测试成功', message)


def isEquals(a, b, message):
    import json
    if json.dumps(a) == json.dumps(b):
        log('***  {} 测试成功, 大侄子牛逼呀'.format(message))
    else:
        log('xxxxx 测试失败 结果（{}）  预期（{}）, {}'.format(a, b, message))


import random


def random_num(num1, num2):
    return random.randint(num1, num2)


def exchange(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp



def load_codes():
    path = "code.txt"
    list = []
    with open(path) as all:
        for line in all:
            list.append(line)
    return list

def find2(s1, s2):
    # s1 s2 都是 string
    # 两个 str 的长度不限
    # 返回 s2 在 s1 中的下标, 从 0 开始, 如果不存在则返回 -1
    space = len(s2)
    for i in range(len(s1)):
        str = s1[i : i + space:]
        # log('str', str, i)
        if str == s2:
            # log('i', i, s2)
            return i
    return -1
    pass

def test_find2():
    find2('01234567', '345')
    
# test_find2()


def find_between(str, left, right):
    s = str
    center = ''
    l = find2(s, left)
    data = s[l:: ]
    # log('data', data)
    r = find2(data, right) + l
    start = l + len(left)
    end = r
    # log('start', start, 'end', end)
    if start > 0 and end > 0:
        center = s[start: end:]
        # log('center', center)
    return center
    pass

def test_find_between():
    msg = 'find_between'
    s1 = 'meet #<gua># halfway'
    s2 = 'meet #<gua># #<high>#way'
    left = '#<'
    right = '># '
    isEquals(find_between(s1, left, right), 'gua', msg)
    isEquals(find_between(s2, left, right), 'gua', msg)

# test_find_between()

def load_file(path):
    p = path
    with open(p, 'rb') as f:
        data = f.read()
        return data
    pass

def is_space(str):
    r = False
    for s in str:
        if s == ' ':
            return True
    return r


def list_from_str(str):
    list = []
    if not is_space(str): # 是否包含空格
        list.append(str)
    else:
        list = str.split(' ')
    return list

def cut_blank(str):
    r = ''
    for i in str:
        if i != ' ':
            r += i
    return r