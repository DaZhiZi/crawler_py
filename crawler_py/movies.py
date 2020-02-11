from utils import log
from utils import ensure
from utils import isEquals
from utils import find2
from utils import find_between
from utils import load_file
from utils import list_from_str, cut_blank
import os

class Model(object):
    """
    基类, 用来显示类的信息
    """
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Movie(Model):
    """
    存储电影信息
    """
    def __init__(self):
        self.movie_id = 0
        self.name = ''
        self.score = 0
        self.quote = ''
        self.num_of_comment = 0 # 多少人评论
        self.cover_url = ''
        self.ranking = 0
        self.country = ''
        self.director = ''
        self.actor = ''
        self.year = ''
        self.type = ''

def cached_url(url):
    cached_path = 'cached_html'
    filename = 'start=' + url.split('=', 1)[-1] + '.html'
    path = os.path.join(cached_path, filename)
    # log('path', path)
    if os.path.exists(path):
        data = load_file(path)
        # log('data', data)
        return data.decode('utf-8')
    else:
        # 因为我们预先下载好了豆瓣电影 top250 的页面
        # 所以这里不需要处理 else 的情况
        # 建立文件夹
        # 发送网络请求, 把结果写入到文件夹中
        log('request')

def else_from_inform(inform):
    map = {}
    s = inform
    list = s.split('&nbsp;/&nbsp;')
    map['year'] = cut_blank(list[0])
    map['country'] = list_from_str(list[1])
    map['type'] = list_from_str(list[2])
    return map


"""
大佬的建议:
    你想一下, 如果你段代码将来在其他方法里面也要用呢, 那你得再复制一遍, 
    如果将来豆瓣把网页改了呢, 那你是不是得把所有复制的地方都改一遍？这是一方面

    这些给 m 赋值的操作应该是跟你的 class Movie 相关的, 你应该把它封装起来,
    调用者只需要按照套路调用相应的方法就行了, 不需要关系内部的实现
"""
movie_informs = { # 我的一个想法  写配置： 如果页面改变，我的就直接更改配置movie_inform
    # movie  情况特殊的，嵌套，处理字符串就比较，复杂了
    # key:       value: (left, right)
    'movie_id': ('<em class="">', '</em>'),
    'name':  ('<span class="title">', '</span>'),
    'score': ('<span class="rating_num" property="v:average">', '</span>'),
    'quote': ('<p class="quote">\n' +
                          '                                <span class="inq">', '</span>'),
}
def movie_from_divs(div):
    s = div
    m = Movie()
    m.movie_id = find_between(s, '<em class="">', '</em>')
    m.name = find_between(s, '<span class="title">', '</span>')
    m.score = find_between(s, '<span class="rating_num" property="v:average">', '</span>')
    m.quote = find_between(s, '<p class="quote">\n' +
                          '                                <span class="inq">', '</span>')
    m.num_of_comment = find_between(s, '<span property="v:best" content="10.0"></span>\n' +
                           '                                <span>', '人评价</span>')
    m.ranking = find_between(s, '<span class="rating_num" property="v:average">', '</span>')
    m.cover_url = find_between(s, 'src="', '" class="">\n' +
                             '                    </a>\n' +
                             '                </div>\n' +
                             '                <div class="info">')

    inform = find_between(s, '<br>', '\n' +
                        '                        </p>')
    m.director = find_between(s, '导演: ', '主演: ')
    m.director = m.director.split('&nbsp;&nbsp;')[0]
    m.actor = find_between(s, '主演: ', '<br>')
    map = else_from_inform(inform)
    m.year = map['year']
    m.country = map['country']
    m.type = map['type']
    return m
    pass

def divs_from_page(page): # page  每个页面
    divs = [] # divs 代表 所有的 电影 movies
    left = '<div class="item">'
    right = '</div>\n        </li>'
    index = 0
    s = page[index::]
    for i in range(25):
        div = find_between(s, left, right)
        divs.append(div)
        index += find2(s, left) + len(left)
        s = page[index::]
    log('divs', divs)
    return divs

def movies_from_url(url):
    page = cached_url(url)
    movies_divs = divs_from_page(page)
    movies = []
    for div in movies_divs:
        movie = movie_from_divs(div)
        #  movie_id=(225)
        m = {}
        for k, v in movie.__dict__.items():
            m[k] = v
        # for k, v in movie.__dict__.items():
        #     map[k] = v
        movies.append(m)
    # log('movies', movies)
    return movies
    pass


def save_movies(movies):
    # log('movies', movies)
    # log('movies type', type(movies), len(movies))
    # m = movies[0]
    # log('mvoies element', type(m))
    import json
    # JsonStr = json.dumps( Arr, ensure_ascii=False, encoding='UTF-8')
    # data = json.dumps(movies)  # 数组转换字符串
    # https://cloud.tencent.com/developer/article/1564801
    data = json.dumps(movies, ensure_ascii=False)
    filename = './movies.json'
    with open(filename, 'w', encoding='utf-8') as f: # 写入文件中 保存
        f.write(data)
        # json.dump(data, f)

def test_url():
    movies = []
    url = 'https//movie.douban.com/top250?start=0'
    movies = movies_from_url(url)
    log('movies', movies)

def main():
    # test_url()
    movies = []
    for i in range(0, 225, 25):
        url = 'https//movie.douban.com/top250?start={}'.format(i)
        log('url', url)
        movies_from_url(url)
        ms = movies_from_url(url)
        movies = movies + ms
    # log('movies', movies)
    save_movies(movies) # 保存数据
    pass



if __name__ == '__main__':
    main()