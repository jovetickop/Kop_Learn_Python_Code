#爬取武汉市本周天气
#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import csv
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

def get_data(html):
    final = [];
    soup = BeautifulSoup(html);
    bd = soup.body;

    wea0 = bd.find('div', class_='con today clearfix');

    #城市名
    name0 = wea0.find('div', class_ = 'crumbs fl')
    name1 = name0.find_all('a')
    name2 = ''
    for t in name1:
        name2 += t.string

    wea1 = wea0.find('div',{'id':'7d'})
    wea2 = wea1.find('ul')
    for li in wea2.find_all('li'):
        temp = [];
        date = li.h1.string
        wea = li.find('p',class_ = 'wea').string
        tem = li.find('p', class_ = 'tem')
        high = tem.span.string
        low = tem.i.string
        wind = li.find('p', class_ = 'win').i.string
        temp.append(date);
        temp.append(wea);
        temp.append(high+'/'+low);
        temp.append(wind);
        final.append(temp);
    return final, name2;
        
def writefile(data, path):
    with open(path, 'wb') as f:
        f.write(codecs.BOM_UTF8)
        f_csv = csv.writer(f)
        f_csv.writerows(data)
        f.close()

def read(str):
    return urllib2.urlopen(str).read();

if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101200101.shtml';
    html = read(url)
    data = get_data(html)
    # print data[1]
    writefile(data[0], data[1]+'天气.csv')
    print 'OK'
