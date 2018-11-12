import requests
from lxml import etree

# 下载豆瓣电影主页源数据
url = 'https://movie.douban.com/cinema/nowplaying/chongqing/'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
response = requests.get(url, headers=headers)
text = response.text

# 获取目标数据
movies = []
html = etree.HTML(text)  #格式转换 str—html
ul = html.xpath('//ul[@class="lists"]')[0]
# print(etree.tostring(element_nowplaying, encoding='utf-8').decode('utf-8'))  结点反转码
list_li = ul.xpath('./li')
for li in list_li:
    name = li.xpath('@data-title')[0]
    score = li.xpath('@data-score')[0]
    star = li.xpath('@data-star')[0]
    date = li.xpath('@data-release')[0]
    duration = li.xpath('@data-duration')[0]
    region = li.xpath('@data-region')[0]
    director = li.xpath('@data-director')[0]
    actors = li.xpath('@data-actors')[0]
    movie = {
        'name': name,
        'score': score,
        'star': star,
        'date': date,
        'star': star,
        'duration': duration,
        'region': region,
        'director': director,
        'actors': actors,
    }
    movies.append(movie)
print(movies)