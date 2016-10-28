from bs4 import BeautifulSoup
import csv
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

def write_csv(data, path):
    with open(path, 'wb') as f:
        f.write(codecs.BOM_UTF8)
        f_csv = csv.writer(f)
        f_csv.writerows(data)
        f.close()

def read_url(url):
    res = urllib2.urlopen(url).read();
    return res;

def get_data(html):
    info = []
    soup = BeautifulSoup(html)
    bd = soup.body
    article = bd.find('div', class_ = 'article')
    ol = article.find('ol', class_ = 'grid_view')
    for li in ol.find_all('li'):
        temp = []
        div_name = li.find('div', class_ = 'hd')
        name = div_name.a.span.string #影片名
        div_star = li.find('div', class_ = 'star')
        start = div_star.contents[3].string #评分
        num = div_star.contents[7].string #人数
        temp.append(name);
        temp.append(start);
        temp.append(num);
        info.append(temp)
    return info





if __name__ == '__main__':
    data = [];
    info = ['片名','评分', '评价人数']
    data.append(info);
    for i in range(10):
        url = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
        html = read_url(url)
        data += get_data(html)
    write_csv(data, 'douban250.csv')
    print('ok')
