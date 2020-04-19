#搜狐新闻爬虫
import requests
from lxml import html


class Model(object):
    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ('{} = ({})'.format(k, v) for k, v in self.__dict__.items())
        return '\n<{}:\n  {}\n>'.format(class_name, '\n  '.join(properties))


class New(Model):
    def __init__(self):
        self.url = ""
        self.title = ""


def new_from_div(div):
    new = New()
    new.url = div.xpath('.//a[@class="h4"]/@href')[0]
    new.title = div.xpath('.//a[@class="h4"]')[0].text
    print(new.url, new.title)
    return new


def cached_url(url):
    import os
    filename = 'sohu_news.html'
    path = os.path.join('cached', filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read()
    else:
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
    return r.content


def news_from_url(url):
    page = cached_url(url)
    root = html.fromstring(page)
    new_divs = root.xpath('//div[@class="h4WP"]')
    news = [new_from_div(div) for div in new_divs]
    return news


def main():
    url = 'https://m.sohu.com/'
    news = news_from_url(url)


if __name__ == '__main__':
    main()
