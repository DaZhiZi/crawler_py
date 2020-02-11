from utils import log
from utils import ensure
from utils import isEquals


def get_data():
    path = './movies.json'
    import json
    p = path
    with  open(p, 'rb') as f:
        # data = json.load(f)
        data = f.read().decode('utf-8')
    log('type data', type(data))
    return json.loads(data)

def value_from_data(data, key):
    l = []
    for movie in data:
        # log('movie', movie)
        value = movie[key]
        if isinstance(value, list):
            l = l + value
        else:
            l.append(value)
    return l

# '犯罪': 45,  key: value
def map_from_list(values):
    map = {}
    for v in values:
        if v in map:
            map[v] += 1
        else:
            map[v] = 1
    return map

def content_from_data(data, key):
    values = value_from_data(data, key)
    map = map_from_list(values)
    return map

def country_from_data(data):
    key = 'country'
    d = content_from_data(data, key)
    log('d', d)
    return d

def type_from_data(data):
    key = 'type'
    d = content_from_data(data, key)
    log('d', d)
    return d

def download_image(url, filename):
    # 通过 url 获取到该图片的数据并写入文件
    import requests, os
    r = requests.get(url)

    folder = 'douban_image'
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)

    with open(path, 'wb') as f:
        f.write(r.content)

def save_cover(movies):
    for m in movies:
        name = m.name
        filename = '{}.jpg'.format(name)
        download_image(m.cover_url, filename)



def main():
    data = get_data()
    # save_cover(data)
    country_from_data(data)
    type_from_data(data)
    pass
"""
2020/02/11 20:39:16 type data <class 'str'>
2020/02/11 20:39:16 d {'美国': 126, '中国大陆': 16, '香港': 24, '法国': 21, '意大利': 10, '日本': 32, '英国': 28, '印度': 4, '瑞士': 3, '德国': 16, '加拿大': 7, '冰岛': 1, '韩国': 8, '台湾': 6, '新西兰': 3, '波兰': 1, '伊朗': 2, '澳大利亚': 5, '西班牙': 4, '丹麦': 1, '瑞典': 2, '巴西': 2, '奥地利': 1, '阿联酋': 1, '南非': 1, '阿根廷': 1, '爱尔兰': 1, '捷克': 1, '泰国': 1}
2020/02/11 20:39:16 d {'犯罪': 40, '剧情': 175, '爱情': 54, '同性': 7, '动作': 28, '喜剧': 44, '战争': 17, '灾难': 1, '动画': 32, '奇幻': 32, '历史': 10, '科幻': 20, '悬疑': 29, '冒险': 39, '歌舞': 5, '音乐': 6, '传记': 11, '家庭': 21, '惊悚': 30, '运动': 1, '纪录片': 3, '儿童': 3, '情色': 1, '西部': 3, '古装': 6, '武侠': 3, '恐怖': 2}
"""
"""
{
  '美国': 144,
  '中国大陆': 23,    
  '香港': 25,
  '法国': 24,
  '意大利': 12,
  '日本': 33,
  '英国': 34,
  '德国': 20,
  '加拿大': 7,
  '韩国': 9,
  '澳大利亚': 6,
  '西班牙': 6,
  }
"""
ten_type = {
    '犯罪': 45,
    '剧情': 194,
    '爱情': 58,
    '动作': 30,
    '喜剧': 46,
    '动画': 32,
    '奇幻': 32,
    '悬疑': 33,
    '冒险': 45,
    '惊悚': 36,
}
if __name__ == '__main__':
    main()