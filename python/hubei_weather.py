# 爬取湖北省10个城市本周天气
#coding:utf-8
from bs4 import BeautifulSoup
import urllib2
import csv
import sys
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

def get_data(html):
    soup = BeautifulSoup(html);
    bd = soup.body;
    final = [];
    wea0 = bd.find('div', class_='con today clearfix');

    #city name
    name0 = wea0.find('div', class_ = 'crumbs fl')
    name1 = name0.find_all('a')
    temp = []
    name2 = ''
    for t in name1:
        name2 += t.string
    temp.append(name2);
    final.append(temp);

    #weather
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
    tt = []
    final.append(tt);
    return final;
        
def writefile(data, path):
    with open(path, 'wb') as f:
        f.write(codecs.BOM_UTF8)
        f_csv = csv.writer(f)
        f_csv.writerows(data)
        f.close()

def read(str):
    return urllib2.urlopen(str).read();

if __name__ == '__main__':
    #url = 'http://www.weather.com.cn/weather/101200101.shtml';
    data = [];
    for i in range(1,10):
        num = '101200'+str(i)+'01';
        url = 'http://www.weather.com.cn/weather/'+str(num)+'.shtml';
        html = read(url)
        data += get_data(html)
    writefile(data, 'hubei weather.csv')
    print 'OK'